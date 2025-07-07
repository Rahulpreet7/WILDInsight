import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

SUBDIRS = [
    "data/raw",
    "data/processed",
    "etl",
    "analysis",
    "visualizations/tableau",
    "database",
    "utils",
    "tests",
    ".github/workflows"
    ]

FILES = {
    "README.md": "# WildNorth Insight Platform\n\nThis project extracts actionable insights from wildlife intake data.",
    "requirements.txt": "pandas\njupyter\nmatplotlib\nseaborn\n"
}

# Create directories
for subdir in SUBDIRS:
    os.makedirs(os.path.join(PROJECT_DIR, subdir), exist_ok=True)

# Create files with default content
for filename, content in FILES.items():
    path = os.path.join(PROJECT_DIR, filename)
    with open(path, "w") as f:
        f.write(content)

print(f"Project structure created in ./{PROJECT_DIR}")