from rich.table import Table
from rich import print
from repository.filecsv import FileCSV

chaves = FileCSV().get_chaves()
cores = ["cyan", "magenta", "green", "yellow", "blue"]
data = FileCSV().read_csv()
tabela = Table(title="Serviços Cadastrados")
for chave, cor in zip(chaves, cores):
    tabela.add_column(chave, justify="center", style=cor)
for d in data:
    tabela.add_row(d['nome'], d['descricao'], d['data_do_serviço'], d['cliente'], d['valor'])
print(tabela)



