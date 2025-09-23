from models.service import Service
from models.filecsv import FileCSV
from datetime import date

serv = Service(str(input("Nome: ")))
serv.description = str(input("Descrição: "))
serv.client = str(input("Cliente: "))
serv.value = float(input("Valor:R$"))
serv.migration()

