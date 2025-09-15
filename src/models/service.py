from dataclasses import dataclass

@dataclass
class Service:
    name: str
    description: str = "No description provided"
    day: weekday
