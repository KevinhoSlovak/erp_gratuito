import tkinter
from tkinter import *

class Login:
    def __init__(self):
        self.root = Tk()
        self.configurations()
        self.page()

        self.root.mainloop()

    def configurations(self):
        self.root.config(width=800, height=500, bg="#385B8A")
        self.root.resizable(False, False)
        self.root.title('Login to Slovak Studios')

    def page(self):
        def dw():
            self.root.destroy()
            Register()

        # Frame do nome do sistema
        self.f_message = Frame(self.root, bg="#385B8A", highlightthickness=1.5, highlightbackground='white', highlightcolor='white')
        self.f_message.place(relx=0.2, rely=0.02, relwidth=0.6, relheight=0.08)

        # Label do nome do sistema
        self.l_message = Label(self.f_message, text='ACESSE SUA CONTA', bg="#385B8A", fg='white', font='Consolas 20 bold')
        self.l_message.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Frame do campo de login
        self.f_form = Frame(self.root, bg="#385B8A", highlightthickness=1.5, highlightbackground='white', highlightcolor='white')
        self.f_form.place(relx=0.2, rely=0.5, relwidth=0.6, relheight=0.48)

        # Label do nome do Usuário
        self.l_user = Label(self.f_form, text='Usuário:', bg="#385B8A", fg='white', font='Consolas 14 bold')
        self.l_user.place(relx=0.01, rely=0.075, relwidth=0.2, relheight=0.1)

        # Entry do nome do Usuário
        self.e_entry = Entry(self.f_form, bg='white', fg='black', font='Consolas 14')
        self.e_entry.place(relx=0.02, rely=0.185, relwidth=0.96, relheight=0.1)

        # Label do senha do Usuário
        self.l_pass = Label(self.f_form, text='Senha: ', bg="#385B8A", fg='white', font='Consolas 14 bold')
        self.l_pass.place(relx=0, rely=0.35, relwidth=0.2, relheight=0.1)

        # Entry do senha do Usuário
        self.e_entry = Entry(self.f_form, bg='white', fg='black', font='Consolas 14', show='*')
        self.e_entry.place(relx=0.02, rely=0.46, relwidth=0.96, relheight=0.1)

        # Button de senha esquecida
        self.b_pass = Button(self.f_form, text='ESQUECI A SENHA', activebackground='#385B8A', bg='#385B8A', activeforeground='white', fg='white', font='Consolas 8', borderwidth=0)
        self.b_pass.place(relx=0.3, rely=0.59, relwidth=0.4, relheight=0.06)

        # Button de Login
        self.b_login = Button(self.f_form, text='LOGIN', activebackground='green', bg='green', activeforeground='white', fg='white', font='Consolas 12 bold', borderwidth=0)
        self.b_login.place(relx=0.02, rely=0.775, relwidth=0.3, relheight=0.15)

        # Button de Registro
        self.b_login = Button(self.f_form, text='REGISTRO', activebackground='green', bg='green', activeforeground='white', fg='white', font='Consolas 12 bold', borderwidth=0, command=dw)
        self.b_login.place(relx=0.68, rely=0.775, relwidth=0.3, relheight=0.15)


class Register:
    def __init__(self):
        self.root = Tk()
        self.configurations()
        self.page()

        self.root.mainloop()

    def configurations(self):
        self.root.config(width=800, height=500, bg="#385B8A")
        self.root.resizable(False, False)
        self.root.title('Register to Slovak Studios')

    def page(self):
        def dw():
            self.root.destroy()
            Login()

        # Frame do nome do sistema
        self.f_message = Frame(self.root, bg="#385B8A", highlightthickness=1.5, highlightbackground='white', highlightcolor='white')
        self.f_message.place(relx=0.2, rely=0.02, relwidth=0.6, relheight=0.08)

        # Label do nome do sistema
        self.l_message = Label(self.f_message, text='REGISTRE SUA CONTA', bg="#385B8A", fg='white', font='Consolas 20 bold')
        self.l_message.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Frame do campo de login
        self.f_form = Frame(self.root, bg="#385B8A", highlightthickness=1.5, highlightbackground='white', highlightcolor='white')
        self.f_form.place(relx=0.2, rely=0.5, relwidth=0.6, relheight=0.48)

        # Label do nome do Usuário
        self.l_user = Label(self.f_form, text='Usuário:', bg="#385B8A", fg='white', font='Consolas 14 bold')
        self.l_user.place(relx=0.01, rely=0.075, relwidth=0.2, relheight=0.1)

        # Entry do nome do Usuário
        self.e_entry = Entry(self.f_form, bg='white', fg='black', font='Consolas 14')
        self.e_entry.place(relx=0.02, rely=0.185, relwidth=0.96, relheight=0.1)

        # Label do senha do Usuário
        self.l_pass = Label(self.f_form, text='Senha: ', bg="#385B8A", fg='white', font='Consolas 14 bold')
        self.l_pass.place(relx=0, rely=0.35, relwidth=0.2, relheight=0.1)

        # Entry do senha do Usuário
        self.e_entry = Entry(self.f_form, bg='white', fg='black', font='Consolas 14', show='*')
        self.e_entry.place(relx=0.02, rely=0.46, relwidth=0.96, relheight=0.1)

        # Estado do checkbutton
        self.estado = tkinter.IntVar()

        # Criando o checkbutton
        self.checkButton = tkinter.Checkbutton(self.f_form, text="Você concorda com nossos termos e condições?", variable=self.estado, activebackground="#385B8A", activeforeground="white", bg="#385B8A", fg='white', font='Consolas 12', selectcolor="#385B8A")
        self.checkButton.place(relx=0.01, rely=0.615, relheight=0.1)

        # Button de Login
        self.b_login = Button(self.f_form, text='REGISTRO', activebackground='green', bg='green', activeforeground='white', fg='white', font='Consolas 12 bold', borderwidth=0)
        self.b_login.place(relx=0.02, rely=0.775, relwidth=0.3, relheight=0.15)

        # Button de Registro
        self.b_login = Button(self.f_form, text='LOGIN', activebackground='green', bg='green', activeforeground='white', fg='white', font='Consolas 12 bold', borderwidth=0, command=dw)
        self.b_login.place(relx=0.68, rely=0.775, relwidth=0.3, relheight=0.15)


if __name__ == "__main__":
    Login()
