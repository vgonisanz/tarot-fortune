import json
import random

from rich import print
from rich.table import Table


class TarotCardPicker:
    def __init__(self, cards_path: str = "../data/es/cards.json"):
        self.__cards = self.__load_cards(cards_path)

    def __load_cards(self, cards_path):
        with open(cards_path, "r") as json_file:
            data = json.load(json_file)
            cards = data["cards"]
            return cards

    def choose_card_single(self, card_type: str = ""):
        """
        Select randomly a card, up or down.
        Return two lists, cards and meanings.
        In this case with one element.
        """
        title = "Tu fortuna simple"
        cards = []
        meanings = []
        if card_type:
            cards_filtered = [card for card in self.__cards if card["type"] == card_type]
            cards.append(random.choice(cards_filtered))
        else:
            cards.append(random.choice(self.__cards))
        meanings.append(random.choice(["up", "down"]))
        return title, cards, meanings

    def print_result(self, title, cards, meanings):
        table = Table(title=title)
        table.add_column("Nombre de la carta")
        table.add_column("Sentido")
        table.add_column("Significado")
        for card, meaning in zip(cards, meanings):
            
            if meaning == "up":
                table.add_row(card['title'], "Boca arriba", ", ".join(card['meaning_up']))
            else:
                table.add_row(card['title'], "Boca abajo", ", ".join(card['meaning_down']))
        print()
        print(table)
        print()
