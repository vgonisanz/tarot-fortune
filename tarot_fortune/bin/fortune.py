import typer
from tarot_fortune.picker import TarotCardPicker


app = typer.Typer()


@app.command()
def single(cards_path: str = "tarot_fortune/data/es/cards.json", card_type: str = ""):
    tarot_picker = TarotCardPicker(cards_path)
    title, card, meaning = tarot_picker.pick_a_card(card_type)
    tarot_picker.print_result(title, card, meaning)


@app.command()
def draw_past_present_future(cards_path: str = "tarot_fortune/data/es/cards.json", card_type: str = ""):
    tarot_picker = TarotCardPicker(cards_path)
    title, card, meaning = tarot_picker.draw_past_present_future(card_type)
    tarot_picker.print_result(title, card, meaning)


@app.command()
def draw_circle_for_depth(cards_path: str = "tarot_fortune/data/es/cards.json",
                          card_type: str = "", num_cards: int = 5):
    tarot_picker = TarotCardPicker(cards_path)
    title, card, meaning = tarot_picker.draw_circle_for_depth(card_type, num_cards)
    tarot_picker.print_result(title, card, meaning)


if __name__ == "__main__":
    app()
