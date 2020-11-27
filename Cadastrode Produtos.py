from tkinter import *
from tkinter.ttk import *



class CadastroProdutos():
    def __init__(self, master=None):
        self.container1 = Frame(master, width=320)
        self.container1.grid(row=0, column=0)

        self.container2 = Frame(master, width=320)
        self.container2.grid(row=0, column=0)

        self.container3 = Frame(master, width=320)
        self.container3.grid(row=0, column=0)

        self.container4=Frame(master, width=320)
        self.container4.grid(row=0, column=0)

        self.container5=Frame(master, width=320)
        self.container5.grid(row=0, column=0)





        self.cadastronomeL = Label(self.container1, text='Nome do Produto:', width=280)
        self.cadastronomeL.grid(row=0, column=0, sticky=N+S+E+W)

        self.cadastronome=Entry(self.container1, width=280)
        self.cadastronome.grid(row=1, column=0, sticky=N+S+E+W)

        self.cadastroprecoL = Label(self.container2, text='Preço do Produto:', width=280)
        self.cadastroprecoL.grid(row=0, column=0, sticky=N+S+E+W)

        self.cadastropreco= Entry(self.container2, width=280)
        self.cadastropreco.grid(row=1,column=1, sticky=N+S+E+W)

        self.cadastroquantidadeL= Label(self.container3,text='Quantidade do Produto', width=280)
        self.cadastroquantidadeL.grid(row=0, column=0, sticky=N+S+E+W)

        self.cadastroquantidade= Entry(self.container3, width=280)
        self.cadastroquantidade.grid(row=1, column=1, sticky=N+S+E+W)

        self.cadastrarproduto= Button(self.container4, text='Cadastrar Produto' ,width=280)
        self.cadastrarproduto.grid(row=0, column=0, sticky=N+S+E+W)


        self.retorno= Button(self.container5, text='Retornar ao Menu Principal' ,width=280)
        self.retorno.grid(row=0, column=0, sticky=N+S+E+W)













if __name__ == '__main__':
    window = Tk()
    CadastroProdutos(window)
    window.title("Stocky")
    window.geometry("100x100")
    window.configure(background="Red", menu=Menu)
    window.state("zoomed")
    window.mainloop()