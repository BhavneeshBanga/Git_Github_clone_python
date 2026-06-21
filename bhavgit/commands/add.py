import click
from pathlib import Path
import shutil

def add_file(filepath):
    source = Path(filepath)

    if(not source.exists()):
        print("file doesn't exist")
        return 

    if(not source.is_file()):
        return    

    staging_root = Path(".bhav/staging")

    destination = staging_root / source

    destination.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    shutil.copy2(source, destination)

    print(f"Added: {filepath}")   #target === filepath


def add_all_files():

    for file in Path(".").rglob("*"):

        # .bhav folder
        if ".bhav" in file.parts:
            continue

        # ignore folders
        if not file.is_file():
            continue

        add_file(file)



@click.command()
@click.argument("target")
def add(target):
    
    if(target=="."):
        add_all_files()
    else:
        add_file(target)


