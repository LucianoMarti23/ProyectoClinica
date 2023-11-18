import customtkinter as ctk
import tkinter as tk
from tkcalendar import DateEntry
from turno import *
from PIL import ImageTk
from tkinter import messagebox
from frame import Frame

usuario = "root"
contra = "root"

appWidth, appHeight = 1024, 768

class Login(ctk.CTk):
     def autenticarContra(self):
       
        if usuario == self.usuarioEntry.get() and contra == self.contraseniaEntry.get():
            self.destroy()  # Cerrar la ventana actual de login
            panel = Frame(appWidth,appHeight)
            
            return panel.mainloop()
            
        else :  return messagebox.showerror("Error" , "Usuario o Contrasenia invalidos!")
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.title("Log in")
        self.geometry(f"{appWidth}x{appHeight}")

        self.image = ImageTk.PhotoImage(file="./imagenes/images.jpg")
        self.imagenLabel = tk.Label(self, image=self.image)
        self.imagenLabel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.usuario = ctk.CTkLabel(self, text="Usuario")
        self.usuario.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.usuarioEntry = ctk.CTkEntry(self , placeholder_text="Ingrese su usuario")
        self.usuarioEntry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        self.contrasenia = ctk.CTkLabel(self, text="Contraseña")
        self.contrasenia.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        self.contraseniaEntry = ctk.CTkEntry(self, show="*" , placeholder_text="Ingrese su contrasenia")
        self.contraseniaEntry.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.login = ctk.CTkButton(self, text="Ingresar" , command=self.autenticarContra)
        self.login.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

login = Login()
login.mainloop()