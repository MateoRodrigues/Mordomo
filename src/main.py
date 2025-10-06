import tkinter as tk
import tkinter.ttk as ttk
from controllers.getcsv import GetCSV

gtcsv = GetCSV()

# chaves é uma lista com o nome das colunas
data = gtcsv.get_data()
for p,r in enumerate(data):
    print(f'{r}')
root = tk.Tk()
tabela = ttk.Treeview(root)
tabela["columns"] = gtcsv.get_chaves()
# Configurando os cabeçalhos das colunas
tabela.heading("#0", text="", anchor=tk.W)
tabela.heading("#1", text="Nome", anchor=tk.W)
tabela.heading("#2", text="Data", anchor=tk.W)
tabela.heading("#3", text="Cliente", anchor=tk.W)
tabela.heading("#4", text="Valor", anchor=tk.W)
# Configurando a largura das colunas
tabela.column("#0", width=0, stretch=tk.NO)
tabela.column("#1", anchor=tk.W, width=120)
tabela.column("#2", anchor=tk.W, width=120)
tabela.column("#3", anchor=tk.W, width=120)
tabela.column("#4", anchor=tk.W, width=120)
# Adicionando dados à tabela
dados = [(data[0]['nome'], 28, 45.00, 100), (data[1]['nome'], 35, 40, 100), (data[2]['nome'], 19, 70,200)]
for pessoa in dados:
    tabela.insert("", "end", values=pessoa)

tabela.pack()
root.mainloop()

