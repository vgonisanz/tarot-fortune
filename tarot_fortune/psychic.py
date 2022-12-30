from rich.console import Console
from rich.table import Table


from tarot_fortune.picker import TarotCardPicker
from tarot_fortune.utils import get_cards_json


class Psychic:
    def __init__(self, cards_path=get_cards_json('es'), name: str = 'Zahara la Sabia'):
        self.__name = name
        self.tarot_picker = TarotCardPicker(cards_path=cards_path)
        self.predictions = {
            1: self.tarot_picker.get_card_list,
            2: self.tarot_picker.celtic_cross_spread,
            3: self.tarot_picker.circle_spread,
            4: self.tarot_picker.human_body_spread,
            5: self.tarot_picker.life_tree_spread,
            6: self.tarot_picker.past_present_future_spread,
            7: self.tarot_picker.simple_spread,
            8: exit
        }
    
    def make_prediction(self):
        console = Console()
        console.print(f"Bienvenido a la lectura de tarot de f{self.__name}", style="bold red")
        console.print("Yo soy la pitonisa y soy capaz de hacer contacto con fuentes del más allá.")
        console.print("Mi trabajo consiste en hacer predicciones y ayudar a mis clientes a entender sus destinos.")

        # Opciones de predicción
        console.print("Elige la opción que quieras:")

        table = Table(title="Opciones de predicción")
        table.add_column("Opción")
        table.add_column("Descripción")
        table.add_row("1", "Lista de cartas de mi mazo del tarot.")
        table.add_row("2", "Adivinación de la cruz celta.")
        table.add_row("3", "Adivinación del círculo.")
        table.add_row("4", "Adivinación del cuerpo humano.")
        table.add_row("5", "Adivinación del árbol de la vida.")
        table.add_row("6", "Adivinación del pasado, presente y futuro.")
        table.add_row("7", "Adivinación simple, una carta, un destino.")
        table.add_row("8", "No creo en estas cosas, mejor me marcho de aquí.")
        console.print(table)

        prediction_type = int(input("Elige una de las opciones: "))
        while prediction_type not in self.predictions:
            console.print("La elección que has hecho es inválida. Prueba otra vez.")
            prediction_type = console.print("Elige una de las opciones: ")
        if prediction_type == 1:
            card_list = self.predictions[prediction_type]()
            self.tarot_picker.print_card_list(card_list, simple_view=False)
        else:
            title, cards, meanings = self.predictions[prediction_type]()
            self.tarot_picker.print_result(title, cards, meanings)
