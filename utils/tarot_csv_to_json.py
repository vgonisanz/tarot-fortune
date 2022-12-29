import csv
import json
import typer

app = typer.Typer()

@app.command()
def convert(
    csv_path: str = typer.Argument(..., help="Path of the CSV file to process"),
    json_path: str = typer.Argument(..., help="Path of the destination JSON file")
):
    """
    Convert the csv from resources with all the data to json file.

    Example: python tarot_csv_to_json.py <path of the CSV file> <path of the JSON file>
    """
    with open(csv_path, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        col_names = next(csv_reader)

        tarot_cards = dict()
        tarot_cards['cards'] = []

        for row in csv_reader:
            tarot_card = {
                f"{col_names[0]}": row[0],
                f"{col_names[1]}": row[1],
                f"{col_names[2]}": row[2],
                f"{col_names[3]}": row[3],
                f"{col_names[4]}": [word.capitalize() for word in row[4].split(";")],
                f"{col_names[5]}": [word.capitalize() for word in row[5].split(";")]
            }
            tarot_cards['cards'].append(tarot_card)

    with open(json_path, 'w') as json_file:
        json.dump(tarot_cards, json_file, indent=4, separators=(',', ': '), ensure_ascii=False)


if __name__ == "__main__":
  app()
