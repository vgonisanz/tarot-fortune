import typer
from tarot_fortune.picker import TarotCardPicker


app = typer.Typer()


@app.command()
def single(cards_path: str = "tarot_fortune/data/es/cards.json", card_type: str = ""):
    tarot_picker = TarotCardPicker(cards_path)
    title, card, meaning = tarot_picker.choose_card_single(card_type)
    tarot_picker.print_result(title, card, meaning)


if __name__ == "__main__":
    app()
