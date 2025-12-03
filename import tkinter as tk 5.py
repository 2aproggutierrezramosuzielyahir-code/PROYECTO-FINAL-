import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# --- Datos simulados con arreglos ---
usuarios = [
    {"usuario": "Empleado de mostrador", "password": "1111", "rol": "Ventas en mostrador", "correo": "empleado@cuartodemilla.com"}
]

contactos = []  # Aquí se guardarán los mensajes del formulario

# Colores de estilo
COLOR_FONDO = "#f5f5dc"   # beige
COLOR_BOTON = "#8B4513"   # café
COLOR_TEXTO = "#3e2723"   # café oscuro

# --- Ventana de Login ---
def ventana_login():
    login_win = tk.Toplevel()
    login_win.title("Login")
    login_win.geometry("300x220")
    login_win.configure(bg=COLOR_FONDO)

    tk.Label(login_win, text="Usuario:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)
    usuario_entry = tk.Entry(login_win)
    usuario_entry.pack(pady=5)

    tk.Label(login_win, text="Contraseña:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)
    password_entry = tk.Entry(login_win, show="*")
    password_entry.pack(pady=5)

    def validar_login():
        usuario = usuario_entry.get()
        password = password_entry.get()
        for u in usuarios:
            if u["usuario"] == usuario and u["password"] == password:
                messagebox.showinfo("Acceso", f"Bienvenido {u['usuario']}")
                login_win.destroy()
                ventana_perfil(u)
                return
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    tk.Button(login_win, text="Ingresar", bg=COLOR_BOTON, fg="white", command=validar_login).pack(pady=10)
    tk.Button(login_win, text="Cerrar", bg=COLOR_BOTON, fg="white", command=login_win.destroy).pack(pady=5)

# --- Ventana de Contacto ---
def ventana_contacto():
    contacto_win = tk.Toplevel()
    contacto_win.title("Formulario de Contacto")
    contacto_win.geometry("400x350")
    contacto_win.configure(bg=COLOR_FONDO)

    tk.Label(contacto_win, text="Nombre:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)
    nombre_entry = tk.Entry(contacto_win)
    nombre_entry.pack(pady=5)

    tk.Label(contacto_win, text="Correo:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)
    correo_entry = tk.Entry(contacto_win)
    correo_entry.pack(pady=5)

    tk.Label(contacto_win, text="Mensaje:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)
    mensaje_entry = tk.Text(contacto_win, height=5, width=30)
    mensaje_entry.pack(pady=5)

    def enviar_formulario():
        nombre = nombre_entry.get()
        correo = correo_entry.get()
        mensaje = mensaje_entry.get("1.0", tk.END).strip()
        contactos.append({"nombre": nombre, "correo": correo, "mensaje": mensaje})
        messagebox.showinfo("Enviado", f"Gracias {nombre}, tu mensaje ha sido guardado en memoria.")

    tk.Button(contacto_win, text="Enviar", bg=COLOR_BOTON, fg="white", command=enviar_formulario).pack(pady=10)
    tk.Button(contacto_win, text="Cerrar", bg=COLOR_BOTON, fg="white", command=contacto_win.destroy).pack(pady=5)

# --- Ventana de Perfil con edición ---
def ventana_perfil(usuario):
    perfil_win = tk.Toplevel()
    perfil_win.title("Gestión de Perfil")
    perfil_win.geometry("400x300")
    perfil_win.configure(bg=COLOR_FONDO)

    tk.Label(perfil_win, text="Perfil del Usuario", font=("Arial", 14, "bold"), bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=10)

    # Mostrar datos actuales
    tk.Label(perfil_win, text=f"Nombre: {usuario['usuario']}", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)

    tk.Label(perfil_win, text="Rol:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)
    rol_entry = tk.Entry(perfil_win)
    rol_entry.insert(0, usuario["rol"])
    rol_entry.pack(pady=5)

    tk.Label(perfil_win, text="Correo:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)
    correo_entry = tk.Entry(perfil_win)
    correo_entry.insert(0, usuario["correo"])
    correo_entry.pack(pady=5)

    def guardar_cambios():
        usuario["rol"] = rol_entry.get()
        usuario["correo"] = correo_entry.get()
        messagebox.showinfo("Guardado", "Los cambios se han actualizado en el perfil.")

    tk.Button(perfil_win, text="Guardar Cambios", bg=COLOR_BOTON, fg="white", command=guardar_cambios).pack(pady=10)
    tk.Button(perfil_win, text="Cerrar", bg=COLOR_BOTON, fg="white", command=perfil_win.destroy).pack(pady=5)

# --- Ventana principal ---
def ventana_inicio():
    root = tk.Tk()
    root.title("CUARTO DE MILLA")
    root.geometry("600x500")
    root.configure(bg=COLOR_FONDO)

    # --- Logo ---
    try:
        logo_img = Image.open("logo.png.jpg")  # Reemplaza con tu archivo
        logo_img = logo_img.resize((150, 150))
        logo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(root, image=logo, bg=COLOR_FONDO)
        logo_label.image = logo
        logo_label.pack(pady=10)
    except Exception as e:
        tk.Label(root, text="(logo.png.jpg)", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=("Arial", 10)).pack(pady=10)

    # --- Título ---
    titulo = tk.Label(root, text="CUARTO DE MILLA", font=("Arial", 24, "bold"), bg=COLOR_FONDO, fg=COLOR_BOTON)
    titulo.pack(pady=10)

    # --- Info ---
    info = tk.Label(root, text="Tienda especializada en ropa vaquera\nCalidad y estilo para el campo y la ciudad",
                    font=("Arial", 12), bg=COLOR_FONDO, fg=COLOR_TEXTO)
    info.pack(pady=20)

    # --- Pie de página ---
    pie_frame = tk.Frame(root, bg=COLOR_BOTON)
    pie_frame.pack(side="bottom", fill="x")

    contacto = tk.Label(pie_frame, text="Tel: +52 222-123-4567 | WhatsApp: +52 222-987-6543",
                        font=("Arial", 10), fg="white", bg=COLOR_BOTON)
    contacto.pack(pady=2)

    redes = tk.Label(pie_frame, text="Facebook: @CuartoDeMilla | Instagram: @cuartodemilla_vaquero",
                     font=("Arial", 10), fg="white", bg=COLOR_BOTON)
    redes.pack(pady=2)

    # --- Menú hamburguesa ---
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    menu_hamburguesa = tk.Menu(menubar, tearoff=0, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    menubar.add_cascade(label="☰ Menú", menu=menu_hamburguesa)
    menu_hamburguesa.add_command(label="Login", command=ventana_login)
    menu_hamburguesa.add_command(label="Formulario de Contacto", command=ventana_contacto)
    menu_hamburguesa.add_command(label="Gestión de Perfil", command=lambda: ventana_perfil(usuarios[0]))

    root.mainloop()

# Ejecutar ventana
ventana_inicio()
