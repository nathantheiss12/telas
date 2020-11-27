from tkinter import *
from tkinter.ttk import *



class Atualizarproduto():
    def __init__(self, master=None):
        self.container1 = Frame(master, width=320)
        self.container1.grid(row=0, column=0)

        self.container2 = Frame(master, width=320)
        self.container2.grid(row=1, column=0)

        self.container3 = Frame(master, width=320)
        self.container3.grid(row=1, column=0)

        self.container4 = Frame(master, width=320)
        self.container4.grid(row=1, column=0)

        self.container5 = Frame(master, width=320)
        self.container5.grid(row=1, column=0)

        self.container6 = Frame(master, width=320)
        self.container6.grid(row=1, column=0)



        self.procurarprodutoL = Label(self.container1, text='Insira o nome do produto', width=280)
        self.procurarprodutosL.grid(row=0, column=0, sticky=N+S+E+W)

        self.procurarproduto = Entry(self.container1,  width=280)
        self.procurarprodutos.grid(row=1, column=0, sticky=N+S+E+W)

        self.novonomeL = Label(self.container2, text='Insira o novo nome', width=280)
        self.novonomeL.grid(row=0, column=0 , sticky= N+S+E+W)

        self.novonome = Entry(self.container2,  width=280)
        self.novonome.grid(row=0, column=0 , sticky= N+S+E+W)

        self.novoprecoL = Label(self.container3, text='Insira o novo preço', width=280)
        self.novoprecoL.grid(row=0, column=0 , sticky= N+S+E+W)

        self.novopreco = Entry(self.container3,  width=280)
        self.novopreco.grid(row=0, column=0 , sticky= N+S+E+W)

        
        self.novaquantidadeL = Label(self.container4, text='Insira a nova quantidade', width=280)
        self.novaquantidadeL.grid(row=0, column=0 , sticky= N+S+E+W)

        self.novaquantidade = Entry(self.container4,  width=280)
        self.novaquantidade.grid(row=0, column=0 , sticky= N+S+E+W)


        self.confirmar= Button(self.container5, text='Confirmar mudança', width=280)
        self.confirmar.grid(row=0, column=0, sticky= N+S+E+W)

        self.retornar=Button(self.container6, text='Retornar ao Menu Principal', width=280)
        self.retornar.grid(row=0, column=0, sticky= N+S+E+W)

        



       if __name__ == '__main__':
    window = Tk()
    Atualizarproduto(window)
    window.title("Stocky")
    window.geometry("100x100")
    window.configure(background="Red", menu=Menu)
    window.state("zoomed")
    window.mainloop()
