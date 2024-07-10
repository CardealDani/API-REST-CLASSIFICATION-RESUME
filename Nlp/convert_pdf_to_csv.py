import os
import textract
import csv
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

basedirectory = "data/data"
output_csv = "output.csv"
data = []
pdf_id = 1

for subdir, _, files in os.walk(basedirectory):
    class_name = os.path.basename(subdir)

    for filename in files:
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(subdir, filename)
            text = textract.process(pdf_path)
            text = text.decode('utf-8')
            data.append([pdf_id, text, class_name])
            pdf_id += 1
            logging.info(f"Processed PDF: {pdf_path}")

with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "text", "class"])
    writer.writerows(data)
logging.info(f"Data saved to {output_csv}")



