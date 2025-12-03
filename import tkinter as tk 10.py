import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

usuarios = [
    {"usuario": "Empleado de mostrador", "password": "1111", "rol": "Ventas en mostrador",
     "correo": "empleado@cuartodemilla.com", "foto": None}
]

contactos = []

COLOR_FONDO = "#f5f5dc"   # beige
COLOR_BOTON = "#8B4513"   # café
COLOR_TEXTO = "#3e2723"   # café oscuro


def ventana_inicio():
    root = tk.Tk()
    root.title("CUARTO DE MILLA")
    root.geometry("700x600")
    root.configure(bg=COLOR_FONDO)

    # --- Encabezado con logo y título ---
    header_frame = tk.Frame(root, bg=COLOR_FONDO)
    header_frame.pack(fill="x", pady=10)

    try:
        logo_img = Image.open("logo.png.jpg")  # Reemplaza con tu archivo
        logo_img = logo_img.resize((100, 100))
        logo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(header_frame, image=logo, bg=COLOR_FONDO)
        logo_label.image = logo
        logo_label.pack(side="left", padx=20)
    except Exception as e:
        tk.Label(header_frame, text="(logo.png.jpg)", bg=COLOR_FONDO, fg=COLOR_TEXTO,
                 font=("Arial", 10)).pack(side="left", padx=20)

    titulo = tk.Label(header_frame, text="CUARTO DE MILLA", font=("Arial", 24, "bold"),
                      bg=COLOR_FONDO, fg=COLOR_BOTON)
    titulo.pack(side="left", padx=20)

    # --- Contenedor dinámico ---
    main_frame = tk.Frame(root, bg=COLOR_FONDO)
    main_frame.pack(expand=True, fill="both")

    def mostrar_frame(frame):
        for widget in main_frame.winfo_children():
            widget.destroy()
        frame()

    # --- Pantalla de inicio ---
    def frame_inicio():
        tk.Label(main_frame, text="Tienda especializada en ropa vaquera\nCalidad y estilo para el campo y la ciudad",
                 font=("Arial", 12), bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=20)

    # --- Login ---
    def frame_login():
        tk.Label(main_frame, text="Usuario:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)
        usuario_entry = tk.Entry(main_frame)
        usuario_entry.pack(pady=5)

        tk.Label(main_frame, text="Contraseña:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)
        password_entry = tk.Entry(main_frame, show="*")
        password_entry.pack(pady=5)

        def validar_login():
            usuario = usuario_entry.get()
            password = password_entry.get()
            for u in usuarios:
                if u["usuario"] == usuario and u["password"] == password:
                    messagebox.showinfo("Acceso", f"Bienvenido {u['usuario']}")
                    mostrar_frame(frame_perfil)
                    return
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

        tk.Button(main_frame, text="Ingresar", bg=COLOR_BOTON, fg="white", command=validar_login).pack(pady=10)

    # --- Contacto ---
    def frame_contacto():
        tk.Label(main_frame, text="Nombre:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)
        nombre_entry = tk.Entry(main_frame)
        nombre_entry.pack(pady=5)

        tk.Label(main_frame, text="Correo:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)
        correo_entry = tk.Entry(main_frame)
        correo_entry.pack(pady=5)

        tk.Label(main_frame, text="Mensaje:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)
        mensaje_entry = tk.Text(main_frame, height=5, width=40)
        mensaje_entry.pack(pady=5)

        def enviar_formulario():
            nombre = nombre_entry.get()
            correo = correo_entry.get()
            mensaje = mensaje_entry.get("1.0", tk.END).strip()
            contactos.append({"nombre": nombre, "correo": correo, "mensaje": mensaje})
            messagebox.showinfo("Enviado", f"Gracias {nombre}, tu mensaje ha sido guardado en memoria.")

        tk.Button(main_frame, text="Enviar", bg=COLOR_BOTON, fg="white", command=enviar_formulario).pack(pady=10)

    # --- Perfil con foto ---
    def frame_perfil():
        usuario = usuarios[0]
        tk.Label(main_frame, text="Perfil del Usuario", font=("Arial", 14, "bold"),
                 bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=10)
        tk.Label(main_frame, text=f"Nombre: {usuario['usuario']}", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)

        foto_label = tk.Label(main_frame, bg=COLOR_FONDO)
        foto_label.pack(pady=10)

        if usuario["foto"]:
            try:
                img = Image.open(usuario["foto"])
                img = img.resize((120, 120))
                foto = ImageTk.PhotoImage(img)
                foto_label.config(image=foto)
                foto_label.image = foto
            except:
                foto_label.config(text="(Error al cargar foto)", fg="red")

        def seleccionar_foto():
            ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
            if ruta:
                usuario["foto"] = ruta
                img = Image.open(ruta)
                img = img.resize((120, 120))
                foto = ImageTk.PhotoImage(img)
                foto_label.config(image=foto)
                foto_label.image = foto
                messagebox.showinfo("Foto", "Foto de perfil actualizada.")

        tk.Button(main_frame, text="Agregar/Actualizar Foto", bg=COLOR_BOTON, fg="white",
                  command=seleccionar_foto).pack(pady=5)

        tk.Label(main_frame, text="Rol:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)
        rol_entry = tk.Entry(main_frame)
        rol_entry.insert(0, usuario["rol"])
        rol_entry.pack(pady=5)

        tk.Label(main_frame, text="Correo:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=5)
        correo_entry = tk.Entry(main_frame)
        correo_entry.insert(0, usuario["correo"])
        correo_entry.pack(pady=5)

        def guardar_cambios():
            usuario["rol"] = rol_entry.get()
            usuario["correo"] = correo_entry.get()
            messagebox.showinfo("Guardado", "Los cambios se han actualizado en el perfil.")

        tk.Button(main_frame, text="Guardar Cambios", bg=COLOR_BOTON, fg="white",
                  command=guardar_cambios).pack(pady=10)

    # --- Menú hamburguesa ---
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    menu_hamburguesa = tk.Menu(menubar, tearoff=0, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    menubar.add_cascade(label="☰ Menú", menu=menu_hamburguesa)
    menu_hamburguesa.add_command(label="Inicio", command=lambda: mostrar_frame(frame_inicio))
    menu_hamburguesa.add_command(label="Login", command=lambda: mostrar_frame(frame_login))
    menu_hamburguesa.add_command(label="Formulario de Contacto", command=lambda: mostrar_frame(frame_contacto))
    menu_hamburguesa.add_command(label="Gestión de Perfil", command=lambda: mostrar_frame(frame_perfil))

    # --- Pie de página ---
    pie_frame = tk.Frame(root, bg=COLOR_BOTON)
    pie_frame.pack(side="bottom", fill="x")

    contacto = tk.Label(pie_frame, text="Tel: +52 222-123-4567 | WhatsApp: +52 222-987-6543",
                        font=("Arial", 10), fg="white", bg=COLOR_BOTON)
    contacto.pack(pady=2)

    redes = tk.Label(pie_frame, text="Facebook: @CuartoDeMilla | Instagram: @cuartodemilla_vaquero",
                     font=("Arial", 10), fg="white", bg=COLOR_BOTON)
    redes.pack(pady=2)

    # Mostrar inicio por defecto
    mostrar_frame(frame_inicio)

    root.mainloop()


ventana_inicio()