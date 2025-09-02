from models.service import Service
from models.filecsv import FileCSV
serv = Service("MyService")
filcsv = FileCSV("/home/matheus/Documentos/python/visby/data/tasks.csv")
filcsv.write_csv([[f"{serv.name}"], [f"{serv.description}"]])
