#!/usr/bin/env python3
"""Generate an OpenW3D script catalog and RST reference pages."""

from __future__ import annotations

import argparse
import ast
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_ROOT = REPO_ROOT.parent / "OpenW3D" / "Code" / "Scripts"
DEFAULT_OUTPUT_ROOT = REPO_ROOT / "scripts" / "reference"
DEFAULT_CATALOG_PATH = REPO_ROOT / "scripts" / "openw3d-script-catalog.json"
DEFAULT_OVERRIDES_PATH = REPO_ROOT / "scripts" / "openw3d-script-overrides.json"

SCRIPT_EVENTS = [
    "Created",
    "Destroyed",
    "Killed",
    "Damaged",
    "Custom",
    "Sound_Heard",
    "Enemy_Seen",
    "Action_Complete",
    "Timer_Expired",
    "Animation_Complete",
    "Poked",
    "Entered",
    "Exited",
]

PERSISTENCE_HOOKS = [
    "Save_Data",
    "Load_Data",
    "Register_Auto_Save_Variables",
]

SUMMARY_COMMAND_GROUPS = [
    ({"Action_Goto", "Action_Attack", "Action_Reset", "Action_Enter_Exit"}, "drives AI action commands"),
    ({"Start_Timer", "_Start_Timer"}, "uses timers"),
    ({"Send_Custom_Event"}, "sends custom events"),
    ({"Create_Object", "Create_Object_At_Bone", "Destroy_Object"}, "creates or destroys objects"),
    ({"Create_Explosion"}, "creates explosions"),
    ({"Set_Animation", "Set_Animation_Frame", "Set_Animation_Loop"}, "controls animation playback"),
    ({"Create_2D_Sound", "Create_3D_Sound_At_Bone", "Create_3D_Sound_At_Position"}, "plays sounds"),
    ({"Give_PowerUp", "Select_Weapon", "Clear_Weapons"}, "changes inventory or weapons"),
    ({"Set_Objective_Status", "Add_Objective", "Remove_Objective"}, "updates objectives"),
    ({"Innate_Enable", "Innate_Disable", "Innate_Soldier_Enable_Enemy_Seen"}, "changes innate AI behavior"),
    ({"Create_Conversation", "Start_Conversation"}, "starts conversations"),
]

DECLARE_SCRIPT_RE = re.compile(
    r"DECLARE_SCRIPT\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*,\s*((?:\"(?:[^\"\\]|\\.)*\"\s*)+)\)",
    re.S,
)
STRING_LITERAL_RE = re.compile(r"\"(?:[^\"\\]|\\.)*\"")


@dataclass
class ScriptEntry:
    name: str
    source_file: str
    source_line: int
    category: str
    parameter_description: str
    parameters: list[dict[str, str]]
    event_hooks: list[str]
    persistence_hooks: list[str]
    command_calls: list[str]
    summary: str
    summary_source: str
    source_notes: str


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-root",
        type=Path,
        default=DEFAULT_SOURCE_ROOT,
        help="Path to OpenW3D/Code/Scripts",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Directory to write RST reference pages into",
    )
    parser.add_argument(
        "--catalog-path",
        type=Path,
        default=DEFAULT_CATALOG_PATH,
        help="Path to write the generated JSON catalog to",
    )
    parser.add_argument(
        "--overrides-path",
        type=Path,
        default=DEFAULT_OVERRIDES_PATH,
        help="Path to the manual override JSON file",
    )
    args = parser.parse_args()

    source_root = args.source_root.resolve()
    if not source_root.is_dir():
        raise SystemExit(f"Source root does not exist: {source_root}")

    overrides = load_overrides(args.overrides_path)
    scripts_by_file: dict[str, list[ScriptEntry]] = defaultdict(list)

    for path in sorted(source_root.glob("*.cpp")):
        for entry in extract_scripts_from_file(path, overrides):
            scripts_by_file[entry.source_file].append(entry)

    for entries in scripts_by_file.values():
        entries.sort(key=lambda item: item.name.lower())

    all_entries = [
        entry
        for source_file in sorted_source_files(scripts_by_file)
        for entry in scripts_by_file[source_file]
    ]

    catalog = build_catalog(source_root, all_entries, scripts_by_file)
    write_catalog(args.catalog_path, catalog)
    write_reference_pages(args.output_root, source_root, catalog, scripts_by_file)
    return 0


