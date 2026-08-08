APP_NAME = "BylickiLabs Python Reverse Engineering Inspector"
APP_SHORT_NAME = "BPREI"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Thorsten Bylicki / BylickiLabs"

GITHUB_URL = "https://github.com/bylickilabs"
LINKEDIN_URL = "https://www.linkedin.com/in/bylicki/"
FACEBOOK_URL = "https://www.facebook.com/BylickiLabs"

DB_FILENAME = "bprei_history.sqlite3"

EXCLUDED_DIRS = {
    ".git", ".hg", ".svn", ".idea", ".vs", ".vscode",
    "__pycache__", ".pytest_cache", ".mypy_cache",
    ".venv", "venv", "env", "node_modules",
    "build", "dist", ".tox"
}