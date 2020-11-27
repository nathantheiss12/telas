from tkinter import *
from tkinter.ttk import *



class MenuPrincipal():
    def __init__(self, master=None):
        self.container1 = Frame(master, width=320)
        self.container1.grid(row=0, column=0)

        self.container2 = Frame(master, width=320)
        self.container2.grid(row=1, column=0)

        self.container3 = Frame(master, width=320)
        self.container3.grid(row=2, column=0)

        self.container4 = Frame(master, width=320)
        self.container4.grid(row=4, column=0)

        self.container5 = Frame(master, width=320)
        self.container5.grid(row=5, column=0)



        self.cadastroproduto = Button(self.container1, text='Cadastro de Produtos', width=280)
        self.cadastroproduto.grid(row=0, column=0, sticky=N+S+E+W)

        self.movimentacao= Button(self.container2, text='Movimentacao de Produtos', width=280)
        self.movimentacao.grid(row=1, column=0, sticky=N+S+E+W)

        self.reajuste = Button(self.container3, text='Reajuste de Preços', width=280)
        self.reajuste.grid(row=2, column=0, sticky=N+S+E+W)

        self.relatorios= Button(self.container4, text='Relatórios', width=280)
        self.relatorios.grid(row=3, column=0, sticky= N+S+E+W)

        self.finalizar= Button(self.container5, text='Finalizar Programa', width=280)
        self.finalizar.grid(row=4, column=0, sticky=N+S+E+W)







if __name__ == '__main__':
    window = Tk()
    MenuPrincipal(window)
    window.title("Stocky")
    window.geometry("100x100")
    window.configure(background="Red", menu=Menu);
    window.state("zoomed")
    window.mainloop()