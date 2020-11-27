from tkinter import *
from tkinter.ttk import *






class RelatorioProdutos():
    def __init__(self, master=None):
        self.container1 = Frame(master, width=320)
        self.container1.grid(row=0, column=0)

        self.container2 = Frame(master, width=320)
        self.container2.grid(row=1, column=0)

        self.container3 = Frame(master, width=320)
        self.container3.grid(row=1, column=0)

        self.Gerarbalanco = Button(self.container1, text='Gerar Balanço Financeiro', width=280)
        self.Gerarbalanco.grid(row=0, column=0, sticky=N+S+E+W)

        self.GerarPrecoTotal= Button(self.container2, text='Calcular Preço total do estoque', width=280)
        self.GerarPrecoTotal.grid(row=0, column=0, sticky= N+S+E+W)

        self.retornar=Button(self.container3, text='Retornar ao Menu Principal', width=280)
        self.retornar.grid(row=0, column=0, sticky= N+S+E+W)

        

 if __name__ == '__main__':
    window = Tk()
    RelatorioProdutos(window)
    window.title("Stocky")
    window.geometry("100x100")
    window.configure(background="Red", menu=Menu)
    window.state("zoomed")
    window.mainloop()