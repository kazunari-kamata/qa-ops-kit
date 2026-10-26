from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, *args], cwd=ROOT, text=True, capture_output=True, check=False)
def test_checklist() -> None:
    result = run("scripts/generate_qa_checklist.py", "test-execution")
    assert result.returncode == 0 and "障害" in result.stdout
def test_invalid_phase() -> None:
    assert run("scripts/generate_qa_checklist.py", "unknown").returncode != 0
def test_templates() -> None:
    result = run("scripts/validate_templates.py", "templates")
    assert result.returncode == 0 and "validated" in result.stdout
