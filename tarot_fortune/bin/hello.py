"""
Hello
"""
import typer

from tarot_fortune.utils import setup_logger


def main():
    typer.echo(f"Running {__file__}")


if __name__ == "__main__":
    setup_logger()
    typer.run(main)
