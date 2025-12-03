import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import webbrowser

# --- ARREGLOS EN MEMORIA ---
usuarios = [
    {"usuario": "Empleado de mostrador", "password": "1111", "rol": "Ventas en mostrador",
     "correo": "empleado@cuartodemilla.com", "foto": None}
]

contactos = []
productos = []

# --- COLORES Y FUENTES ---
COLOR_FONDO = "#f3d58e"
COLOR_BOTON = "#8B4513"
COLOR_TEXTO = "#3e2723"

FONT_TITULO = ("Arial", 30, "bold")   # <-- MÁS GRANDE
FONT_SUBTITULO = ("Arial", 22, "bold")
FONT_TEXTO = ("Arial", 14)
FONT_BOTON = ("Arial", 14, "bold")
FONT_MENU = ("Arial", 18, "bold")

def ventana_inicio():
    root = tk.Tk()
    root.title("CUARTO DE MILLA")
    root.geometry("1000x850")
    root.configure(bg=COLOR_FONDO)

    # ---------- ENCABEZADO ----------
    header_frame = tk.Frame(root, bg=COLOR_FONDO)
    header_frame.pack(fill="x", pady=10)

    try:
        logo_img = Image.open("logo.png.jpg")
        logo_img = logo_img.resize((150, 150))  # <-- LOGO MÁS GRANDE
        logo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(header_frame, image=logo, bg=COLOR_FONDO)
        logo_label.image = logo
        logo_label.pack(side="left", padx=20)
    except:
        tk.Label(header_frame, text="(logo)", font=FONT_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(side="left", padx=20)

    titulo = tk.Label(header_frame, text="CUARTO DE MILLA", font=("Arial", 42, "bold"),  # <-- TÍTULO MÁS GRANDE
                      bg=COLOR_FONDO, fg=COLOR_BOTON)
    titulo.pack(side="left", padx=60)

    # ---- LÍNEA SEPARADORA ----
    linea = tk.Frame(root, bg=COLOR_BOTON, height=4)
    linea.pack(fill="x", pady=5)

    # ---------- CONTENEDOR PRINCIPAL ----------
    main_frame = tk.Frame(root, bg=COLOR_FONDO)
    main_frame.pack(expand=True, fill="both")

    def mostrar_frame(funcion_frame):
        for widget in main_frame.winfo_children():
            widget.destroy()
        funcion_frame()

    # ---------- INICIO ----------
    def frame_inicio():
        titulo_inicio = tk.Label(
            main_frame,
            text="CUARTO DE MILLA",
            font=("Lucida Handwriting", 54, "bold"),  # <-- MÁS GRANDE Y BONITA
            bg=COLOR_FONDO,
            fg=COLOR_BOTON
        )
        titulo_inicio.pack(pady=60)

        subtitulo = tk.Label(
            main_frame,
            text="Tienda especializada en ropa vaquera\nCalidad y estilo para el campo y la ciudad",
            font=("Arial", 22),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            justify="center"
        )
        subtitulo.pack(pady=10)

    # ---------- LOGIN ----------
    def frame_login():
        tk.Label(main_frame, text="Usuario:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)
        usuario_entry = tk.Entry(main_frame, font=FONT_TEXTO)
        usuario_entry.pack(pady=5)

        tk.Label(main_frame, text="Contraseña:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)
        password_entry = tk.Entry(main_frame, show="*", font=FONT_TEXTO)
        password_entry.pack(pady=5)

        def validar():
            usuario = usuario_entry.get()
            password = password_entry.get()
            for u in usuarios:
                if u["usuario"] == usuario and u["password"] == password:
                    messagebox.showinfo("Bienvenido", usuario)
                    mostrar_frame(frame_perfil)
                    return
            messagebox.showerror("Error", "Credenciales incorrectas.")

        tk.Button(main_frame, text="Ingresar", bg=COLOR_BOTON, fg="white",
                  font=FONT_BOTON, width=15, height=2, command=validar).pack(pady=20)

    # ---------- CONTACTO ----------
    def frame_contacto():
        tk.Label(main_frame, text="Nombre:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)
        nombre = tk.Entry(main_frame, font=FONT_TEXTO)
        nombre.pack(pady=5)

        tk.Label(main_frame, text="Correo:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)
        correo = tk.Entry(main_frame, font=FONT_TEXTO)
        correo.pack(pady=5)

        tk.Label(main_frame, text="Mensaje:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=5)
        mensaje = tk.Text(main_frame, height=5, width=40, font=FONT_TEXTO)
        mensaje.pack(pady=5)

        def enviar():
            contactos.append({
                "nombre": nombre.get(),
                "correo": correo.get(),
                "mensaje": mensaje.get("1.0", tk.END)
            })
            messagebox.showinfo("Enviado", "Mensaje guardado.")

        tk.Button(main_frame, text="Enviar", bg=COLOR_BOTON, fg="white",
                  font=FONT_BOTON, width=15, height=2, command=enviar).pack(pady=20)

    # ---------- PERFIL ----------
    def frame_perfil():
        usuario = usuarios[0]

        tk.Label(main_frame, text="Perfil del Usuario", font=FONT_SUBTITULO,
                 bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=15)

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
                foto_label.config(text="Error al cargar foto", fg="red")

        def cambiar_foto():
            ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
            if ruta:
                usuario["foto"] = ruta
                img = Image.open(ruta)
                img = img.resize((150, 150))
                foto = ImageTk.PhotoImage(img)
                foto_label.config(image=foto)
                foto_label.image = foto

        tk.Button(main_frame, text="Cambiar Foto", bg=COLOR_BOTON, fg="white",
                  font=FONT_BOTON, width=20, height=2, command=cambiar_foto).pack(pady=10)

        tk.Label(main_frame, text=f"Nombre: {usuario['usuario']}", bg=COLOR_FONDO,
                 fg=COLOR_TEXTO, font=FONT_TEXTO).pack()

        tk.Label(main_frame, text=f"Correo: {usuario['correo']}", bg=COLOR_FONDO,
                 fg=COLOR_TEXTO, font=FONT_TEXTO).pack()

        tk.Label(main_frame, text=f"Rol: {usuario['rol']}", bg=COLOR_FONDO,
                 fg=COLOR_TEXTO, font=FONT_TEXTO).pack()

    # ---------- GESTIÓN DE PRODUCTOS ----------
    def frame_productos():

        def abrir_imagen(ruta):
            if not ruta:
                messagebox.showinfo("Imagen", "Este producto no tiene foto.")
                return
            ventana = tk.Toplevel()
            ventana.title("Imagen del Producto")
            img = Image.open(ruta)
            img = img.resize((400, 400))
            foto = ImageTk.PhotoImage(img)
            lbl = tk.Label(ventana, image=foto)
            lbl.image = foto
            lbl.pack()

        def actualizar_catalogo():
            for w in catalogo.winfo_children():
                w.destroy()
            if not productos:
                tk.Label(catalogo, text="No hay productos aún.", bg=COLOR_FONDO,
                         fg=COLOR_TEXTO, font=FONT_TEXTO).pack()
                return
            for idx, p in enumerate(productos):
                card = tk.Frame(catalogo, bg="#ecd9a3", bd=2, relief="solid", cursor="hand2")
                card.pack(pady=10, padx=10, fill="x")
                card.bind("<Button-1>", lambda e, ruta=p["foto"]: abrir_imagen(ruta))

                if p["foto"]:
                    try:
                        img = Image.open(p["foto"])
                        img = img.resize((100, 100))
                        imgTk = ImageTk.PhotoImage(img)
                        img_lbl = tk.Label(card, image=imgTk, bg="#ecd9a3")
                        img_lbl.image = imgTk
                        img_lbl.pack(side="left", padx=10)
                        img_lbl.bind("<Button-1>", lambda e, ruta=p["foto"]: abrir_imagen(ruta))
                    except:
                        pass

                info = tk.Frame(card, bg="#ecd9a3")
                info.pack(side="left", padx=10)

                nombre_label = tk.Label(info, text=f"Nombre: {p['nombre']}", bg="#ecd9a3",
                                        fg=COLOR_TEXTO, font=FONT_TEXTO)
                precio_label = tk.Label(info, text=f"Precio: ${p['precio']}", bg="#ecd9a3",
                                        fg=COLOR_TEXTO, font=FONT_TEXTO)
                nombre_label.pack(anchor="w")
                precio_label.pack(anchor="w")

                # Botón para eliminar
                tk.Button(card, text="Eliminar", bg="red", fg="white",
                          command=lambda i=idx: eliminar_producto(i)).pack(side="right", padx=10)

        def eliminar_producto(i):
            productos.pop(i)
            actualizar_catalogo()

        tk.Label(main_frame, text="Gestión de Productos", font=FONT_SUBTITULO,
                 bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=15)

        nombre = tk.Entry(main_frame, font=FONT_TEXTO)
        precio = tk.Entry(main_frame, font=FONT_TEXTO)

        tk.Label(main_frame, text="Nombre del producto:", bg=COLOR_FONDO,
                 fg=COLOR_TEXTO, font=FONT_TEXTO).pack()
        nombre.pack(pady=5)

        tk.Label(main_frame, text="Precio:", bg=COLOR_FONDO,
                 fg=COLOR_TEXTO, font=FONT_TEXTO).pack()
        precio.pack(pady=5)

        foto_label = tk.Label(main_frame, bg=COLOR_FONDO)
        foto_label.pack(pady=10)

        ruta_foto = {"path": None}

        def seleccionar():
            ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
            if ruta:
                ruta_foto["path"] = ruta
                img = Image.open(ruta)
                img = img.resize((130, 130))
                ft = ImageTk.PhotoImage(img)
                foto_label.config(image=ft)
                foto_label.image = ft

        tk.Button(main_frame, text="Agregar Foto del Producto", font=FONT_BOTON,
                  bg=COLOR_BOTON, fg="white", width=22, height=2,
                  command=seleccionar).pack(pady=10)

        def agregar():
            productos.append({
                "nombre": nombre.get(),
                "precio": precio.get(),
                "foto": ruta_foto["path"]
            })
            nombre.delete(0, tk.END)
            precio.delete(0, tk.END)
            ruta_foto["path"] = None
            foto_label.config(image="")
            actualizar_catalogo()
            messagebox.showinfo("Agregado", "Producto agregado correctamente.")

        tk.Button(main_frame, text="Agregar Producto", bg=COLOR_BOTON, fg="white",
                  font=FONT_BOTON, width=20, height=2, command=agregar).pack(pady=15)

        tk.Label(main_frame, text="Catálogo", font=FONT_SUBTITULO,
                 bg=COLOR_FONDO, fg=COLOR_TEXTO).pack()

        catalogo = tk.Frame(main_frame, bg=COLOR_FONDO)
        catalogo.pack(fill="both", expand=True)

        actualizar_catalogo()

    # ---------- ATENCIÓN AL CLIENTE ----------
    def frame_atencion_cliente():
        tk.Label(
            main_frame,
            text="Atención al Cliente",
            font=FONT_SUBTITULO,
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO
        ).pack(pady=20)

        tk.Label(
            main_frame,
            text="Estamos aquí para ayudarte.\nSelecciona una opción:",
            font=FONT_TEXTO,
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO
        ).pack(pady=10)

        opciones = [
            ("Problemas con un pedido", "Lamentamos los inconvenientes con tu pedido. Por favor contáctanos."),
            ("Devoluciones y cambios", "Para devoluciones, revisa nuestra política y contáctanos."),
            ("Seguimiento de envío", "Introduce tu número de pedido en nuestra página web para seguimiento."),
            ("Información de productos", "Puedes consultar nuestra sección de productos para más información."),
            ("Soporte en tienda", "Visítanos en nuestra tienda, estaremos encantados de ayudarte."),
            ("Atención por WhatsApp", "Abriendo WhatsApp para chatear con atención al cliente...")
        ]

        def accion(op):
            if op[0] == "Atención por WhatsApp":
                url = "https://wa.me/522229876543?text=Hola,%20necesito%20ayuda%20con%20mi%20pedido"
                webbrowser.open(url)
            else:
                messagebox.showinfo("Atención al Cliente", op[1])

        for texto, mensaje in opciones:
            tk.Button(
                main_frame,
                text=texto,
                font=FONT_BOTON,
                bg=COLOR_BOTON,
                fg="white",
                width=28,
                height=2,
                command=lambda t=texto, m=mensaje: accion((t, m))
            ).pack(pady=8)

        tk.Label(
            main_frame,
            text="Horario de atención:\nLunes a Sábado 10:00 AM – 8:00 PM",
            font=FONT_TEXTO,
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO
        ).pack(pady=20)

    # ---------- MENÚ HAMBURGUESA ----------
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    menu_hamburguesa = tk.Menu(menubar, tearoff=0, font=FONT_MENU)
    menubar.add_cascade(label="☰ MENÚ", menu=menu_hamburguesa)

    menu_hamburguesa.add_command(label="Inicio", command=lambda: mostrar_frame(frame_inicio))
    menu_hamburguesa.add_command(label="Login", command=lambda: mostrar_frame(frame_login))
    menu_hamburguesa.add_command(label="Contacto", command=lambda: mostrar_frame(frame_contacto))
    menu_hamburguesa.add_command(label="Gestión de Perfil", command=lambda: mostrar_frame(frame_perfil))
    menu_hamburguesa.add_command(label="Gestión de Productos", command=lambda: mostrar_frame(frame_productos))
    menu_hamburguesa.add_command(label="Atención al Cliente", command=lambda: mostrar_frame(frame_atencion_cliente))

    # ---------- PIE ----------
    pie = tk.Frame(root, bg=COLOR_BOTON)
    pie.pack(side="bottom", fill="x")

    tk.Label(pie, text="Tel: +52 2215 6805 63 | WhatsApp: +52 222 987 6543",
             font=FONT_TEXTO, bg=COLOR_BOTON, fg="white").pack()

    tk.Label(pie, text="Facebook: @CuartoDeMilla | Instagram: @cuartodemilla_vaquero",
             font=FONT_TEXTO, bg=COLOR_BOTON, fg="white").pack()

    mostrar_frame(frame_inicio)
    root.mainloop()

ventana_inicio()
