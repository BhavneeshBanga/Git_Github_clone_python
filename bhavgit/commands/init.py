import click
from pathlib import Path
import json

@click.command()
def init():

    bhav_dir = Path(".bhav")

    if bhav_dir.exists():
        click.echo("Repository already initialized.")
        return
    (bhav_dir / "commits").mkdir(parents=True)
    (bhav_dir / "objects").mkdir(parents=True)
    (bhav_dir / "staging").mkdir(parents=True)

    config = {
        "version": "0.1",
        "branch": "main"
    }

    with open(bhav_dir / "config.json", "w") as f:
        json.dump(config, f, indent=4)

    click.echo("Hello Bhavneesh 🚀")
    click.echo("Bhav Repository Initialized")
