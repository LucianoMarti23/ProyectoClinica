import customtkinter as ctk
import tkinter as tk
from tkcalendar import DateEntry
import sqlite3 
from tkinter import messagebox
from personaCampos import PersonaCampos

ctk.set_appearance_mode("System")
 
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("blue")   
 
a = ["hola","como"]
# App Class
class Profesional(PersonaCampos):

    def insertarTurno(self):
        conexion = sqlite3.connect("baseturnos.db")

        cursor = conexion.cursor()

        cursor.execute('''
                INSERT INTO profesionales (nombre , apellido , dni , numero , correo , especialidad , direccion)
                VALUES(?,?,?,?,?,?,?)  
                ''', (self.nombreEntry.get(),self.apellidoEntry.get(),self.dniEntry.get(),
                      self.telefoEntry.get(), self.correoEntry.get() , self.profesionalEntry.get() , self.direccionEntry.get() ))
        conexion.commit()

        conexion.close()        

    def __init__(self, *args, **kwargs ):
        
        super().__init__(*args, **kwargs , )

        self.profesionLabel = ctk.CTkLabel(self,
                                             text="Especialidad")
        self.profesionLabel.grid(row=0, column=4,
                                   padx=20, pady=20,
                                   sticky="ew")
 
        self.profesionalEntry = ctk.CTkOptionMenu(self,
                                         values=(a))
        self.profesionalEntry.grid(row=0, column=5,
                                        padx=20, pady=20,
                                        columnspan=3, sticky="ew")

        self.cargarDatos = ctk.CTkButton(self,
                                         text="Cargar  Turno" , command=self.insertarTurno)
        
        self.cargarDatos.grid(row=9, column=1,
                                        columnspan=9,
                                        padx=20, pady=20,
                                        sticky="ew",)

if __name__ == "__main__":
    app = Profesional()

    app.mainloop()
        