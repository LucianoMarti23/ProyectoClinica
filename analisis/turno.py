import customtkinter as ctk
import tkinter as tk
from tkcalendar import DateEntry
import sqlite3 
from tkinter import messagebox



a = ["hola","como"]
ctk.set_appearance_mode("System")

ctk.set_default_color_theme("blue")   
 
appWidth, appHeight = 1024, 768
 
profesionalWidth, profesionalHeight = 1024,768
# App Class
class App(ctk.CTk):

    def __init__(self, *args, **kwargs ):
        
        super().__init__(*args, **kwargs , )
 
        self.title("Sistema de Turno Medicos")
        self.geometry(f"{appWidth}x{appHeight}")
    
        self.dniLabel = ctk.CTkLabel(self,text = "D.N.I-Paciente")
        self.dniLabel.grid(row=0 , column=0 , padx=20 , pady=20 , sticky="ew" )

        self.dniEntry = ctk.CTkEntry(self,placeholder_text="Ingrese D.N.i paciente")
        self.dniEntry.grid(row=0 , column=1 , padx=20 , pady=20 , columnspan=3 , sticky ="ew")
                # Genero opcion

        self.profesionalDniLabel = ctk.CTkLabel(self,text="D.N.I-Profesional")
        self.profesionalDniLabel.grid(row=1,column=0 , padx=20 , pady=20 , sticky = "ew")   

        self.profesionalDniEntry = ctk.CTkEntry(self, placeholder_text="Ingrese D.N.I profesional")
        self.profesionalDniEntry.grid(row=1,column=1,padx=20,pady=20, columnspan=3, sticky='ew')     

        
        self.cargarDatos = ctk.CTkButton(self,
                                         text="Cargar  Turno" )
        
        self.cargarDatos.grid(row=9, column=1,
                                        columnspan=9,
                                        padx=20, pady=20,
                                        sticky="ew",)

        self.calendarLabel = ctk.CTkLabel(self,text="Fecha")
        self.calendarLabel.grid(row=2 , column=0 , padx=20 , pady=20)
        self.calendarioEntry = DateEntry(self, width=50, background='gray',
        
                          foreground='gray', borderwidth=10 , heigth=50)
        
        self.calendarioEntry.grid(row=2, column=1, padx=20, pady=20,
                   columnspan=3, sticky="ew")
        
        self.horaLabel = ctk.CTkLabel(self, text="Hora")
        self.horaLabel.grid(row=3 , column=0 , padx=20 , pady=20 , sticky='ew')

        self.horaEntry = ctk.CTkEntry(self, placeholder_text="Ingrese Hora del turno")
        self.horaEntry.grid(row=3 ,column=1 , padx=20 , pady=20 , columnspan=3 , sticky="ew" )
 
if __name__ == "__main__":
    app = App()

    app.mainloop()