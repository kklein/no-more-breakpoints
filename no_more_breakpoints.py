import click
from pathlib import Path
import subprocess


@click.group()
def cli():
    pass


def validate_file(file: Path) -> None:
    res = subprocess.run(["rg", r"breakpoint\(\)", file], capture_output=True)
    if res.stdout:
        raise ValueError(f"Found at least one breakpoint in {file}.")


@cli.command("validate")
@click.argument(
    "csv_paths", type=click.Path(exists=True, file_okay=True, dir_okay=False), nargs=-1
)
def validate(csv_paths):
    for csv_path in csv_paths:
        path = Path(csv_path)
        validate_file(path)
