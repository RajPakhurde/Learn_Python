from pathlib import Path

path = Path("modules")

for file in path.glob("*.py"):
    print(file)
