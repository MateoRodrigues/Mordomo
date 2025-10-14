import tkinter as tk
import tkinter.ttk as ttk
from controllers.getcsv import GetCSV

class ReadCSVView(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Leitor de CSV")
        self.geometry("600x400")
        self.data = GetCSV().get_data()
        self.tabela = ttk.Treeview(self)
        self.tabela["columns"] = GetCSV().get_chaves()
        # Configurando os cabeçalhos das colunas
        self.tabela.heading("#0", text="", anchor=tk.W)
        self.tabela.heading("#1", text="Nome", anchor=tk.W)
        self.tabela.heading("#2", text="Data", anchor=tk.W)
        self.tabela.heading("#3", text="Cliente", anchor=tk.W)
        self.tabela.heading("#4", text="Valor", anchor=tk.W)
        # Configurando a largura das colunas
        self.tabela.column("#0", width=0, stretch=tk.NO)
        self.tabela.column("#1", anchor=tk.W, width=120)
        self.tabela.column("#2", anchor=tk.W, width=120)
        self.tabela.column("#3", anchor=tk.W, width=120)
        self.tabela.column("#4", anchor=tk.W, width=120)
        self.dados = [(self.data[0]['nome'], 28, 45.00, 100), (self.data[1]['nome'], 35, 40, 100), (self.data[2]['nome'], 19, 70,200)]
        for pessoa in self.dados:
            self.tabela.insert("", "end", values=pessoa)
        self.tabela.pack()

