"""Run the repository's local quality checks in the same order as CI."""

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class QualityCheck:
    """A single repository quality check."""

    name: str
    arguments: tuple[str, ...]


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent

QUALITY_CHECKS = (
    QualityCheck("Ruff lint", ("-m", "ruff", "check", ".")),
    QualityCheck("Ruff format", ("-m", "ruff", "format", "--check", ".")),
    QualityCheck("mypy", ("-m", "mypy", ".")),
    QualityCheck("pytest", ("-m", "pytest")),
)


def run_check(check: QualityCheck) -> bool:
    """Run one quality check and report whether it succeeded."""
    print(f"\n=== {check.name} ===")

    result = subprocess.run(
        [sys.executable, *check.arguments],
        cwd=REPOSITORY_ROOT,
        check=False,
    )

    return result.returncode == 0


def main() -> int:
    """Run all configured quality checks, stopping at the first failure."""
    print("Running My Pythonic Zoo quality checks...")

    for check in QUALITY_CHECKS:
        if not run_check(check):
            print(f"\nFAILED: {check.name}")
            return 1

    print("\nAll quality checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
