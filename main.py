# -*- coding: utf-8 -*-


import csv
import sys
from datetime import datetime


def convert_usd_to_eur(usd_value, exchange_rate=0.85):
    ""schimba dolari in euro."""
    try:
        return round(float(usd_value) * exchange_rate, 2)
    except ValueError:
        return 0


def process_file(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, \
            open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile)
        writer.writerow(['Date', 'Commodity code', 'Commodity', 'Quantity KG', 'Quantity T', 'Value USD', 'Value EUR']
        next(reader) 
        for row in reader:
            if len(row) < 7:
                continue  
            year = row[0]
            month = row[1]
            commodity_code = row[2]
            commodity_description = row[3]
            value_usd = row[5]
            quantity_kg = row[6]
                
            try:
                date = datetime(int(year), int(month), 1).strftime('%Y-%m')
            except ValueError:
                continue 
                
            try:
                quantity_kg = float(quantity_kg.replace(',', ''))
                quantity_t = round(quantity_kg / 1000, 2)
            except ValueError:
                quantity_kg = 0
                quantity_t = 0
                
            value_eur = convert_usd_to_eur(value_usd)

            writer.writerow(
                [date, commodity_code, commodity_description, quantity_kg, quantity_t, value_usd, value_eur])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
