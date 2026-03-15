from dataclasses import dataclass, field

from typing import Literal


@dataclass
class Task:
    nome: str
    descricao: str
    responsavel: str
    data_inicio: str
    data_final: str

