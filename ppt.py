import random
import tkinter as tk
from tkinter import messagebox

# Configuración de la ventana principal

# ventana principal
ventana_principal = tk.Tk()

# titulo
ventana_principal.title("Sistemas Guanenta")

# tamaño de la ventana
ventana_principal.geometry("500x520")

# color de fondo
ventana_principal.configure(bg="black")

ventana_principal.resizable(0, 0)

# cargar imágenes
try:
    imagen_piedra = tk.PhotoImage(file="img/piedra.png")
    imagen_papel = tk.PhotoImage(file="img/papel.png")
    imagen_tijera = tk.PhotoImage(file="img/tijera.png")
    imagen_piedra_btn = imagen_piedra.subsample(7, 7)
    imagen_papel_btn = imagen_papel.subsample(7, 7)
    imagen_tijera_btn = imagen_tijera.subsample(7, 7)
except tk.TclError as e:
    messagebox.showerror("Error", f"No se pudo cargar las imágenes: {e}")
    ventana_principal.destroy()
    raise SystemExit

# frame para los campos de entrada
frame_input = tk.Frame(ventana_principal, bg="#696969", width=480, height=120)
frame_input.place(x=10, y=10)

# etiquetas y campos de entrada
tk.Label(frame_input, text="Piedra, Papel o Tijera", bg="#696969", fg="black", font=("Arial", 16, "bold")).place(x=20, y=15)
tk.Label(frame_input, text="TERMINAL ENGINE v2.4", bg="#696969", fg="black", font=("Arial", 10)).place(x=20, y=45)

score_usuario = 0
score_computadora = 0
score_text = tk.Text(frame_input, width=28, height=3, bg="#dcdcdc", fg="black", font=("Arial", 12, "bold"), bd=2, relief="ridge")
score_text.place(x=20, y=75)
score_text.insert("1.0", f"Puntos:\nTú {score_usuario}\nPC {score_computadora}")
score_text.config(state="disabled")

# frame para los resultados
frame_results = tk.Frame(ventana_principal, bg="#696969", width=480, height=240)
frame_results.place(x=10, y=140)

resultado_label = tk.Label(frame_results, text="Elige una opción", bg="#696969", fg="black", font=("Arial", 14, "bold"), justify="left")
resultado_label.place(x=20, y=20)

imagen_label = tk.Label(frame_results, bg="#696969")
imagen_label.place(x=160, y=80)

# función de juego
def jugar(opcion_usuario):
    global score_usuario, score_computadora
    opciones = ["piedra", "papel", "tijera"]
    opcion_computadora = random.choice(opciones)

    if opcion_usuario == opcion_computadora:
        resultado = "Empate"
    elif (opcion_usuario == "piedra" and opcion_computadora == "tijera") or \
         (opcion_usuario == "papel" and opcion_computadora == "piedra") or \
         (opcion_usuario == "tijera" and opcion_computadora == "papel"):
        resultado = "Ganaste"
        score_usuario += 1
    else:
        resultado = "Perdiste"
        score_computadora += 1

    score_text.config(state="normal")
    score_text.delete("1.0", "end")
    score_text.insert("1.0", f"Puntos:\nTú {score_usuario}\nPC {score_computadora}")
    score_text.config(state="disabled")

    texto = f"Tú elegiste: {opcion_usuario.capitalize()}\nComputadora: {opcion_computadora.capitalize()}\n{resultado}"
    resultado_label.config(text=texto)

    imagenes = {"piedra": imagen_piedra, "papel": imagen_papel, "tijera": imagen_tijera}
    imagen_actual = imagenes[opcion_usuario]
    imagen_label.config(image=imagen_actual)
    imagen_label.image = imagen_actual

# frame para los botones
frame_buttons = tk.Frame(ventana_principal, bg="#696969", width=480, height=120)
frame_buttons.place(x=10, y=390)

# boton para piedra
btn_piedra = tk.Button(frame_buttons, text="Piedra", image=imagen_piedra_btn, compound="top", bg="#4CAF50", fg="black", font=("Arial", 12, "bold"), width=100, height=90, command=lambda: jugar("piedra"))
btn_piedra.place(x=20, y=10)

# boton para papel
btn_papel = tk.Button(frame_buttons, text="Papel", image=imagen_papel_btn, compound="top", bg="#f44336", fg="black", font=("Arial", 12, "bold"), width=100, height=90, command=lambda: jugar("papel"))
btn_papel.place(x=180, y=10)

# boton para tijera
btn_tijera = tk.Button(frame_buttons, text="Tijera", image=imagen_tijera_btn, compound="top", bg="#2196F3", fg="black", font=("Arial", 12, "bold"), width=100, height=90, command=lambda: jugar("tijera"))
btn_tijera.place(x=340, y=10)

# bucle principal
ventana_principal.mainloop()