def load_overrides(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("scripts", {})


def build_catalog(
    source_root: Path,
    all_entries: list[ScriptEntry],
    scripts_by_file: dict[str, list[ScriptEntry]],
) -> dict[str, object]:
    category_counts = Counter(entry.category for entry in all_entries)
    summary_source_counts = Counter(entry.summary_source for entry in all_entries)
    files = []
    for source_file in sorted_source_files(scripts_by_file):
        entries = scripts_by_file[source_file]
        files.append(
            {
                "source_file": source_file,
                "category": entries[0].category,
                "script_count": len(entries),
                "page_slug": slugify(source_file),
            }
        )

    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_root": str(source_root),
        "script_count": len(all_entries),
        "file_count": len(files),
        "category_counts": dict(sorted(category_counts.items())),
        "summary_source_counts": dict(sorted(summary_source_counts.items())),
        "files": files,
        "scripts": [
            {
                "name": entry.name,
                "source_file": entry.source_file,
                "source_line": entry.source_line,
                "category": entry.category,
                "parameter_description": entry.parameter_description,
                "parameters": entry.parameters,
                "event_hooks": entry.event_hooks,
                "persistence_hooks": entry.persistence_hooks,
                "command_calls": entry.command_calls,
                "summary": entry.summary,
                "summary_source": entry.summary_source,
                "source_notes": entry.source_notes,
            }
            for entry in all_entries
        ],
    }


