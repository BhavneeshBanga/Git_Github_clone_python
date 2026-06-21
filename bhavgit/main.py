import click
from pathlib import Path
import json

from bhavgit.commands.init import init
from bhavgit.commands.add import add
from bhavgit.commands.commit import commit
from bhavgit.commands.log import log
from bhavgit.commands.status import status


@click.group()
def main():
    pass

main.add_command(init)
main.add_command(add)
main.add_command(commit)
main.add_command(log)
main.add_command(status)

if __name__ == "__main__":
    main()