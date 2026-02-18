from dataclasses import dataclass
from datetime import date
from repository.filecsv import FileCSV


@dataclass
class Service:
    name: str = "Unnamed Service"
    description: str = "No description provided"
    day_number: date = date.today()
    client: str = "No client assigned"
    value: float = 0.0
    def migration(self):
        filcsv = FileCSV()
        filcsv.write_csv(data=[self.name, self.description, self.day_number,self.client, self.value])
        
