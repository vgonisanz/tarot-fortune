import typer
import json
import random


def load_cards(path: str):
    with open(path, "r") as json_file:
        data = json.load(json_file)
        cards = data["cards"]
        return cards


def choose_card_single(cards):
    card = random.choice(cards)
    meaning = random.choice(["up", "down"])
    return card, meaning


def print_result(card, meaning):
    typer.echo(f"La carta elegida es: {card['title']}")
    typer.echo(f"Descripción: {card['description']}")
    if meaning == "up":
        typer.echo("La carta ha salido para arriba")
        typer.echo(f"Significado de la carta: {', '.join(card['meaning_up'])}")
    else:
        typer.echo("La carta ha salido para abajo")
        typer.echo(f"Significado de la carta: {', '.join(card['meaning_down'])}")


def main(cards_path: str = "../data/es/cards.json", card_type: str = ""):
    typer.echo("Elegiendo una carta al azar...")
    
    cards = load_cards(cards_path)

    if card_type:
        cards_filtered = [card for card in cards if card["type"] == card_type]
        card, meaning = choose_card_single(cards_filtered)
    else:
        card, meaning = choose_card_single(cards)
    
    print_result(card, meaning)


if __name__ == "__main__":
    typer.run(main)
