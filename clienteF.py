import socket
import tkinter as tk

def enviar_comando(comando):
    # Función para enviar el comando al servidor
    client.send(comando.encode())

def toggle_color(btn):
    # Función para alternar el color del botón
    if btn['bg'] == 'green':
        btn.config(bg='red')
    else:
        btn.config(bg='green')

# Configuración de la interfaz gráfica
root = tk.Tk()
root.configure(bg='yellow')

root.title("Cliente para enviar comandos")

frame = tk.Frame(root)
frame.pack(padx=40, pady=40)

commands = {
    "Encender/Apagar el Bomba Manual": "TOGGLE_LED_MANUAL",
    "Encender/Apagar el Ventilador Manual": "TOGGLE_VENTILADOR_MANUAL",
    "Encender/Apagar las Luces Manual": "TOGGLE_LUCES_MANUAL",
    "Secuencia Automática": "TOGGLE_SECUENCIA",
    "Actualizar Valores de los Sensores": "REFRESH_SENSORES",
    "ABRIR PUERTA": "GIRAR_HORARIO",
    "CERRAR PUERTA": "GIRAR_ANTIHORARIO"
    
}

buttons = []
for label, command in commands.items():
    btn = tk.Button(frame, text=label, command=lambda cmd=command: enviar_comando(cmd))
    btn.pack(pady=9)
    btn.config(width=40, bg='red')  # Dimensión y color inicial del botón
    btn.bind('<Button-1>', lambda event, b=btn: toggle_color(b))  # Cambio de color al hacer clic
    buttons.append(btn)

# Conexión al servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.100.47', 5555))  # Reemplaza 'dirección_ip_servidor' por la IP del servidor

root.mainloop()