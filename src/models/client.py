from dataclasses import dataclass
from pathlib import Path

@dataclass
class Client:
    name: str
    email: str
    phone: str
    address: str = "No address provided"
    table: Path = Path(__file__).parent.parent.parent/'data'/'client.csv'