import os
import subprocess
import sys

import pytest

SCRIPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'source', 'data_playing')
SCRIPTS = sorted(name for name in os.listdir(SCRIPTS_DIR) if name.endswith('.py') and name != '__init__.py')


@pytest.mark.parametrize('script', SCRIPTS)
def test_script_runs_from_any_directory(script, tmp_path):
    result = subprocess.run([sys.executable, os.path.join(SCRIPTS_DIR, script)],
                            cwd=tmp_path, capture_output=True, text=True, timeout=120)
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip()
