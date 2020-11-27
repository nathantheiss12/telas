from tkinter import *
from tkinter.ttk import *



class Login():
    def __init__(self, master=None):
        self.container1 = Frame(master, width=320)
        self.container1.grid(row=0, column=0)

        self.container2 = Frame(master, width=320)
        self.container2.grid(row=1, column=0)

        self.container3 = Frame(master, width=320)
        self.container3.grid(row=2, column=0)

        self.container4 = Frame(master, width=320)
        self.container4.grid(row=4, column=0)

        self.usuarioL = Label(self.container1, text='Usuario', width=320)
        self.usuarioL.grid(row=0, column=0, sticky=N+S+E+W)

        self.usuario = Entry(self.container1, width=320)
        self.usuario.grid(row=1, column=0, sticky=N+S+E+W)

        self.senhaL = Label(self.container2, text='Senha', width=320)
        self.senhaL.grid(row=0, column=0, sticky=N+S+E+W)

        self.senha = Entry(self.container2, width=320)
        self.senha.grid(row=1, column=0, sticky=N+S+E+W)

        self.logar = Button(self.container3, text='Acessar', width=320)
        self.logar.grid(row=2, column=0, sticky=N+S+E+W)

        self.mensagem = Label(self.container4, text='Não tem conta? ', width=320, anchor='center')
        self.mensagem.grid(row=0, column=0)

        self.registrabotao = Button(self.container4, text='Registre-se', width=320)
        self.registrabotao.grid(row=1, column=0, sticky=N+S+E+W)


if __name__ == '__main__':
    window = Tk()
    Login(window)
    window.title("Stocky")
    window.geometry("100x100")
    window.configure(background="Red", menu=Menu)
    window.state("zoomed")
    window.mainloop()