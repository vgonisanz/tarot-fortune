import json
import random


from tarot_fortune.utils import get_cards_json
from tarot_fortune.entities import TarotCard


class TarotCardPicker:
    def __init__(self, cards_path: str = get_cards_json('es')):
        self.__cards = self.__load_cards(cards_path)

    def __load_cards(self, cards_path):
        with open(cards_path, "r") as json_file:
            cards = []
            data = json.load(json_file)
            for card_data in data['cards']:
                cards.append(TarotCard(**card_data))
            return cards

    def __pick_a_card(self, card_type: str):
        if card_type:
                cards_filtered = [card for card in self.__cards if card['type'] == card_type]
                card = random.choice(cards_filtered)
        else:
            card = random.choice(self.__cards).copy()
        card.orientation = random.choice(['up', 'down'])
        return card

    def __pick_n_cards(self, card_type: str, num_cards: int):
        cards = []

        for _ in range(num_cards):
            cards.append(self.__pick_a_card(card_type))

        return cards
    
    def get_card_list(self):
        """
        Return a list with the card id and title.
        """
        return self.__cards

    def get_card_by_title(self, title: str, orientation: str = 'up'):
        for card in self.__cards:
            if card.title == title:
                new_card = TarotCard(**card.dict())
                new_card.orientation = orientation
                return new_card
        return None

    def simple_spread(self, card_type: str = ""):
        """
        Spread with a single card.
        
        Select randomly a card, up or down.
        Returns a list of cards and a title
        """
        title = "Tu fortuna simple"
        cards = []
    
        cards.append(self.__pick_a_card(card_type))
        return title, cards

    def past_present_future_spread(self, card_type: str = ""):
        """
        Spread with multiple cards.
        
        Linking the past, the present and the future.
        Select randomly 3 cards, up or down.
        
        Returns a list of cards and a title
        """
        title = "Reparto del Pasado, presente y futuro"
        cards = []

        cards = self.__pick_n_cards(card_type, 3)
        return title, cards

    def circle_spread(self, card_type: str = "", num_cards: int = 5):
        """
        Spread with multiple cards.
    
        Select randomly a number of cards between 5 and 8, inclusive.
        Returns a list of cards and a title
        """
        title = "Reparto del Círculo, para un tema en profundidad"
        cards = []

        if num_cards < 5 or num_cards > 8:
            raise ValueError("El número de cartas debe estar entre 5 y 8, incluyendo ambos extremos.")

        cards = self.__pick_n_cards(card_type, num_cards)
        return title, cards

    def life_tree_spread(self, card_type: str = "", num_cards: int = 5):
        """
        Spread with multiple cards.

        Select randomly a number of cards between 5 and 10, inclusive.
        Returns a list of cards and a title
        """
        title = "Reparto del Árbol de la vida"
        cards = []

        if num_cards < 5 or num_cards > 10:
            raise ValueError("El número de cartas debe estar entre 5 y 10, incluyendo ambos extremos.")

        cards = self.__pick_n_cards(card_type, num_cards)
        return title, cards

    def human_body_spread(self, card_type: str = "", num_cards: int = 5):
        """
        Select randomly a number of cards between 5 and 9, inclusive.
        Returns a list of cards and a title
        """
        title = "Reparto del cuerpo humano, para el estado físico y mental"
        cards = []

        if num_cards < 5 or num_cards > 9:
            raise ValueError("El número de cartas debe estar entre 5 y 9, incluyendo ambos extremos.")

        cards = self.__pick_n_cards(card_type, num_cards)
        return title, cards
    
    def celtic_cross_spread(self, card_type: str = "", num_cards: int = 5):
        """
        Select randomly a 5 cards.
        Returns a list of cards and a title
        """
        title = "Reparto de la Cruz Celta"
        cards = []

        if not num_cards == 5:
            raise ValueError("El número de cartas debe ser 5.")

        cards = self.__pick_n_cards(card_type, num_cards)
        return title, cards
