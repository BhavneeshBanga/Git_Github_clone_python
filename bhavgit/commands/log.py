import click
from pathlib import Path
import json


@click.command()
def log():

    commits = Path(".bhav/commits")

    if not commits.exists():
        print("No commits found")
        return

    commit_folders = sorted(
        commits.iterdir(),
        reverse=True
    )

    for commit in commit_folders:

        metadata_file = commit / "metadata.json"

        if not metadata_file.exists():
            continue

        with open(metadata_file, "r") as f:
            metadata = json.load(f)

        print(f"\n{commit.name}")
        print(f"Message: {metadata['message']}")