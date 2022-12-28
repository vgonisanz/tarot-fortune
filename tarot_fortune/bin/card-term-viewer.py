"""
Visualize a card
"""
import os
import typer
from imgrender import render

from tarot_fortune.utils import setup_logger


def main(image: str, width: int = 120, height: int = 90):
    typer.echo(f"Running {__file__}")
    if not os.path.isfile(image):
        typer.echo(f"Image {image} do not exist")
        typer.Exit(-1)
                                                                                    
    render(image, scale=(width, height))


if __name__ == "__main__":
    setup_logger()
    typer.run(main)