def write_catalog(path: Path, catalog: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(catalog, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def write_reference_pages(
    output_root: Path,
    source_root: Path,
    catalog: dict[str, object],
    scripts_by_file: dict[str, list[ScriptEntry]],
) -> None:
    generated_root = output_root / "generated"
    generated_root.mkdir(parents=True, exist_ok=True)
    for old_page in generated_root.glob("*.rst"):
        old_page.unlink()

    output_root.mkdir(parents=True, exist_ok=True)
    (output_root / "index.rst").write_text(
        render_reference_index(catalog, scripts_by_file),
        encoding="utf-8",
    )

    for source_file in sorted_source_files(scripts_by_file):
        entries = scripts_by_file[source_file]
        page_path = generated_root / f"{slugify(source_file)}.rst"
        page_path.write_text(
            render_source_file_page(source_root, source_file, entries),
            encoding="utf-8",
        )


def render_reference_index(
    catalog: dict[str, object],
    scripts_by_file: dict[str, list[ScriptEntry]],
) -> str:
    lines = [
        "OpenW3D Script Reference",
        "========================",
        "",
        "This section is generated from active ``DECLARE_SCRIPT(...)`` registrations",
        "found in the local OpenW3D ``Code/Scripts`` tree.",
        "",
        f"* Active scripts indexed: ``{catalog['script_count']}``",
        f"* Source files indexed: ``{catalog['file_count']}``",
        "* Summary precedence: manual override, source comment, then heuristic",
        "",
        "The machine-readable catalog for future LevelEditQt integration is stored",
        "in ``scripts/openw3d-script-catalog.json``. Manual overrides live in",
        "``scripts/openw3d-script-overrides.json``.",
        "",
        "Categories",
        "----------",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "",
        "   * - Category",
        "     - Source Files",
        "     - Scripts",
    ]

    category_to_files: dict[str, list[str]] = defaultdict(list)
    for source_file in sorted_source_files(scripts_by_file):
        category_to_files[scripts_by_file[source_file][0].category].append(source_file)

    for category in sorted(category_to_files):
        lines.extend(
            [
                f"   * - ``{category}``",
                f"     - ``{len(category_to_files[category])}``",
                f"     - ``{sum(len(scripts_by_file[name]) for name in category_to_files[category])}``",
            ]
        )

    lines.extend(
        [
            "",
            "By Source File",
            "--------------",
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "",
        ]
    )

    for source_file in sorted_source_files(scripts_by_file):
        lines.append(f"   generated/{slugify(source_file)}")

    return "\n".join(lines) + "\n"


def render_source_file_page(source_root: Path, source_file: str, entries: list[ScriptEntry]) -> str:
    title = source_file
    underline = "=" * len(title)
    rel_source = f"Code/Scripts/{source_file}"
    lines = [
        title,
        underline,
        "",
        f"* Category: ``{entries[0].category}``",
        f"* Active scripts: ``{len(entries)}``",
        f"* Source: ``{rel_source}``",
        "",
    ]

    for entry in entries:
        heading = entry.name
        lines.extend(
            [
                heading,
                "-" * len(heading),
                "",
                entry.summary,
                "",
                f"* Source line: ``{entry.source_line}``",
                f"* Event hooks: {format_code_list(entry.event_hooks) or 'none detected'}",
                f"* Persistence hooks: {format_code_list(entry.persistence_hooks) or 'none detected'}",
                f"* Key engine calls: {format_code_list(entry.command_calls[:8]) or 'none detected'}",
                f"* Summary source: ``{entry.summary_source}``",
                "",
            ]
        )
        if entry.parameter_description:
            lines.extend(
                [
                    "Parameter Description::",
                    "",
                    *indent_lines(wrap_literal(entry.parameter_description)),
                    "",
                ]
            )
        if entry.source_notes:
            lines.extend(
                [
                    "Source Notes::",
                    "",
                    *indent_lines(entry.source_notes.splitlines()),
                    "",
                ]
            )

    return "\n".join(lines).rstrip() + "\n"


def indent_lines(lines: Iterable[str]) -> list[str]:
    return [f"   {line}" if line else "" for line in lines]


def wrap_literal(text: str, width: int = 100) -> list[str]:
    return re.findall(rf".{{1,{width}}}(?:, |$)", text) or [text]


def format_code_list(items: list[str]) -> str:
    if not items:
        return ""
    return ", ".join(f"``{item}``" for item in items)


def extract_scripts_from_file(path: Path, overrides: dict[str, dict[str, str]]) -> list[ScriptEntry]:
    source_text = path.read_text(encoding="utf-8", errors="ignore")
    active_text = preprocess_source(source_text)
    scripts = []

    for match in DECLARE_SCRIPT_RE.finditer(active_text):
        name = match.group(1)
        parameter_description = decode_string_literals(match.group(2))
        class_body = extract_class_body(active_text, match.end())
        source_notes = extract_preceding_comment(active_text, match.start())
        comment_summary = summarize_source_notes(source_notes, name)
        override = overrides.get(name, {})
        summary, summary_source = choose_summary(
            name=name,
            source_file=path.name,
            override=override,
            comment_summary=comment_summary,
            class_body=class_body,
        )
        scripts.append(
            ScriptEntry(
                name=name,
                source_file=path.name,
                source_line=line_number_for_offset(active_text, match.start()),
                category=categorize_source_file(path.name),
                parameter_description=parameter_description,
                parameters=parse_parameter_description(parameter_description),
                event_hooks=find_named_functions(class_body, SCRIPT_EVENTS),
                persistence_hooks=find_named_functions(class_body, PERSISTENCE_HOOKS),
                command_calls=find_command_calls(class_body),
                summary=summary,
                summary_source=summary_source,
                source_notes=source_notes,
            )
        )

    return scripts


def preprocess_source(text: str) -> str:
    lines = text.splitlines(keepends=True)
    stack: list[dict[str, object]] = []
    output = []

    for line in lines:
        directive = re.match(r"\s*#\s*(if|ifdef|ifndef|elif|else|endif)\b(.*)", line)
        if directive:
            kind = directive.group(1)
            rest = directive.group(2).strip()
            if kind in {"if", "ifdef", "ifndef"}:
                parent_active = all(frame["branch_active"] for frame in stack) if stack else True
                condition = evaluate_condition(kind, rest)
                branch_active = parent_active and condition
                stack.append(
                    {
                        "parent_active": parent_active,
                        "matched": bool(condition),
                        "branch_active": branch_active,
                    }
                )
            elif kind == "elif" and stack:
                frame = stack[-1]
                parent_active = bool(frame["parent_active"])
                if bool(frame["matched"]):
                    frame["branch_active"] = False
                else:
                    condition = evaluate_condition("if", rest)
                    frame["branch_active"] = parent_active and condition
                    frame["matched"] = bool(condition)
            elif kind == "else" and stack:
                frame = stack[-1]
                parent_active = bool(frame["parent_active"])
                frame["branch_active"] = parent_active and not bool(frame["matched"])
                frame["matched"] = True
            elif kind == "endif" and stack:
                stack.pop()

            output.append("\n" if line.endswith("\n") else "")
            continue

        active = all(frame["branch_active"] for frame in stack) if stack else True
        output.append(line if active else ("\n" if line.endswith("\n") else ""))

    return "".join(output)


def evaluate_condition(kind: str, rest: str) -> bool:
    if kind == "if":
        stripped = rest.replace(" ", "")
        if stripped == "0":
            return False
        if stripped == "1":
            return True
    return True


def decode_string_literals(text: str) -> str:
    parts = []
    for token in STRING_LITERAL_RE.findall(text):
        parts.append(ast.literal_eval(token))
    return "".join(parts)


def extract_class_body(text: str, start_index: int) -> str:
    brace_start = text.find("{", start_index)
    if brace_start == -1:
        return ""

    depth = 0
    i = brace_start
    state = "code"
    while i < len(text):
        ch = text[i]
        nxt = text[i + 1] if i + 1 < len(text) else ""

        if state == "code":
            if ch == "/" and nxt == "/":
                state = "line_comment"
                i += 2
                continue
            if ch == "/" and nxt == "*":
                state = "block_comment"
                i += 2
                continue
            if ch == '"':
                state = "string"
                i += 1
                continue
            if ch == "'":
                state = "char"
                i += 1
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return text[brace_start + 1 : i]
        elif state == "line_comment":
            if ch == "\n":
                state = "code"
        elif state == "block_comment":
            if ch == "*" and nxt == "/":
                state = "code"
                i += 2
                continue
        elif state == "string":
            if ch == "\\":
                i += 2
                continue
            if ch == '"':
                state = "code"
        elif state == "char":
            if ch == "\\":
                i += 2
                continue
            if ch == "'":
                state = "code"
        i += 1

    return ""


def extract_preceding_comment(text: str, decl_start: int) -> str:
    cursor = decl_start
    while cursor > 0 and text[cursor - 1].isspace():
        cursor -= 1
    if not text[:cursor].endswith("*/"):
        return ""

    comment_start = text.rfind("/*", 0, cursor)
    if comment_start == -1:
        return ""

    between = text[cursor:decl_start]
    if between.count("\n") > 3:
        return ""

    raw = text[comment_start:cursor]
    cleaned = sanitize_comment(raw)
    if looks_like_file_header(cleaned):
        return ""
    return cleaned


def sanitize_comment(raw: str) -> str:
    body = raw
    if body.startswith("/*"):
        body = body[2:]
    if body.endswith("*/"):
        body = body[:-2]

    lines = []
    for line in body.splitlines():
        line = re.sub(r"^\s*\*+\s?", "", line.rstrip())
        line = line.rstrip()
        lines.append(line)

    text = "\n".join(lines).strip()
    text = re.sub(r"^Editor Script\s*-\s*", "", text)
    text = re.sub(r"^Editor Script\s*", "", text)
    return text.strip()


def looks_like_file_header(comment: str) -> bool:
    header_markers = ["FILE", "PROGRAMMER", "VERSION INFO", "$Archive:"]
    return sum(marker in comment for marker in header_markers) >= 2


def summarize_source_notes(source_notes: str, script_name: str) -> str:
    if not source_notes:
        return ""

    lines = [line.strip() for line in source_notes.splitlines()]
    summary_lines = []
    for line in lines:
        if not line:
            continue
        if line == script_name or line.replace("_", "") == script_name.replace("_", ""):
            continue
        if line.lower().startswith("parameters"):
            break
        if line.startswith("DEBUG"):
            continue
        if "= " in line or "\t=" in line or re.search(r"\b=\b", line):
            break
        summary_lines.append(line)
        if len(summary_lines) == 2:
            break

    summary = " ".join(summary_lines).strip()
    summary = re.sub(r"\s+", " ", summary)
    return summary


def choose_summary(
    *,
    name: str,
    source_file: str,
    override: dict[str, str],
    comment_summary: str,
    class_body: str,
) -> tuple[str, str]:
    manual_summary = (override.get("summary") or "").strip()
    if manual_summary:
        return manual_summary, "manual"
    if comment_summary:
        return comment_summary, "source comment"
    return build_heuristic_summary(name, source_file, class_body), "heuristic"


def build_heuristic_summary(name: str, source_file: str, class_body: str) -> str:
    event_hooks = find_named_functions(class_body, SCRIPT_EVENTS)
    command_calls = find_command_calls(class_body)

    phrases = []
    if "Created" in event_hooks:
        phrases.append("initializes behavior when the object is created")
    if "Custom" in event_hooks:
        phrases.append("responds to custom events")
    if "Timer_Expired" in event_hooks:
        phrases.append("continues work on timer callbacks")
    if "Killed" in event_hooks or "Destroyed" in event_hooks:
        phrases.append("reacts to destruction state")
    if "Poked" in event_hooks:
        phrases.append("handles player poke interaction")
    if "Entered" in event_hooks or "Exited" in event_hooks:
        phrases.append("watches enter or exit events")

    for commands, phrase in SUMMARY_COMMAND_GROUPS:
        if any(command in command_calls for command in commands):
            phrases.append(phrase)

    if not phrases and event_hooks:
        phrases.append("implements script callbacks")
    if not phrases and command_calls:
        phrases.append("calls into engine script commands")
    if not phrases:
        phrases.append("has no extracted behavior summary yet")

    primary = "; ".join(dict.fromkeys(phrases))
    return f"{name} in {source_file} {primary}."


def find_named_functions(class_body: str, names: list[str]) -> list[str]:
    found = []
    for name in names:
        if re.search(rf"\b{name}\s*\(", class_body):
            found.append(name)
    return found


def find_command_calls(class_body: str) -> list[str]:
    calls = []
    for match in re.finditer(r"Commands->(_?[A-Za-z0-9_]+)\s*\(", class_body):
        call = match.group(1)
        if call not in calls:
            calls.append(call)
    return calls


def parse_parameter_description(description: str) -> list[dict[str, str]]:
    if not description.strip():
        return []

    parameters = []
    for raw_param in description.split(","):
        token = raw_param.strip()
        if not token:
            continue

        type_name = ""
        default_value = ""
        name = token

        if ":" in token:
            left, type_name = token.rsplit(":", 1)
            name = left.strip()
            type_name = type_name.strip()

        if "=" in name:
            left, default_value = name.split("=", 1)
            name = left.strip()
            default_value = default_value.strip()
        else:
            name = name.strip()

        parameters.append(
            {
                "name": name,
                "type": type_name,
                "default": default_value,
                "raw": token,
            }
        )

    return parameters


def categorize_source_file(source_file: str) -> str:
    lower_name = source_file.lower()
    if lower_name.startswith("toolkit"):
        return "toolkit"
    if lower_name.startswith("mission") or lower_name == "mission08.cpp":
        return "mission"
    if lower_name.startswith("test_") or source_file in {"PRDemo.cpp", "DrMobius.cpp"}:
        return "test-and-prototype"
    return "misc"


def line_number_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def slugify(name: str) -> str:
    stem = Path(name).stem.lower()
    return re.sub(r"[^a-z0-9]+", "-", stem).strip("-")


def sorted_source_files(source_files: Iterable[str]) -> list[str]:
    return sorted(source_files, key=str.lower)


if __name__ == "__main__":
    raise SystemExit(main())
