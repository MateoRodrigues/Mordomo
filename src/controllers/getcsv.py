from ..repository.filecsv import FileCSV

class GetCSV:
    def __init__(self):
        self.filcsv = FileCSV()
        self.tchaves = tuple()
        self.data = []

    def get_data(self):
        self.data = self.filcsv.read_csv()

        