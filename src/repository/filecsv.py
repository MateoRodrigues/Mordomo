import csv
from pathlib import Path

class FileCSV:
   
    def __init__(self, filepath=Path(__file__).parent.parent.parent/'data'/'service.csv'):
        self.filepath = filepath

    def read_csv(self):
        with open(self.filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data



    def write_csv(self, data):
        with open(self.filepath, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer
            writer.writerow(data)
    
    def get_chaves(self):
        with open(self.filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            chaves = reader.fieldnames
        return chaves
        
