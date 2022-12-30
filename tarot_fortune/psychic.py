from rich.console import Console
from rich.table import Table


from tarot_fortune.picker import TarotCardPicker
from tarot_fortune.utils import get_cards_json
from tarot_fortune.renderer import Renderer


class Psychic:
    def __init__(self, cards_path=get_cards_json('es'), name: str = 'Zahara la Sabia'):
        self.__name = name
        self.__console = Console()
        self.__tarot_picker = TarotCardPicker(cards_path=cards_path)
        self.__predictions = {
            1: self.__tarot_picker.simple_spread,
            2: self.__tarot_picker.past_present_future_spread,
            3: self.__tarot_picker.circle_spread,
            4: self.__tarot_picker.human_body_spread,
            5: self.__tarot_picker.life_tree_spread,
            6: self.__tarot_picker.celtic_cross_spread,
            7: self.__tarot_picker.get_card_list,
            8: self.__tarot_picker.get_card_by_title,
            9: self.__bye
        }
    
    def __bye(self):
        self.__console.print(f"¿No confías en {self.__name}? Pues ahí tienes la puerta", style="bold red")
        exit(0)

    def __print_main_menu(self):
        self.__console.print(f"Bienvenido a la lectura de tarot de {self.__name}", style="bold red")
        self.__console.print("Yo soy la pitonisa y soy capaz de hacer contacto con fuentes del más allá.")
        self.__console.print("Mi trabajo consiste en hacer predicciones y ayudar a mis clientes a entender sus destinos.")

        self.__console.print("Elige la opción que quieras:")

        table = Table(title="Opciones de predicción")
        table.add_column("Opción")
        table.add_column("Descripción")
        table.add_row("1", "Adivinación simple, una carta, un destino.")
        table.add_row("2", "Adivinación del pasado, presente y futuro.")
        table.add_row("3", "Adivinación del círculo.")
        table.add_row("4", "Adivinación del cuerpo humano.")
        table.add_row("5", "Adivinación del árbol de la vida.")
        table.add_row("6", "Adivinación de la cruz celta.")
        table.add_row("7", "Lista de cartas de mi mazo del tarot.")
        table.add_row("8", "Enseñame la carta que te pida.")
        table.add_row("9", "No creo en estas cosas, mejor me marcho de aquí.")
        self.__console.print(table)

    def make_prediction(self):
        self.__print_main_menu()
        prediction_type = int(input("Elige una de las opciones: "))
        while prediction_type not in self.__predictions:
            self.__console.print("La elección que has hecho es inválida. Prueba otra vez.")
            prediction_type = self.__console.print("Elige una de las opciones: ")
        if prediction_type == 7:
            card_list = self.__predictions[prediction_type]()
            Renderer.print_card_list(card_list, simple_view=False)
        elif prediction_type == 8:
            choosen_card = input("Dime la carta que quieres dandome su nombre: ")
            found = False
            for card in self.__tarot_picker.get_card_list():
                if card.title == choosen_card:
                    Renderer.print_card_list([card], simple_view=False)
                    found = True 
            if not found:
                self.__console.print("Ese ID de carta no existe")
        else:
            title, cards = self.__predictions[prediction_type]()
            Renderer.print_result(title, cards)
