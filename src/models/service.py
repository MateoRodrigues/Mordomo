from dataclasses import dataclass
from datetime import date

@dataclass
class Service:
    name: str
    description: str = "No description provided"
    day_number: date = date.today()
    client: str = "No client assigned"
