import csv
from pathlib import Path

class FileCSV:
    """ Esta classe é responsável por ler e escrever arquivos CSV.
     EXEMPLO DE USO:
        file_csv = FileCSV()
        data, reader = file_csv.read_csv()
        file_csv.write_csv(['novo', 'registro', 'csv'])"""
   
    def __init__(self, filepath=Path(__file__).parent.parent.parent/'data'/'service.csv'):
        self.filepath = filepath

    def read_csv(self):
        with open(self.filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            #values = [row for row in csv.reader(file)]
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
        
