#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import sqlite3
from tkinter.messagebox import showinfo
import os

def Cruzar():

    BD = "CUITS.db"
    Excel ="CUITS.xlsx"

    # Leer la BD de SQLite
    Cuits = pd.read_sql_query("SELECT * FROM CUITs", sqlite3.connect(BD))

    # Leer el archivo de Excel
    df = pd.read_excel(Excel)

    # Convertir el CUIT a string
    df['CUIT'] = df['CUIT'].astype(str)

    # si el CUIT esta en la lista, se agrega una columna con el valor "Cruzado"
    df["Cruzado"] = df["CUIT"].isin(Cuits["CUIT"]).map({True: "Cruzado", False: "No cruzado"})

    # Guardar el dataframe en un archivo de Excel
    df.to_excel("Cruce.xlsx", index=False)

    showinfo("Cruce", "El archivo se ha cruzado correctamente en el archivo Cruce.xlsx donde se encuentra el ejecutable")
        
def Ver_Archivo():
    os.system("start excel.exe Cruce.xlsx")
    
def Cafecito():
    os.system("start https://cafecito.app/abustos")
    
def LinkedIn_Leo():
    os.system("start https://www.linkedin.com/in/leonardo-sola-b2707b195/")
    
def LinkedIn_ABP():
    os.system("start https://www.linkedin.com/in/agust%C3%ADn-bustos-piasentini-468446122/")
    
def Abrir_Excel():
    os.system("start excel.exe CUITS.xlsx")

class App:
    def __init__(self, master=None):
        # build ui
        Toplevel_1 = tk.Tk() if master is None else tk.Toplevel(master)
        Toplevel_1.configure(
            background="#2e2e2e",
            cursor="arrow",
            height=250,
            width=325)
        Toplevel_1.iconbitmap("ABP-blanco-en-fondo-negro.ico")
        Toplevel_1.minsize(325, 250)
        Toplevel_1.overrideredirect("False")
        Toplevel_1.resizable(False, False)
        Toplevel_1.title("Cruce de Bases Filtradas ")
        Label_3 = ttk.Label(Toplevel_1)
        self.img_ABPblancoenfondonegro111 = tk.PhotoImage(
            file="ABP-blanco-sin-fondo.png")
        Label_3.configure(
            background="#2e2e2e",
            image=self.img_ABPblancoenfondonegro111)
        Label_3.pack(side="top")
        Label_1 = ttk.Label(Toplevel_1)
        Label_1.configure(
            background="#2e2e2e",
            cursor="arrow",
            foreground="#ffffff",
            justify="center",
            takefocus=False,
            text='Cruce de CUITs con la Base de Datos Filtrada, en caso de cruce se recomienda cambiar la clave de manera INMEDIATA.\n',
            wraplength=325)
        Label_1.pack(expand=True, side="top")
        Label_2 = ttk.Label(Toplevel_1)
        Label_2.configure(
            background="#2e2e2e",
            foreground="#ffffff",
            justify="center",
            text='creado por:\nLeonardo Sola\ny \nAgustín Bustos Piasentini\n\nhttps://www.Agustin-Bustos-Piasentini.com.ar/')
        Label_2.pack(expand=True, side="top")
        self.Cuits_xlsx = ttk.Button(Toplevel_1)
        self.Cuits_xlsx.configure(text='Abrir Excel con CUITs' , command=Abrir_Excel)
        self.Cuits_xlsx.pack(expand=True, pady=4, side="top")
        self.Cruzar = ttk.Button(Toplevel_1)
        self.Cruzar.configure(text='Cruzar', command=Cruzar)
        self.Cruzar.pack(expand=True, pady=4, side="top")
        self.Ver_Archivo = ttk.Button(Toplevel_1)
        self.Ver_Archivo.configure(text='Ver Resultado', command=Ver_Archivo)
        self.Ver_Archivo.pack(expand=True, padx=0, pady=4, side="top")
        self.LinkedIn_Leo = ttk.Button(Toplevel_1)
        self.LinkedIn_Leo.configure(text='LinkedIn de Leonardo' , command=LinkedIn_Leo)
        self.LinkedIn_Leo.pack(expand=True, pady=4, side="top")
        self.LindekIn_ABP = ttk.Button(Toplevel_1)
        self.LindekIn_ABP.configure(text='LinkedIn de Agustín', command=LinkedIn_ABP)
        self.LindekIn_ABP.pack(expand=True, pady=4, side="top")
        self.Colaboraciones = ttk.Button(Toplevel_1)
        self.Colaboraciones.configure(text='Colaboraciones', command=Cafecito)
        self.Colaboraciones.pack(expand=True, pady=4, side="top")

        # Main widget
        self.mainwindow = Toplevel_1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
