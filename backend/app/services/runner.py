import sys
import subprocess
import tempfile
import os
from typing import Dict, Any

class CodeRunner:
    @staticmethod
    def execute_code(code: str, test_assertions: str = "", timeout_sec: int = 5) -> Dict[str, Any]:
        """
        Executes Python code in an isolated subprocess with timeout protection.
        """
        full_script = f"""
import sys

# User Code Submission
{code}

# Test Harness & Verification
{test_assertions}
print("\\n[SUCCESS] All verification tests passed successfully!")
"""

        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write(full_script)
            temp_path = f.name

        try:
            result = subprocess.run(
                [sys.executable, temp_path],
                capture_output=True,
                text=True,
                timeout=timeout_sec
            )
            
            passed = result.returncode == 0
            return {
                "status": "passed" if passed else "failed",
                "score": 100 if passed else 0,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "exit_code": result.returncode
            }

        except subprocess.TimeoutExpired:
            return {
                "status": "timeout",
                "score": 0,
                "stdout": "",
                "stderr": f"Execution exceeded safety limit of {timeout_sec} seconds (Infinite loop or slow I/O detected).",
                "exit_code": -1
            }
        except Exception as e:
            return {
                "status": "error",
                "score": 0,
                "stdout": "",
                "stderr": str(e),
                "exit_code": -1
            }
        finally:
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except Exception:
                    pass

code_runner = CodeRunner()
