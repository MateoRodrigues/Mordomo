from models.service import Service
from models.filecsv import FileCSV
serv = Service("MyService")
filcsv = FileCSV()
filcsv.write_csv([[f"{serv.name}"], [f"{serv.description}"], [f"{serv.day_number}"]])
