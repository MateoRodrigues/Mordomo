from models.service import Service
from models.filecsv import FileCSV

serv = Service("MyService")
serv.client = "Client A"
filcsv = FileCSV()
filcsv.write_csv([[f"{serv.name}"], [f"{serv.description}"], [f"{serv.day_number}"],[f"{serv.client}"]])

