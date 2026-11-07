"""Run from the repository root: python src/check_environment.py."""

from pathlib import Path
import sys


def main():
    version_ok = sys.version_info >= (3, 10)
    print(f"Python: {sys.version.split()[0]}")
    print(f"Python >= 3.10: {'PASS' if version_ok else 'FAIL'}")

    required = [
        Path("team.md"),
        Path("2021245017_공지혁.md"),
        Path(".gitignore"),
        Path("src"),
        Path("week1") / "README.md",
        Path("week1") / "src",
        Path("week1") / "reports" / "figures",
    ]
    missing = [path for path in required if not path.exists()]
    for path in missing:
        print(f"MISSING: {path}")
    print(f"Week 1 structure: {'FAIL' if missing else 'PASS'}")
    print("GitHub upload and Arduino IDE must be checked separately.")
    return 0 if version_ok and not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
