"""
Visualize a card
"""
import os
import typer


from term_image.image import from_file


from tarot_fortune.utils import setup_logger


def main(image: str, width: int = 120, height: int = 90):
    typer.echo(f"Running {__file__}")
    if not os.path.isfile(image):
        typer.echo(f"Image {image} do not exist")
        typer.Exit(-1)

    image = from_file(image)
    image.draw()                                  


if __name__ == "__main__":
    setup_logger()
    typer.run(main)
