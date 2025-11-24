import csv
import json
import os

def convert_csv_2_json():
    """Converts files/drivers.csv to files/drivers.json"""

    input_file = "files/drivers.csv"
    output_file = "files/drivers.json"

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"{input_file} not found")

    data = []

    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return output_file


if __name__ == "__main__":
    convert_csv_2_json()

