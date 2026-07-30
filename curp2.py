
import tkinter as tk
from tkinter import ttk

def datos():
    apellidoP = apellidoPtk.get()
    apellidoM = apellidoMtk.get()
    nombre = nombretk.get()
    genero = generotk.get()
    dia = diatk.get()
    mes = mestk.get()
    anio = aniotk.get()
    lugarNac = lugartk.get()

ventana = tk.Tk()  # Crea la ventana
ventana.title("Mi CURP")  # Título
ventana.geometry("600x400")   # Tamaño

tk.Label(ventana, text="porfavor ingresa tus datos para generar tu CURP").pack()  # Etiqueta


#==================================
#NOMBRE COMPLETO
#==================================

tk.Label(ventana, text="NOMBRE").place(x=360,y=40)  # Etiqueta


tk.Label(ventana, text="Ingresa tu primer apellido:").place(x=10, y=60)
apellidoPtk = tk.Entry(ventana)
apellidoPtk.place(x=200, y=60)  # Campo de entrada

tk.Label(ventana, text="Ingresa tu segundo apellido:").place(x=10, y=90)
apellidoMtk = tk.Entry(ventana)
apellidoMtk.place(x=200, y=90)  # Campo de entrada

tk.Label(ventana, text="Ingresa tu nombre:").place(x=10, y=120)
nombretk = tk.Entry(ventana)
nombretk.place(x=200, y=120)  # Campo de entrada

tk.Label(ventana, text="Ingresa tu genero:").place(x=10, y=150)
generotk = tk.Entry(ventana)
generotk.place(x=200, y=150)  # Campo de entrada


linea = ttk.Separator(ventana, orient='horizontal')
linea.pack(fill='x', pady=10)
#=================================
#FECHA DE NACIMIENTO
#==================================


tk.Label(ventana, text="FECHA DE NACIMIENTO").place(x=360,y=175)  # Etiqueta


#DIA
tk.Label(ventana, text="Ingresa tu dia de nacimiento:").place(x=10, y=210)
diatk = tk.Entry(ventana)
diatk.place(x=200, y=210) # Campo de entrada
#MES
tk.Label(ventana, text="Ingresa tu mes de nacimiento:").place(x=10, y=240)
mestk = tk.Entry(ventana)
mestk.place(x=200, y=240) # Campo de entrada
#AÑO
tk.Label(ventana, text="Ingresa tu año de nacimiento:").place(x=10, y=270)
aniotk = tk.Entry(ventana)
aniotk.place(x=200, y=270) # Campo de entrada
#LUGAR DE NACIMIENTO
ESTADOS_CURP = {
    "AGUASCALIENTES": "AS", "BAJA CALIFORNIA": "BC", "BAJA CALIFORNIA SUR": "BS",
    "CAMPECHE": "CC", "COAHUILA": "CL", "COLIMA": "CM", "CHIAPAS": "CS",
    "CHIHUAHUA": "CH", "CIUDAD DE MEXICO": "DF", "DURANGO": "DG",
    "GUANAJUATO": "GT", "GUERRERO": "GR", "HIDALGO": "HG", "JALISCO": "JC",
    "MEXICO": "MC", "MICHOACAN": "MN", "MORELOS": "MS", "NAYARIT": "NT",
    "NUEVO LEON": "NL", "OAXACA": "OC", "PUEBLA": "PL", "QUERETARO": "QT",
    "QUINTANA ROO": "QR", "SAN LUIS POTOSI": "SP", "SINALOA": "SL",
    "SONORA": "SR", "TABASCO": "TC", "TAMAULIPAS": "TS", "TLAXCALA": "TL",
    "VERACRUZ": "VZ", "YUCATAN": "YN", "ZACATECAS": "ZS",
    "NACIDO EN EL EXTRANJERO": "NE"
}

tk.Label(ventana, text="Lugar de nacimiento:").place(x=10, y=300)
lugartk = ttk.Combobox(ventana, values=list(ESTADOS_CURP.keys()), state="readonly", width=25)
lugartk.place(x=200, y=300) # Campo de entrada

tk.Button(ventana, text="GENERAR").place(x=10, y=340)

datos()




#curp = apellidoP[0:2] + apellidoM[0]+ nombre[0]+ dia + mes + anio + genero[0] + lugarNacimiento[0:3] + P14 + P15 + P16 + "00"




ventana.mainloop() 