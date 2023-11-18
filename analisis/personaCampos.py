import customtkinter as ctk
import tkinter as tk
appWidth , appHeight = 1024 , 768

class PersonaCampos(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry(f"{appWidth}x{appHeight}")
        self.title("Persona")

        self.nameLabel = ctk.CTkLabel(self,
                                      text="Nombre")
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
        
        self.nombreEntry = ctk.CTkEntry(self,
                         placeholder_text="Ingrese su nombre")
        self.nombreEntry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
        
        self.correoLabel = ctk.CTkLabel(self,text="Correo")
        self.correoLabel.grid(row=6 , column=0 , padx=20 , pady=20)

        self.correoEntry = ctk.CTkEntry(self,placeholder_text="Ingrese su correo")
        self.correoEntry.grid(row=6 , column=1 , padx=20 , pady=20 , columnspan=3, sticky="ew")
        # Ag
        self.apellidoLabel = ctk.CTkLabel(self,
                                     text="Apellido")
        self.apellidoLabel.grid(row=1, column=0,
                           padx=20, pady=20,
                           sticky="ew")
 
        # Age Entry Field
        self.apellidoEntry = ctk.CTkEntry(self,
                            placeholder_text="Ingrese su apellido")
        self.apellidoEntry.grid(row=1, column=1,
                           columnspan=3, padx=20,
                           pady=20, sticky="ew")
 
        self.telefonoLabel = ctk.CTkLabel(self,text="Telefono")
        self.telefonoLabel.grid(row=7,column=0 , padx=20, pady=20 , sticky='ew')

        self.telefoEntry = ctk.CTkEntry(self,placeholder_text="Ingrese su telefono")
        self.telefoEntry.grid(row=7 , column=1 , padx=20 , pady=20 , sticky='ew' , columnspan=3)
        # Correo Label
        self.edadLabel = ctk.CTkLabel(self,text="Edad")
        self.edadLabel.grid(row=2 , column=0,
                        padx=30 ,pady=20 ,sticky="ew" , )
        
        self.edadEntry = ctk.CTkEntry(self,placeholder_text="Ingrese su edad")
        self.edadEntry.grid(row=2 , column =1 , columnspan=3, padx=20, pady=20, sticky="ew")

        self.dniLabel = ctk.CTkLabel(self,text = "D.N.I")
        self.dniLabel.grid(row=3 , column=0 , padx=20 , pady=20 , sticky="ew" )

        self.dniEntry = ctk.CTkEntry(self,placeholder_text="Ingrese su D.N.i")
        self.dniEntry.grid(row=3 , column=1 , padx=20 , pady=20 , columnspan=3 , sticky ="ew")
                # Genero opcion
        self.direccion = ctk.CTkLabel(self,text="Direccion")
        self.direccion.grid(row=4 , column=0 , padx=20 , pady=20 , sticky="ew")

        self.direccionEntry = ctk.CTkEntry(self,placeholder_text="Ingrese su direccion" )
        self.direccionEntry.grid(row=4 , column=1 , padx=20 , pady=20 , columnspan=3 , sticky="ew")

        self.generoLabel = ctk.CTkLabel(self,
                                     text="Genero")
        self.generoLabel.grid(row=8, column=0,
                               padx=20, pady=20,
                               sticky="ew")
 
        self.generoEntry = tk.StringVar(value="")
 
        self.maleRadioButton = ctk.CTkRadioButton(self,
                                   text="Masculino",
                                   variable=self.generoEntry,
                                             value="Masculino")
        self.maleRadioButton.grid(row=8, column=1, padx=20,
                                   pady=20, sticky="ew")
 
        self.femaleRadioButton = ctk.CTkRadioButton(self,
                                       text="Femenino",
                                       variable=self.generoEntry,
                                       value="Femenino")
        self.femaleRadioButton.grid(row=8, column=2,
                                     padx=20,
                                     pady=20, sticky="ew")
         
        self.noneRadioButton = ctk.CTkRadioButton(self,
                                     text="Prefiero no decirlo",
                                     variable=self.generoEntry,
                                             value="Ambos")
        self.noneRadioButton.grid(row=8, column=3,
                                   padx=20, pady=20,
                                   sticky="ew")

        self.cargarDatos = ctk.CTkButton(self,
                                         text="Listo" , command=self.insertarTurno)
        
        self.cargarDatos.grid(row=9, column=1,
                                        columnspan=9,
                                        padx=20, pady=20,
                                        sticky="ew",)