from tarot_fortune.picker import TarotCardPicker
from tarot_fortune.utils import get_default_resources_path


class Psychic:
    def __init__(self, cards_path=get_default_resources_path()):
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
        print("Bienvenido a la lectura de tarot del Psychic")
        print("Yo soy la pitonisa y soy capaz de hacer contacto con fuentes del más allá.")
        print("Mi trabajo consiste en hacer predicciones y ayudar a mis clientes a entender sus destinos.")
        print("Elige la opción que quieras:")
        print("1: Lista de cartas de mi mazo del tarot.")
        print("2: Adivinación de la cruz celta.")
        print("3: Adivinación del círculo.")
        print("4: Adivinación del cuerpo humano.")
        print("5: Adivinación del árbol de la vida.")
        print("6: Adivinación del pasado, presente y futuro.")
        print("7: Adivinación simple, una carta, un destino.")
        print("8: No creo en estas cosas, mejor me marcho de aquí.")
        prediction_type = int(input("Elige una de las opciones: "))
        while prediction_type not in self.predictions:
            print("La elección que has hecho es inválida. Prueba otra vez.")
            prediction_type = input("Elige una de las opciones: ")
        if prediction_type == 1:
            card_list = self.predictions[prediction_type]()
            self.tarot_picker.print_card_list(card_list, simple_view=False)
        else:
            title, cards, meanings = self.predictions[prediction_type]()
            self.tarot_picker.print_result(title, cards, meanings)

    def abort_prediction():
        return True