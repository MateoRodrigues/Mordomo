from dataclasses import dataclass

@dataclass
class Client:
    name: str
    email: str
    phone: str
    address: str = "No address provided"