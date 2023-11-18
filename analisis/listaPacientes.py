import customtkinter as ctk
import sqlite3

appWidth, appHeight = 1024, 768

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from paciente import Paciente

class ListaRegistro(ctk.CTk):
    def FitrarDatos(self):
            conexion = sqlite3.connect("baseturnos.db")   
            cursor = conexion.cursor()
            try: 
                cursor.execute('''
                SELECT * FROM pacientes WHERE dni =?

                ''',(self.filtro1Entry.get(),))
                datos = cursor.fetchall()

                conexion.close()
                if datos:
                    self.treeview.delete(*self.treeview.get_children())
                    for paciente in datos:
                        self.treeview.insert("", tk.END, values=paciente)
                else : return  messagebox.showinfo("Error","No se encontro el dni")
            
            except : messagebox.showinfo("Error" , "Algo salio mal")
                       
    

  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Lista de Pacientes")
        self.geometry(f"{appWidth}x{appHeight}")
        
    

        self.filtro = ctk.CTkButton(self,text="Buscar" , command=self.FitrarDatos)
        self.filtro.grid(row=0 , column=0 , padx=20 , pady=20 , sticky="ew")

        self.filtro1Entry = ctk.CTkEntry(self,placeholder_text="Ingrese el DNI")
        self.filtro1Entry.grid(row=0 , column=2 , padx=20 , pady=20 , columnspan=2)

        self.frame1 = ctk.CTkFrame(master=self, width=1100, height=500)
        self.frame1.place(x=10, y=60)

        # Crear el Treeview dentro del frame1
        self.treeview = ttk.Treeview(self.frame1)
        self.treeview["columns"] = ("ID","NOMBRE", "APELLIDO", "EDAD" , "TELEFONO" , "DNI" , "DIRECCION" , "CORREO" , "OBRASOCIAL" , "SEXO" )  # Definir las columnas del Treeview

        # Configurar las columnas
        self.framePanel = ctk.CTkFrame(master=self, width=200, height=500)
        self.framePanel.place(x=1125, y=60)

        self.elminar = ctk.CTkButton(self.framePanel,text="Eliminar",command=self.eliminarDatos)
        self.elminar.place(relx=0.5 , rely=0.1 , anchor=tk.CENTER)

        self.modificar = ctk.CTkButton(self.framePanel,text="Modificar",command=self.ModificarDatos)
        self.modificar.place(relx=0.5 , rely=0.3 , anchor=tk.CENTER)

        lista = ['ID' , 'NOMBRE' , 'APELLIDO' , 'EDAD' , 'DNI' 
        , 'TELEFONO' , 'DIRECCION' , 'CORREO' , 'OBRASOCIAL' , 'SEXO']

        for i in lista : 
            self.treeview.column(i,anchor=tk.W,width=100,minwidth=50)
            self.treeview.heading(i, text=i)

        self.treeview.column("ID", anchor=tk.W, width=3 ,minwidth=50)  # Columna de índice
        self.treeview.column("#0", width=0, stretch=False)

        # Agregar algunos datos de ejemplo
    
        self.treeview.place(width=1644 , height=740)
        # Ajustar el tamaño del Treeview
        self.TraerDatos()

    def TraerDatos(self):
        conexion = sqlite3.connect("baseturnos.db")   
        cursor = conexion.cursor()

        cursor.execute(''' SELECT * FROM pacientes ''')
        datos = cursor.fetchall()  # Ejecutar el método fetchall para obtener los resultados

        for paciente in datos:
            self.treeview.insert("", tk.END, values=paciente)

            conexion.close()

    def eliminarDatos(self):
         

         confirmacion = messagebox.askyesno(title="Eliminar" , message="Estas seguro que desea eliminar el registro?")

         if confirmacion and self.treeview.focus():
            registro_id = self.treeview.item(self.treeview.focus())['values'][0]

            conexion = sqlite3.connect("baseturnos.db")

            cursor = conexion.cursor()

            cursor.execute('''DELETE FROM pacientes WHERE ID=?''', (registro_id,))

            conexion.commit()

            self.treeview.delete(self.treeview.focus())
            
            conexion.close()
      

             

    def ModificarDatos(self):
            self.pacientes = Paciente()
            

            self.pacientes.mainloop()
            





        
       



