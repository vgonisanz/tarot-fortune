import typer

from tarot_fortune.picker import TarotCardPicker
from tarot_fortune.psychic import Psychic
from tarot_fortune.utils import get_cards_json


app = typer.Typer(help="Tarot fortune-telling application")


@app.command()
def single(cards_path: str = get_cards_json('es'), card_type: str = ""):
    """
    Single card draw
    
    This is a very simple spread that consists of drawing a single card from the deck
    and reading it as a response to a question or as a reflection on the day.
    """
    tarot_picker = TarotCardPicker(cards_path)
    title, card, meaning = tarot_picker.simple_spread(card_type)
    tarot_picker.print_result(title, card, meaning)


@app.command()
def past_present_future(cards_path: str = get_cards_json('es'), card_type: str = ""):
    """
    Past, present, and future spread
    
    This spread is used to explore how a situation has evolved in the past,
    how it is influencing the present,
    and how it may influence the future.
    Three cards are drawn from the deck and placed in a row,
    representing the past, present, and future.
    """
    tarot_picker = TarotCardPicker(cards_path)
    title, card, meaning = tarot_picker.past_present_future_spread(card_type)
    tarot_picker.print_result(title, card, meaning)


@app.command()
def circle(cards_path: str = get_cards_json('es'),
                          card_type: str = "", num_cards: int = 6):
    """
    Circle spread
    
    This spread is used to explore a topic or question in depth.
    Several cards are drawn from the deck and placed in a circle
    around the question or topic being explored.
    """
    tarot_picker = TarotCardPicker(cards_path)
    title, card, meaning = tarot_picker.circle_spread(card_type, num_cards)
    tarot_picker.print_result(title, card, meaning)


@app.command()
def life_tree(cards_path: str = get_cards_json('es'),
                          card_type: str = "", num_cards: int = 7):
    """
    Tarot spread for the tree of life
    
    This spread is used to explore a person's life path
    and how it relates to the different aspects of existence.
    Several cards are drawn from the deck and placed in a shape that simulates a tree,
    representing different aspects of life.
    """
    tarot_picker = TarotCardPicker(cards_path)
    title, card, meaning = tarot_picker.life_tree_spread(card_type, num_cards)
    tarot_picker.print_result(title, card, meaning)


@app.command()
def human_body(cards_path: str = get_cards_json('es'),
                    card_type: str = "", num_cards: int = 5):
    """
    Tarot spread for the human body
    
    This spread is used to explore how different aspects of life are affecting a person physically and emotionally.
    Several cards are drawn from the tarot deck and placed in a shape that simulates a human body,
    representing different aspects of health and well-being.
    """
    tarot_picker = TarotCardPicker(cards_path)
    title, card, meaning = tarot_picker.human_body_spread(card_type, num_cards)
    tarot_picker.print_result(title, card, meaning)


@app.command()
def celtic_cross(cards_path: str = get_cards_json('es'),
                 card_type: str = ""):
    """
    The Celtic Cross spread
    
    This spread is used to explore a particular theme,
    see how different aspects of a person's life are interconnected
    and how they may affect the present and future.
    The Celtic Cross consists of five cards placed in a cross-like shape,
    representing different aspects of life such as the past, present, future, inner self, and outer self.
    By interpreting each card in relation to these aspects,
    a more comprehensive and deep understanding of the situation
    or question being explored can be obtained.
    """
    tarot_picker = TarotCardPicker(cards_path)
    title, card, meaning = tarot_picker.celtic_cross_spread(card_type, 5)
    tarot_picker.print_result(title, card, meaning)


@app.command()
def cards(cards_path: str = get_cards_json('es'), simple_view: bool = False):
    """
    List loaded cards

    Show all available cards in the loaded deck in a table or simple list form.
    If simple_view is True, only print the values.
    If simple_view is False, print a table.
    """
    tarot_picker = TarotCardPicker(cards_path)
    card_list = tarot_picker.get_card_list()
    tarot_picker.print_card_list(card_list, simple_view)


@app.command()
def psychic(cards_path: str = get_cards_json('es')):
    """
    The psychic will take care of your divination.
    All you have to do is interact with her.
    """
    psychic = Psychic()
    psychic.make_prediction()
          

if __name__ == "__main__":
    app()
