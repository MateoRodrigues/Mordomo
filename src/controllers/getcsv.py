from repository.filecsv import FileCSV
from pathlib import Path

class GetCSV:
    def __init__(self):
        self.filcsv = FileCSV()
        self.tchaves = tuple()
        self.data = self.filcsv.read_csv()

    def get_data(self):
        # data é uma lista de dicionários
        return self.data
    def get_chaves(self):
        chaves = self.filcsv.get_chaves()
        for c in chaves:
            # nome das colunas do csv em uma tupla
            self.tchaves += (c,)
        return self.tchaves
    def get_tdata(self):
        # tdata é uma lista de tuplas
        self.tdata = list()
        self.titem = tuple()
        for pos, service in enumerate(self.data):
            for value in service.values():
                last_item = list(service.values())[-1]
                self.titem += (value,)
                if (value) == last_item:
                    self.tdata.append(self.titem)
                    self.titem = tuple()
        return self.tdata
        


        