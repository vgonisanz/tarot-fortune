from rich import print
from rich.table import Table


class Renderer:
    @staticmethod
    def print_result(title, cards, print_cards: bool = False):
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
            print("IN PROGRESS")

        print()
        print(table)
        print()

    @staticmethod
    def print_card_list(card_list, simple_view):
        if simple_view:
            print([card.id for card in card_list])
        else:
            table = Table(title="Cartas disponibles", show_header=True, header_style="bold red")
            table.add_column("ID")
            table.add_column("Título")
            table.add_column("Tipo")
            for card in card_list:
                table.add_row(card.id, card.title, card.type)
            
            print()
            print(table)
            print()
