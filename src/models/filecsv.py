import csv

class FileCSV:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_csv(self):
        with open(self.filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data

    def write_csv(self, data):
        with open(self.filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data)