import customtkinter as ctk
import tkinter as tk
from tkcalendar import DateEntry
import sqlite3 
from tkinter import messagebox
from personaCampos import PersonaCampos



ctk.set_appearance_mode("System")
 
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("blue")   
 
appWidth, appHeight = 1024, 768




profesionalWidth, profesionalHeight = 1024,768
# App Class
class Paciente(PersonaCampos):
    
    def bloquear_choice(self):
            if self.checkboxVar.get() == "SI":
                self.choice2.configure(state="disabled")
            elif self.checkboxVar.get() == "NO":
                self.choice1.configure(state="disabled")     
            else:
                self.choice2.configure(state="normal")
                self.choice1.configure(state="normal")   

    def limpiarCampos(self):
         self.nombreEntry.delete(0,ctk.END)    
         self.apellidoEntry.delete(0,ctk.END)
         self.edadEntry.delete(0,ctk.END)
         self.telefoEntry.delete(0 ,ctk.END)
         self.direccionEntry.delete(0 ,ctk.END)
         self.correoEntry.delete(0,ctk.END)
         self.dniEntry.delete(0,ctk.END)

    
         
             
    

    def insertarTurno(self):

        conexion = sqlite3.connect("baseturnos.db")

        cursor = conexion.cursor()

        condiciones = [
                self.nombreEntry.get().isalpha(),
                self.apellidoEntry.get().isalpha(),
                self.edadEntry.get().isnumeric(),
                self.telefoEntry.get().isnumeric(),
                self.dniEntry.get().isnumeric()
         ]




        if "" in [self.nombreEntry.get() , self.apellidoEntry.get() , self.edadEntry.get() , self.telefoEntry.get() , self.direccionEntry.get() , self.correoEntry.get() , self.dniEntry.get() , self.generoEntry.get() , self.checkboxVar.get()]:
             return messagebox.showerror("Error" , "Todos los campos son obligatorios")
        
        
        elif  not all(condiciones):
                return messagebox.showerror("Error" , "Ingresate mal datos en campos")
        else :
                try :
                        cursor.execute('''
                        INSERT INTO pacientes (nombre , apellido , edad , telefono , dni , direccion , correo , obrasocial , sexo)
                        VALUES(?,?,?,?,?,?,?,?,?)   
                        ''', (self.nombreEntry.get(),self.apellidoEntry.get(),self.edadEntry.get(),self.telefoEntry.get() , 
                                self.dniEntry.get() , self.direccionEntry.get() ,self.correoEntry.get() , self.checkboxVar.get() , self.generoEntry.get() 
                                ))
                        conexion.commit()
                        conexion.close()
                        messagebox.showinfo("Paciente" , "Paciente Cargado con Exito")
                        self.limpiarCampos()
                
                except : messagebox.showerror("ERROR" , "ALGO SALIO MAL")
        conexion.close()    
        
    def __init__(self, *args, **kwargs ):
        
        

        super().__init__(*args, **kwargs , )
 

        self.obrasocialLabel = ctk.CTkLabel(self,
                                        text="Obra social")
        self.obrasocialLabel.grid(row=0, column=4,
                              padx=20, pady=20,
                              sticky="ew")
        # Choice Check boxes
        self.checkboxVar = tk.StringVar(value="")
         
        self.choice1 = ctk.CTkCheckBox(self, text="Si",
                                       variable=self.checkboxVar,
                                       onvalue="SI",
                                       offvalue="c1",
                                        command=self.bloquear_choice)
        self.choice1.grid(row=0, column=5, padx=20,
                          pady=20, sticky="ew")
 
        self.choice2 = ctk.CTkCheckBox(self, text="No",
                                       variable=self.checkboxVar,
                                       onvalue="NO",
                                       offvalue="c2",
                                       command=self.bloquear_choice)                              
        self.choice2.grid(row=0, column=6, padx=20, pady=20,
                          sticky="ew")

