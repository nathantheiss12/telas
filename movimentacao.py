from tkinter import *
from tkinter.ttk import *



class MovimentacaoProdutos():
    def __init__(self, master=None):
        self.container1 = Frame(master, width=320)
        self.container1.grid(row=0, column=0)

        self.container2 = Frame(master, width=320)
        self.container2.grid(row=1, column=0)

         self.container3 = Frame(master, width=320)
        self.container3.grid(row=1, column=0)

        
    

        self.Entradaprodutos = Button(self.container1, text='Entrada de Produtos', width=280)
        self.Entradaprodutos.grid(row=0, column=0, sticky=N+S+E+W)

        self.Vendaprodutos=Button(self.container2, text='Saida de Produtos' width=280)
        self.Vendaprodutos.grid(row=0, column=0, sticky=N+S+E+W)

        self.retornar=Button(self.container3, text='Retornar ao Menu Principal', width=280)
        self.retornar.grid(row=0, column=0, sticky= N+S+E+W)

 if __name__ == '__main__':
    window = Tk()
    MovimentacaoProdutos(window)
    window.title("Stocky")
    window.geometry("100x100")
    window.configure(background="Red", menu=Menu)
    window.state("zoomed")
    window.mainloop()