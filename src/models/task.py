from dataclasses import dataclass, field


@dataclass
class Task:
    nome: str
    descricao: str
    responsavel: str
    data_inicio: str
    data_final: str
    status:list = field(default_factory=list, init=False) # pyright: ignore[reportInvalidTypeForm]
    projeto: str
    sessao: str
    colaboradores:list = field(default_factory=list, init=False)
