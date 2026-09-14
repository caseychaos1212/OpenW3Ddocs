import importlib.util
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().parents[1] / 'generate_openw3d_scripts_reference.py'
SPEC = importlib.util.spec_from_file_location('script_reference', MODULE_PATH)
reference = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = reference
SPEC.loader.exec_module(reference)


class CommentExtractionTests(unittest.TestCase):
    def extract(self, source):
        with patch.object(Path, 'read_text', return_value=source):
            return reference.extract_scripts_from_file(Path('sample.cpp'), {})

    def test_commented_registrations_and_callbacks_are_not_indexed(self):
        source = '''/* DECLARE_SCRIPT(Live, "Obsolete:int") { void Damaged() {} }; */
// DECLARE_SCRIPT(Disabled, "") { void Killed() {} };
/* Creates an object when attached. */
DECLARE_SCRIPT(Live, "Count=1:int")
{
    void Created() { Commands->Create_Object("Object", position); }
    // void Timer_Expired() { Commands->Destroy_Object(obj); }
    /* void Damaged() { Commands->Set_Health(obj, 100); } */
};
'''
        entries = self.extract(source)
        self.assertEqual([entry.name for entry in entries], ['Live'])
        self.assertEqual(entries[0].source_line, 4)
        self.assertEqual(entries[0].parameter_description, 'Count=1:int')
        self.assertEqual(entries[0].event_hooks, ['Created'])
        self.assertEqual(entries[0].command_calls, ['Create_Object'])
        self.assertEqual(entries[0].source_notes, 'Creates an object when attached.')

    def test_commented_directives_do_not_change_active_branch(self):
        source = '''/*
#if 0
*/
#if 0 // disabled prototype
DECLARE_SCRIPT(Disabled, "") {};
#else
DECLARE_SCRIPT(Live, "") {};
#endif
'''
        entries = self.extract(source)
        self.assertEqual([entry.name for entry in entries], ['Live'])
        self.assertEqual(entries[0].source_line, 7)

    def test_comment_delimiters_inside_literals_survive(self):
        source = r'''const char *url = "https://example.test/*path*/";
const char *quote = "escaped \" // still a string";
char slash = '/'; /* removed */
'''
        masked = reference.mask_cpp_comments(source)
        self.assertEqual(len(masked), len(source))
        self.assertEqual(masked.count('\n'), source.count('\n'))
        self.assertIn('"https://example.test/*path*/"', masked)
        self.assertIn(r'"escaped \" // still a string"', masked)
        self.assertNotIn('removed', masked)

    def test_comments_between_registration_tokens_are_whitespace(self):
        entries = self.extract('DECLARE_SCRIPT /* comment */ (Live, "URL=https://host:int") {};')
        self.assertEqual([entry.name for entry in entries], ['Live'])
        self.assertEqual(entries[0].parameter_description, 'URL=https://host:int')

    def test_backslash_continues_line_comment(self):
        source = '// old prototype \\\nDECLARE_SCRIPT(Disabled, "") {};\nDECLARE_SCRIPT(Live, "") {};\n'
        self.assertEqual([entry.name for entry in self.extract(source)], ['Live'])

    def test_disabled_script_is_not_documentation_for_next_script(self):
        entries = self.extract('/* DECLARE_SCRIPT(Old, "") {} */\nDECLARE_SCRIPT(Live, "") {};')
        self.assertEqual([entry.name for entry in entries], ['Live'])
        self.assertEqual(entries[0].source_notes, '')
        self.assertEqual(entries[0].summary_source, 'heuristic')

    def test_comment_brace_does_not_start_class_body(self):
        entries = self.extract('DECLARE_SCRIPT(Live, "") // {\n{ void Created() {} };')
        self.assertEqual(entries[0].event_hooks, ['Created'])


if __name__ == '__main__':
    unittest.main()
