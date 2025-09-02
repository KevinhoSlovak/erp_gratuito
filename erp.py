from tkinter import *

class Login:
    def __init__(self):
        self.root = Tk()
        self.configs()
        self.frames()
        self.texts()
        self.buttons()

        self.root.mainloop()

    def configs(self):
        self.root.config(bg='grey31')
        self.root.state('zoomed')
        self.root.resizable(False, False)
        self.root.title('Slovak System - Version 1.0.0')

    def frames(self):
        # Menu de acesso
        self._acess_account = Frame(self.root, bg='grey31', highlightbackground='white', highlightthickness=1, highlightcolor='white')
        self._acess_account.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.5)

        # Tipo de Acesso ( registro / acesso )
        self._create_account = Frame(self._acess_account, highlightbackground='white', highlightthickness=1, bg='grey31')
        self._create_account.place(relx=0.02, rely=0.065, relwidth=0.96, relheight=0.12)

    def texts(self):
        # ERP System - Label de bem vindo!
        self._erp_system = Label(self.root, text='Login to ERP SYSTEM', activebackground='grey31', activeforeground='white', bg='grey31', fg='white', font='Consolas 20', highlightbackground='white', highlightthickness='1')
        self._erp_system.place(relx=0.3, rely=0.01, relwidth=0.4, relheight=0.06)

        # Slovak System - Label do nome do sistema!
        self._name_system = Label(self.root, text='© Slovak SYSTEM - 2025', activebackground='grey31', activeforeground='white', bg='grey31', fg='white', font='Consolas 20', highlightbackground='white', highlightthickness='1')
        self._name_system.place(relx=0.3, rely=0.93, relwidth=0.4, relheight=0.06)

        # Criar Conta?
        self._create_account_register_acess = Label(self._create_account, text='Criar conta:', bg='grey31', fg='white', font='Consolas 15')
        self._create_account_register_acess.place(relx=0, rely=0, relwidth=0.25, relheight=1)

    def buttons(self):
        def registrar():
            # Frame de Espaço de Registro
            self._data_registro = Frame(self._acess_account, highlightbackground='white', highlightcolor='white', highlightthickness=1, bg='grey31')
            self._data_registro.place(relx=0.02, rely=0.25, relwidth=0.96, relheight=0.725)
            # ------------------------- Nome Completo ------------------------------------------   
            # Label - Nome Completo
            self._name_complete_l = Label(self._data_registro, text='Nome Completo', bg='grey31', fg='white', font='Consolas 12', justify='left')
            self._name_complete_l.place(relx=0.025, rely=0.02, relwidth=0.2, relheight=0.1)

            # Entry = Nome Completo
            self._name_complete = Entry(self._data_registro, bg='grey31', font='white', highlightbackground='white', highlightthickness=1)
            self._name_complete.place(relx=0.02, rely=0.13, relwidth=0.96, relheight=0.1)
            self._name_complete.config(font='Consolas 15', fg='white')

            # ------------------------- CPF ------------------------------------------   
            # Label - CPF
            self._cpf_complete_l = Label(self._data_registro, text='CPF', bg='grey31', fg='white', font='Consolas 12', justify='left')
            self._cpf_complete_l.place(relx=0, rely=0.29, relwidth=0.1, relheight=0.1)

            # Entry = CPF
            self._cpf_complete = Entry(self._data_registro, bg='grey31', font='white', highlightbackground='white', highlightthickness=1)
            self._cpf_complete.place(relx=0.02, rely=0.4, relwidth=0.4, relheight=0.1)
            self._cpf_complete.config(font='Consolas 15', fg='white')

            # ------------------------- EMAIL ------------------------------------------   
            # Label - email
            self._email_complete_l = Label(self._data_registro, text='E-mail', bg='grey31', fg='white', font='Consolas 12', justify='left')
            self._email_complete_l.place(relx=0.44, rely=0.29, relwidth=0.4, relheight=0.1)

            # Entry = email
            self._email_complete = Entry(self._data_registro, bg='grey31', font='white', highlightbackground='white', highlightthickness=1)
            self._email_complete.place(relx=0.58, rely=0.4, relwidth=0.4, relheight=0.1)
            self._email_complete.config(font='Consolas 15', fg='white')

            # ------------------------- senha ------------------------------------------   
            # Label - senha
            self._senha_complete_l = Label(self._data_registro, text='Senha', bg='grey31', fg='white', font='Consolas 12', justify='left')
            self._senha_complete_l.place(relx=0.015, rely=0.56, relwidth=0.1, relheight=0.1)

            # Entry = senha
            self._senha_complete = Entry(self._data_registro, bg='grey31', font='white', highlightbackground='white', highlightthickness=1)
            self._senha_complete.place(relx=0.02, rely=0.67, relwidth=0.4, relheight=0.1)
            self._senha_complete.config(font='Consolas 15', fg='white')

            # ----------------------- DROP DOWN BUTTON - Tipo de Conta -----------------------------------------
            self._drop_complete = Label(self._data_registro, text='Tipo de Conta', bg='grey31', fg='white', font='Consolas 12', justify='left')
            self._drop_complete.place(relx=0.49, rely=0.56, relwidth=0.4, relheight=0.1)

            self._type_account = StringVar(self._data_registro)
            self._type_account.set('Selecionar')
            self._options_account = ('Gratuita', 'Paga')

            self._option_t_a_menu = OptionMenu(self._data_registro, self._type_account, *self._options_account)
            self._option_t_a_menu.place(relx=0.58, rely=0.67, relwidth=0.4, relheight=0.1)
            self._option_t_a_menu.config(font='Consolas 12')

            # ------------------------------ salvar -----------------------------------------------------
            self._save_register = Button(self._data_registro, text='Registrar Conta', activebackground='green', activeforeground='white', bg='green', fg='white', font='Consolas 12 bold')
            self._save_register.place(relx=0.35, rely=0.85, relwidth=0.3, relheight=0.13)

        def entrar():
            # Frame de Espaço de Registro
            self._data_account = Frame(self._acess_account, highlightbackground='white', highlightcolor='white', highlightthickness=1, bg='grey31')
            self._data_account.place(relx=0.02, rely=0.25, relwidth=0.96, relheight=0.725)

            # ------------------------- CPF ------------------------------------------   
            # Label - CPF
            self._cpf_complete_l = Label(self._data_account, text='CPF', bg='grey31', fg='white', font='Consolas 12', justify='left')
            self._cpf_complete_l.place(relx=0, rely=0.02, relwidth=0.1, relheight=0.1)

            # Entry = CPF
            self._cpf_complete = Entry(self._data_account, bg='grey31', font='white', highlightbackground='white', highlightthickness=1)
            self._cpf_complete.place(relx=0.02, rely=0.13, relwidth=0.4, relheight=0.1)
            self._cpf_complete.config(font='Consolas 15', fg='white')

            # ------------------------- EMAIL ------------------------------------------   
            # Label - email
            self._email_complete_l = Label(self._data_account, text='E-mail', bg='grey31', fg='white', font='Consolas 12', justify='left')
            self._email_complete_l.place(relx=0.44, rely=0.02, relwidth=0.4, relheight=0.1)

            # Entry = email
            self._email_complete = Entry(self._data_account, bg='grey31', font='white', highlightbackground='white', highlightthickness=1)
            self._email_complete.place(relx=0.58, rely=0.13, relwidth=0.4, relheight=0.1)
            self._email_complete.config(font='Consolas 15', fg='white')

            # ------------------------- senha ------------------------------------------   
            # Label - senha
            self._senha_complete_l = Label(self._data_account, text='Senha', bg='grey31', fg='white', font='Consolas 12', justify='left')
            self._senha_complete_l.place(relx=0.015, rely=0.29, relwidth=0.1, relheight=0.1)

            # Entry = senha
            self._senha_complete = Entry(self._data_account, bg='grey31', font='white', highlightbackground='white', highlightthickness=1)
            self._senha_complete.place(relx=0.02, rely=0.4, relwidth=0.4, relheight=0.1)
            self._senha_complete.config(font='Consolas 15', fg='white')

            # ----------------------- DROP DOWN BUTTON - Tipo de Conta -----------------------------------------
            self._drop_complete = Label(self._data_account, text='Tipo de Conta', bg='grey31', fg='white', font='Consolas 12', justify='left')
            self._drop_complete.place(relx=0.025, rely=0.56, relwidth=0.2, relheight=0.1)

            self._type_account = StringVar(self._data_account)
            self._type_account.set('Selecionar')
            self._options_account = ('Gratuita', 'Paga')
            self._option_t_a_menu = OptionMenu(self._data_account, self._type_account, *self._options_account)
            
            self._option_t_a_menu.place(relx=0.02, rely=0.67, relwidth=0.4, relheight=0.1)
            self._option_t_a_menu.config(font='Consolas 12')

            # ------------------------------ salvar -----------------------------------------------------
            self._save_register = Button(self._data_account, text='Acessar', activebackground='green', activeforeground='white', bg='green', fg='white', font='Consolas 12 bold')
            self._save_register.place(relx=0.35, rely=0.85, relwidth=0.3, relheight=0.13)

        # Registrar conta no ERP System.
        self._register = Button(self._create_account, text='Registrar conta', activebackground='white', activeforeground='black', bg='darkblue', fg='white', font='Consolas 12 bold', command=registrar)
        self._register.place(relx=0.26, rely=0, relwidth=0.32, relheight=1)

        # Acessar conta no ERP System.
        self._login = Button(self._create_account, text='Acessar conta', activebackground='white', activeforeground='black', bg='darkblue', fg='white', font='Consolas 12 bold', command=entrar)
        self._login.place(relx=0.645, rely=0, relwidth=0.32, relheight=1)

Login()