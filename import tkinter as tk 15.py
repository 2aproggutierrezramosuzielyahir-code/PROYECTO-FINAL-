import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

usuarios = [
    {"usuario": "Empleado de mostrador", "password": "1111", "rol": "Ventas en mostrador",
     "correo": "empleado@cuartodemilla.com", "foto": None}
]

contactos = []
productos = []  # Lista donde se guardarán los productos

# COLORES
COLOR_FONDO = "#f3d58e"
COLOR_BOTON = "#8B4513"
COLOR_TEXTO = "#3e2723"

# FUENTES GRANDES
FONT_TITULO = ("Arial", 26, "bold")
FONT_SUBTITULO = ("Arial", 20, "bold")
FONT_TEXTO = ("Arial", 14)
FONT_BOTON = ("Arial", 14, "bold")


def ventana_inicio():
    root = tk.Tk()
    root.title("CUARTO DE MILLA")
    root.geometry("900x750")
    root.configure(bg=COLOR_FONDO)

    # ENCABEZADO
    header_frame = tk.Frame(root, bg=COLOR_FONDO)
    header_frame.pack(fill="x", pady=10)

    try:
        logo_img = Image.open("logo.png.jpg")
        logo_img = logo_img.resize((110, 110))
        logo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(header_frame, image=logo, bg=COLOR_FONDO)
        logo_label.image = logo
        logo_label.pack(side="left", padx=20)
    except:
        tk.Label(header_frame, text="(logo)", bg=COLOR_FONDO, fg=COLOR_TEXTO,
                 font=("Arial", 12)).pack(side="left", padx=20)

    titulo = tk.Label(header_frame, text="CUARTO DE MILLA", font=FONT_TITULO,
                      bg=COLOR_FONDO, fg=COLOR_BOTON)
    titulo.pack(side="left", padx=20)

    # CONTENEDOR PRINCIPAL
    main_frame = tk.Frame(root, bg=COLOR_FONDO)
    main_frame.pack(expand=True, fill="both")

    def mostrar_frame(frame):
        for widget in main_frame.winfo_children():
            widget.destroy()
        frame()

    # ------------ PANTALLAS EXISTENTES ------------

    def frame_inicio():
        tk.Label(main_frame,
                 text="Tienda especializada en ropa vaquera\nCalidad y estilo para el campo y la ciudad",
                 font=FONT_SUBTITULO, bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=40)

    def frame_login():
        tk.Label(main_frame, text="Usuario:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)
        usuario_entry = tk.Entry(main_frame, font=FONT_TEXTO)
        usuario_entry.pack(pady=5)

        tk.Label(main_frame, text="Contraseña:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)
        password_entry = tk.Entry(main_frame, show="*", font=FONT_TEXTO)
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

        tk.Button(main_frame, text="Ingresar", bg=COLOR_BOTON, fg="white",
                  font=FONT_BOTON, width=15, height=2,
                  command=validar_login).pack(pady=20)

    def frame_contacto():
        tk.Label(main_frame, text="Nombre:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)
        nombre_entry = tk.Entry(main_frame, font=FONT_TEXTO)
        nombre_entry.pack(pady=5)

        tk.Label(main_frame, text="Correo:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)
        correo_entry = tk.Entry(main_frame, font=FONT_TEXTO)
        correo_entry.pack(pady=5)

        tk.Label(main_frame, text="Mensaje:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)
        mensaje_entry = tk.Text(main_frame, height=6, width=45, font=FONT_TEXTO)
        mensaje_entry.pack(pady=5)

        def enviar_formulario():
            nombre = nombre_entry.get()
            correo = correo_entry.get()
            mensaje = mensaje_entry.get("1.0", tk.END).strip()
            contactos.append({"nombre": nombre, "correo": correo, "mensaje": mensaje})
            messagebox.showinfo("Enviado", f"Gracias {nombre}, tu mensaje ha sido guardado.")

        tk.Button(main_frame, text="Enviar", bg=COLOR_BOTON, fg="white",
                  font=FONT_BOTON, width=15, height=2, command=enviar_formulario).pack(pady=20)

    def frame_perfil():
        usuario = usuarios[0]

        tk.Label(main_frame, text="Perfil del Usuario", font=FONT_SUBTITULO,
                 bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=15)

        tk.Label(main_frame, text=f"Nombre: {usuario['usuario']}", bg=COLOR_FONDO,
                 fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)

        foto_label = tk.Label(main_frame, bg=COLOR_FONDO)
        foto_label.pack(pady=10)

        if usuario["foto"]:
            try:
                img = Image.open(usuario["foto"])
                img = img.resize((150, 150))
                foto = ImageTk.PhotoImage(img)
                foto_label.config(image=foto)
                foto_label.image = foto
            except:
                foto_label.config(text="Error al cargar foto", fg="red", font=FONT_TEXTO)

        def seleccionar_foto():
            ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
            if ruta:
                usuario["foto"] = ruta
                img = Image.open(ruta)
                img = img.resize((150, 150))
                foto = ImageTk.PhotoImage(img)
                foto_label.config(image=foto)
                foto_label.image = foto
                messagebox.showinfo("Foto", "Foto actualizada.")

        tk.Button(main_frame, text="Agregar/Actualizar Foto", font=FONT_BOTON,
                  bg=COLOR_BOTON, fg="white", width=22, height=2,
                  command=seleccionar_foto).pack(pady=10)

        tk.Label(main_frame, text="Rol:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)
        rol_entry = tk.Entry(main_frame, font=FONT_TEXTO)
        rol_entry.insert(0, usuario["rol"])
        rol_entry.pack(pady=5)

        tk.Label(main_frame, text="Correo:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)
        correo_entry = tk.Entry(main_frame, font=FONT_TEXTO)
        correo_entry.insert(0, usuario["correo"])
        correo_entry.pack(pady=5)

        def guardar_cambios():
            usuario["rol"] = rol_entry.get()
            usuario["correo"] = correo_entry.get()
            messagebox.showinfo("Guardado", "Los cambios se han guardado.")

        tk.Button(main_frame, text="Guardar Cambios", bg=COLOR_BOTON, fg="white",
                  font=FONT_BOTON, width=20, height=2,
                  command=guardar_cambios).pack(pady=20)

    # ------------ GESTIÓN DE PRODUCTOS ------------
    def frame_productos():

        def actualizar_catalogo():
            for widget in catalogo_frame.winfo_children():
                widget.destroy()

            if not productos:
                tk.Label(catalogo_frame, text="No hay productos agregados.",
                         font=FONT_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=20)
                return

            for p in productos:
                card = tk.Frame(catalogo_frame, bg="#f5deb3", bd=2, relief="solid")
                card.pack(pady=10, padx=10, fill="x")

                # Foto
                if p["foto"]:
                    try:
                        img = Image.open(p["foto"])
                        img = img.resize((100, 100))
                        img_tk = ImageTk.PhotoImage(img)
                        img_label = tk.Label(card, image=img_tk, bg="#f5deb3")
                        img_label.image = img_tk
                        img_label.pack(side="left", padx=10)
                    except:
                        tk.Label(card, text="Foto no disponible", bg="#f5deb3",
                                 fg="red", font=FONT_TEXTO).pack(side="left", padx=10)
                else:
                    tk.Label(card, text="Sin foto", bg="#f5deb3",
                             fg="gray", font=FONT_TEXTO).pack(side="left", padx=10)

                info = tk.Frame(card, bg="#f5deb3")
                info.pack(side="left", padx=10)

                tk.Label(info, text=f"Nombre: {p['nombre']}", bg="#f5deb3",
                         fg=COLOR_TEXTO, font=FONT_TEXTO).pack(anchor="w")
                tk.Label(info, text=f"Precio: ${p['precio']}", bg="#f5deb3",
                         fg=COLOR_TEXTO, font=FONT_TEXTO).pack(anchor="w")

        tk.Label(main_frame, text="Gestión de Productos", font=FONT_SUBTITULO,
                 bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=10)

        # Campos
        tk.Label(main_frame, text="Nombre del producto:", bg=COLOR_FONDO,
                 fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)
        nombre_entry = tk.Entry(main_frame, font=FONT_TEXTO)
        nombre_entry.pack(pady=5)

        tk.Label(main_frame, text="Precio:", bg=COLOR_FONDO,
                 fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)
        precio_entry = tk.Entry(main_frame, font=FONT_TEXTO)
        precio_entry.pack(pady=5)

        foto_label = tk.Label(main_frame, bg=COLOR_FONDO)
        foto_label.pack(pady=10)
        ruta_foto = {"path": None}

        def seleccionar_foto_producto():
            ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
            if ruta:
                ruta_foto["path"] = ruta
                img = Image.open(ruta)
                img = img.resize((130, 130))
                foto = ImageTk.PhotoImage(img)
                foto_label.config(image=foto)
                foto_label.image = foto

        tk.Button(main_frame, text="Agregar Foto del Producto", font=FONT_BOTON,
                  bg=COLOR_BOTON, fg="white", width=22, height=2,
                  command=seleccionar_foto_producto).pack(pady=5)

        # Botón AGREGAR
        def agregar_producto():
            nombre = nombre_entry.get()
            precio = precio_entry.get()

            if not nombre or not precio:
                messagebox.showerror("Error", "Debes llenar todos los campos.")
                return

            productos.append({
                "nombre": nombre,
                "precio": precio,
                "foto": ruta_foto["path"]
            })

            nombre_entry.delete(0, tk.END)
            precio_entry.delete(0, tk.END)
            ruta_foto["path"] = None
            foto_label.config(image="")

            actualizar_catalogo()
            messagebox.showinfo("Agregado", "Producto agregado correctamente.")

        tk.Button(main_frame, text="Agregar Producto", bg=COLOR_BOTON,
                  fg="white", font=FONT_BOTON, width=20, height=2,
                  command=agregar_producto).pack(pady=10)

        tk.Label(main_frame, text="Catálogo de Productos", font=FONT_SUBTITULO,
                 bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=10)

        catalogo_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        catalogo_frame.pack(fill="both", expand=True)

        actualizar_catalogo()

    # ------------ MENÚ HAMBURGUESA ------------
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    menu_hamburguesa = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="☰ Menú", menu=menu_hamburguesa)

    menu_hamburguesa.add_command(label="Inicio", command=lambda: mostrar_frame(frame_inicio))
    menu_hamburguesa.add_command(label="Login", command=lambda: mostrar_frame(frame_login))
    menu_hamburguesa.add_command(label="Formulario de Contacto", command=lambda: mostrar_frame(frame_contacto))
    menu_hamburguesa.add_command(label="Gestión de Perfil", command=lambda: mostrar_frame(frame_perfil))
    menu_hamburguesa.add_command(label="Gestión de Productos", command=lambda: mostrar_frame(frame_productos))

    # PIE DE PÁGINA
    pie_frame = tk.Frame(root, bg=COLOR_BOTON)
    pie_frame.pack(side="bottom", fill="x")

    contacto = tk.Label(pie_frame,
                        text="Tel: +52 2215 6805 63 | WhatsApp: +52 222-987-6543",
                        font=("Arial", 14), fg="white", bg=COLOR_BOTON)
    contacto.pack(pady=2)

    redes = tk.Label(pie_frame,
                     text="Facebook: @CuartoDeMilla | Instagram: @cuartodemilla_vaquero",
                     font=("Arial", 14), fg="white", bg=COLOR_BOTON)
    redes.pack(pady=2)

    mostrar_frame(frame_inicio)
    root.mainloop()


ventana_inicio()
