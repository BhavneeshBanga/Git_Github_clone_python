import click
from pathlib import Path
from colorama import Fore, Style, init
init(autoreset=True)

class TextColor:
    RED = "\033[31m"
    RESET = "\033[0m"

def load_ignore_patterns():

    ignore_file = Path(".bhavignore")

    if not ignore_file.exists():
        return []

    patterns = []

    with open(ignore_file, "r") as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            patterns.append(line)

    return patterns


def should_ignore(filepath):

    patterns = load_ignore_patterns()
    patterns.append(".bhav")
    for part in filepath.parts:

        if part in patterns:
            return True

    return False


@click.command()
def status():

    untracked = []
    modified = []

    for file in Path(".").rglob("*"):
        # print(file)

        # folders skip
        if not file.is_file():
            continue

        # .bhav ignore
        if ".bhav" in file.parts:
            continue

        # .bhavignore rules
        if should_ignore(file):
            continue

        staged_file = Path(".bhav/staging") / file

        # file never added
        if not staged_file.exists():
            untracked.append(str(file))
            continue

        try:
            working_content = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            staged_content = staged_file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            if working_content != staged_content:
                modified.append(str(file))

        except Exception:
            pass

    print("\n=== STATUS ===\n")

    if not untracked and not modified:
        print("Working tree clean nothing to commit")
        return

    if untracked:
        print(f"{TextColor.RED}Untracked files{TextColor.RESET}")
        # print("    (use "bhav add <file>..." to update what will be committed)")
        print("  (use \"bhav add <file>...\" to include what will be committed)")
        for file in untracked:
            print(Fore.RED + f"    {file}")

    print()

    if modified:
        print(f"{TextColor.RED}Modified Files{TextColor.RESET}")
        for file in modified:
            print(Fore.RED + f"Modified:    {file}")