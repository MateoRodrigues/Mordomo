from repository.filecsv import FileCSV

class GetCSV:
    def __init__(self):
        self.filcsv = FileCSV()
        self.tchaves = tuple()
        self.data = []

    def get_data(self):
        # data é uma lista de dicionários
        self.data = self.filcsv.read_csv()
        return self.data
    def get_chaves(self):
        chaves = self.filcsv.get_chaves()
        for c in chaves:
            # nome das colunas do csv em uma tupla
            self.tchaves += (c,)
        return self.tchaves


        