"""Script para convertir un archivo CSV a JSON"""

import csv
import json
import os

def convert_csv_2_json(input_file, output_file=None):
    """Converts a CSV file to a JSON file"""
    
    if output_file is None:
        output_file = input_file.replace(".csv", ".json")
    
    data = []

    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# Si el test importa este archivo, NO debe ejecutar una app ni interface
if __name__ == "__main__":
    # Ejecutar conversión automática para el test
    convert_csv_2_json("files/drivers.csv")

