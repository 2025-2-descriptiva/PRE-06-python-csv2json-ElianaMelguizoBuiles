import csv
import json
import os

def convert_csv_2_json(input_file, output_file):
    """Converts CSV to JSON without GUI"""

    data = []

    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# AUTOGENERA drivers.json AUTOMÁTICAMENTE
def main():
    input_path = "files/drivers.csv"
    output_path = "files/drivers.json"

    if not os.path.exists(output_path):
        convert_csv_2_json(input_path, output_path)


if __name__ == "__main__":
    main()

