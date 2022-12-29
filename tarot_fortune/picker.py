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

    def __pick_a_card(self, card_type: str):
        if card_type:
                cards_filtered = [card for card in self.__cards if card["type"] == card_type]
                card = random.choice(cards_filtered)
        else:
            card = random.choice(self.__cards)
        meaning = random.choice(["up", "down"])
        return card, meaning

    def __pick_n_cards(self, card_type: str, num_cards: int):
        cards = []
        meanings = []

        for _ in range(3):
            card, meaning = self.__pick_a_card(card_type)
            cards.append(card)
            meanings.append(meaning)
        return cards, meanings
        
    def simple_spread(self, card_type: str = ""):
        """
        Select randomly a card, up or down.
        Return two lists, cards and meanings.
        In this case with one element.
        """
        title = "Tu fortuna simple"
        cards = []
        meanings = []
        
        card, meaning = self.__pick_a_card(card_type)
        cards.append(card)
        meanings.append(meaning)
        return title, cards, meanings

    def past_present_future_spread(self, card_type: str = ""):
        """
        Select randomly 3 cards, up or down.
        Return two lists, cards and meanings.
        Linking the past, the present and the future.
        """
        title = "Reparto del Pasado, presente y futuro"
        cards = []
        meanings = []

        cards, meanings = self.__pick_n_cards(card_type, 3)
        return title, cards, meanings

    def circle_spread(self, card_type: str = "", num_cards: int = 5):
        """
        Select randomly a number of cards between 5 and 8, inclusive.
        Return two lists, cards and meanings.
        """
        title = "Reparto del Círculo, para un tema en profundidad"
        cards = []
        meanings = []

        if num_cards < 5 or num_cards > 8:
            raise ValueError("El número de cartas debe estar entre 5 y 8, incluyendo ambos extremos.")

        cards, meanings = self.__pick_n_cards(card_type, num_cards)
        return title, cards, meanings

    def life_tree_spread(self, card_type: str = "", num_cards: int = 5):
        """
        Select randomly a number of cards between 5 and 10, inclusive.
        Return two lists, cards and meanings.
        """
        title = "Reparto del Árbol de la vida"
        cards = []
        meanings = []

        if num_cards < 5 or num_cards > 10:
            raise ValueError("El número de cartas debe estar entre 5 y 10, incluyendo ambos extremos.")

        cards, meanings = self.__pick_n_cards(card_type, num_cards)
        return title, cards, meanings

    def human_body_spread(self, card_type: str = "", num_cards: int = 5):
        """
        Select randomly a number of cards between 5 and 9, inclusive.
        Return two lists, cards and meanings.
        """
        title = "Reparto del cuerpo humano, para el estado físico y mental"
        cards = []
        meanings = []

        if num_cards < 5 or num_cards > 9:
            raise ValueError("El número de cartas debe estar entre 5 y 9, incluyendo ambos extremos.")

        cards, meanings = self.__pick_n_cards(card_type, num_cards)
        return title, cards, meanings
    
    def celtic_cross_spread(self, card_type: str = "", num_cards: int = 5):
        """
        Select randomly a 5 cards.
        Return two lists, cards and meanings.
        """
        title = "Reparto de la Cruz Celta"
        cards = []
        meanings = []

        if not num_cards == 5:
            raise ValueError("El número de cartas debe ser 5.")

        cards, meanings = self.__pick_n_cards(card_type, num_cards)
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
