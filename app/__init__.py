from pathlib import Path
from .version import VERSION, VersionObj

PROJECT_DIR = Path(__file__).resolve().parent.parent
SCRIPT_DIR = PROJECT_DIR / "scripts"
SCRIPT_DIR.mkdir(parents=True, exist_ok=True)