"""Runner contract tests; mock model execution, never contact external services."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('origin_agent', Path(__file__).with_name('agent.py'))
agent = importlib.util.module_from_spec(spec)
spec.loader.exec_module(agent)

class RunnerTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / 'ops/agents').mkdir(parents=True)
        (self.root / 'ops/brief.json').write_text(json.dumps({'city': None, 'dispatch_mode': 'draft_only'}))
        (self.root / 'ops/agents/analyst.md').write_text('Analyst role')
        self.root_patch = patch.object(agent, 'ROOT', self.root)
        self.root_patch.start()
    def tearDown(self):
        self.root_patch.stop()
        self.temp.cleanup()
    def invoke(self):
        with patch('sys.argv', ['agent.py', 'run', 'analyst', '--task', 'Audit $(echo never)']), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return agent.main()
    def test_task_is_stdin_not_shell_command(self):
        def fake(command, **kwargs):
            self.assertEqual(command[command.index('--sandbox') + 1], 'read-only')
            self.assertNotIn('shell', kwargs)
            self.assertIn('$(echo never)', kwargs['input'])
            Path(command[command.index('--output-last-message') + 1]).write_text('No evidence of paid customers.')
            return subprocess.CompletedProcess(command, 0)
        with patch.object(agent.shutil, 'which', return_value='/bin/codex'), patch.object(agent.subprocess, 'run', side_effect=fake):
            self.assertEqual(self.invoke(), 0)
        self.assertEqual(len(list((self.root / 'ops/runs').glob('*.md'))), 1)
        self.assertFalse(list((self.root / 'ops/runs').glob('*.partial.md')))
    def test_nonzero_exit_is_preserved(self):
        with patch.object(agent.shutil, 'which', return_value='/bin/codex'), patch.object(agent.subprocess, 'run', return_value=subprocess.CompletedProcess([], 7)):
            self.assertEqual(self.invoke(), 7)
    def test_success_without_report_is_failure(self):
        with patch.object(agent.shutil, 'which', return_value='/bin/codex'), patch.object(agent.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0)):
            self.assertEqual(self.invoke(), 2)
    def test_timeout_is_failure(self):
        with patch.object(agent.shutil, 'which', return_value='/bin/codex'), patch.object(agent.subprocess, 'run', side_effect=subprocess.TimeoutExpired('codex', 600)):
            self.assertEqual(self.invoke(), 2)
    def test_product_research_uses_its_budget_not_service_brief(self):
        (self.root / 'ops/product-brief.json').write_text(json.dumps({'total_budget_idr': 1000000, 'starting_category': 'FMCG'}))
        (self.root / 'ops/agents/product-hunter.md').write_text('Product research role')
        prompt = agent.make_prompt('product-hunter', 'Research goods')
        self.assertIn('1000000', prompt)
        self.assertIn('FMCG', prompt)
        self.assertIn('ops/PRODUCT-HUNTER.md', prompt)
        self.assertNotIn('ops/STRATEGI.md', prompt)
        self.assertNotIn('Analyst role', prompt)

    def test_missing_cli_is_failure(self):
        with patch.object(agent.shutil, 'which', return_value=None):
            self.assertEqual(self.invoke(), 2)

if __name__ == '__main__':
    unittest.main()
