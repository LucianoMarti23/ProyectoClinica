import customtkinter as ctk
import os
import tkinter as tk
from PIL import ImageTk, Image
from paciente import Paciente
from profesional import Profesional
from turno import App
import sqlite3
from listaPacientes import ListaRegistro

class Frame(ctk.CTk):
    def __init__(self, geometria1, geometria2):
        super().__init__()
        
        self.geometry(f"{geometria1}x{geometria2}")
        self.title("Panel de Administracion de turnos")
        # Obtener la ruta del directorio del script actual
        script_directory = os.path.dirname(os.path.abspath(__file__))
        self.textoTurnos = ctk.CTkLabel(self, text="Turnos", text_color="white")
        self.textoTurnos.place(x=597, y=35, anchor=tk.CENTER)

        self.textoProfesionales = ctk.CTkLabel(self, text="Profesionales", text_color="white")
        self.textoProfesionales.place(x=350, y=35, anchor=tk.CENTER)

        self.textoPacientes = ctk.CTkLabel(self, text="Pacientes", text_color="white")
        self.textoPacientes.place(x=110, y=35, anchor=tk.CENTER)

        self.textoEnfermero = ctk.CTkLabel(self, text="Emergencias" , text_color="white")
        self.textoEnfermero.place(x=850 , y=35  , anchor=tk.CENTER)
        # Crear el marco
        frame1 = ctk.CTkFrame(master=self, width=200, height=400 , )
        frame1.place(x=10, y=60)


        frame2 = ctk.CTkFrame(master=self , width=200 , height=400)
        frame2.place(x=250, y=60)
         
        frame3 = ctk.CTkFrame(master=self , width=200 , height=400)
        frame3.place(x=500, y=60)

        frame4 = ctk.CTkFrame(master=self , width =200 , height=400)
        frame4.place(x= 750 , y=60)
        # Ruta relativa de la imagen en base al directorio del script
        image_doctora = "doctor.png"
        image_pathdoctora = os.path.join(script_directory,image_doctora)

        image_filename = "pacientes.png"
        image_path = os.path.join(script_directory, image_filename)
        
        image_especialidad = "emergencia.png"
        image_pathespecialidad = os.path.join(script_directory,image_especialidad)

        imagenEspecialidad = Image.open(image_pathespecialidad)
        imagenEspecialidad = imagenEspecialidad.resize((100,100) , Image.ANTIALIAS)

        ImagenInsertadaEspecialidad = ImageTk.PhotoImage(imagenEspecialidad)
        imagenDoc = Image.open(image_pathdoctora)
        imagenDoc = imagenDoc.resize((100 , 100), Image.ANTIALIAS)
        imagenInsertada = ImageTk.PhotoImage(imagenDoc)

        imagen_turnos  = "lista.png"
        imagen_pathturnos = os.path.join(script_directory,imagen_turnos)

        imagenTurnos = Image.open(imagen_pathturnos)
        imagenTurnos = imagenTurnos.resize((100,100) , Image.ANTIALIAS)
        imagenInsertadaTurnos = ImageTk.PhotoImage(imagenTurnos)

        # Cargar la imagen
        image = Image.open(image_path)
        image = image.resize((100, 100), Image.ANTIALIAS)  # Ajusta el tamaño de la imagen según tus necesidades
        image_tk = ImageTk.PhotoImage(image)
        
        # Crear el widget Label para mostrar la imagen dentro del marco
        imagenLabelPaciente = ctk.CTkLabel(frame1, image=image_tk, text=None)
        imagenLabelPaciente.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        imagenLabelProfesional = ctk.CTkLabel(frame2, image=imagenInsertada , text=None)
        imagenLabelProfesional.place(relx=0.5 , rely=0.1 , anchor=tk.CENTER)

        imagenLabelTurnos = ctk.CTkLabel(frame3 , image=imagenInsertadaTurnos , text=None)
        imagenLabelTurnos.place(relx=0.5 , rely=0.1 , anchor=tk.CENTER)  
        
        imagenEspecialidad = ctk.CTkLabel(frame4,image=ImagenInsertadaEspecialidad , text=None)
        imagenEspecialidad.place(relx=0.5 , rely=0.1 , anchor=tk.CENTER)
        self.button1 = ctk.CTkButton(frame1, text="Ingresar un paciente" , command=self.mostrarFrameOne)
        
        self.button1.place(relx=0.5 , rely=0.3 , anchor=tk.CENTER)

        self.buttonListaPacientes = ctk.CTkButton(frame1,text="Lista de pacientes" ,command=self.mostrarListaPacientes ,hover=True)
        self.buttonListaPacientes.place(relx=0.5 , rely=0.4 , anchor=tk.CENTER)
        self.button2 = ctk.CTkButton(frame2, text="Ingresar un profesional" ,command=self.mostrarFrameTwo )
        self.button2.place(relx=0.5, rely=0.3 , anchor=tk.CENTER)
        self.buttonListaProfesionales = ctk.CTkButton(frame2 , text="Lista de profesionales")
        self.buttonListaProfesionales.place(relx=0.5 , rely=0.4 , anchor=tk.CENTER)
        self.button3 = ctk.CTkButton(frame3, text="Ingresar un turno",command=self.mostrarFramThre)
        self.button3.place(relx=0.5 , rely=0.3 , anchor=tk.CENTER)

        self.buttonListaTurnos = ctk.CTkButton(frame3,text="Lista de turnos")
        self.buttonListaTurnos.place(relx=0.5 , rely=0.4 , anchor=tk.CENTER)

    def mostrarFramThre(self):
        self.turnosRegistro = App()
        self.turnosRegistro.mainloop()

    def mostrarListaPacientes(self):
        self.listapacientes = ListaRegistro()
        self.listapacientes.mainloop()

    def mostrarFrameOne(self):
        self.pacienteRegistro = Paciente()
        self.pacienteRegistro.mainloop()

    def mostrarFrameTwo(self):
        self.profesionalRegistro = Profesional()
        self.profesionalRegistro.mainloop()
        
if __name__ == "__main__":
    geometria1, geometria2 = 1024, 768
    ventana = Frame(geometria1, geometria2)
    ventana.mainloop()


