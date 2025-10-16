import tkinter as tk
import tkinter.ttk as ttk
from controllers.getcsv import GetCSV

class ReadCSVView(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Leitor de CSV")
        self.geometry("900x400")
        self.getcsv = GetCSV()
        self.data:list[dict] = self.getcsv.get_data()
        self.colunas:tuple = self.getcsv.get_chaves()
        self.tabela = ttk.Treeview(self)
        self.tabela["columns"] = self.colunas
        # Configurando os cabeçalhos das colunas
        for coluna, nome_coluna in enumerate(self.colunas):
            self.tabela.heading(f"#{coluna+1}", text=nome_coluna, anchor=tk.W)
        # Configurando a largura das colunas
        self.tabela.column("#0", width=0, stretch=tk.NO)
        self.tabela.column("#1", anchor=tk.W, width=120)
        self.tabela.column("#2", anchor=tk.W, width=120)
        self.tabela.column("#3", anchor=tk.W, width=120)
        self.tabela.column("#4", anchor=tk.W, width=120)
        self.dados = self.getcsv.get_tdata()
        for pessoa in self.dados:
            self.tabela.insert("", "end", values=pessoa)
        self.tabela.pack()


