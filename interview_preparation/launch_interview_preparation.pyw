"""
launch_interview_preparation.pyw

Launch the Interview Preparation application without a console window.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from interview_preparation.interview_controller import main  # noqa: E402

if __name__ == "__main__":
    main()
