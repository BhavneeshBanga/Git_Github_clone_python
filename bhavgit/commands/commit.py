import click
from pathlib import Path
import json
import shutil
from datetime import datetime


@click.command()
@click.option(
    "-b",
    "--message",
    required=True
)
def commit(message):

    print("commit msg : ", message)
    staging = Path(".bhav/staging")
    if not staging.exists():
        print("Nothing to commit")
        return

    commits = Path(".bhav/commits")

    commit_id = len(list(commits.iterdir())) + 1

    commit_folder = commits / f"commit_{commit_id}"

    shutil.copytree(
        staging,
        commit_folder
    )
    metadata = {
        "message": message,
        "timestamp" : str(datetime.now())
    }

    with open(commit_folder / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)
