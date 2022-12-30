from rich import print
from rich.table import Table
from term_image.image import from_file

from tarot_fortune.utils import get_card_path


class Renderer:
    @staticmethod
    def print_result(title, cards, print_cards: bool = True):
        table = Table(title=title)
        table.add_column("Nombre de la carta")
        table.add_column("Sentido")
        table.add_column("Significado")
        for card in cards:
            if card.orientation == "up":
                table.add_row(card.title, "Boca arriba", ", ".join(card.meaning_up))
            else:
                table.add_row(card.title, "Boca abajo", ", ".join(card.meaning_down))
        
        if print_cards:
            for card in cards:
                image = get_card_path(card.id)
                from_file(image).draw()

        print()
        print(table)
        print()

    @staticmethod
    def print_card_list(card_list, simple_view):
        if simple_view:
            print([card.id for card in card_list])
        else:
            table = Table(title="Cartas disponibles", show_header=True, header_style="bold red")
            table.add_column("ID de la carta")
            table.add_column("Nombre de la carta")
            table.add_column("Tipo")
            for card in card_list:
                table.add_row(card.id, card.title, card.type)
            
            print()
            print(table)
            print()
