from pathlib import Path
PROJECT_DIR = Path(__file__).resolve().parent.parent
SCRIPT_DIR = PROJECT_DIR / "scripts"
SCRIPT_DIR.mkdir(parents=True, exist_ok=True)