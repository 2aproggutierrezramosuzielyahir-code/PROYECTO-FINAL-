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

FONT_TITULO = ("Arial", 30, "bold")
FONT_SUBTITULO = ("Arial", 22, "bold")
FONT_TEXTO = ("Arial", 14)
FONT_BOTON = ("Arial", 14, "bold")
FONT_MENU = ("Arial", 18, "bold")


def ventana_inicio():
    root = tk.Tk()
    root.title("CUARTO DE MILLA")
    root.geometry("1130x650")   # ← VENTANA MÁS GRANDE
    root.configure(bg=COLOR_FONDO)

    # ------------ CONTENEDOR PRINCIPAL ------------
    main_container = tk.Frame(root, bg=COLOR_FONDO)
    main_container.pack(fill="both", expand=True)

    # ------------ ENCABEZADO ------------
    header_frame = tk.Frame(main_container, bg=COLOR_FONDO)
    header_frame.pack(fill="x", pady=10)

    try:
        logo_img = Image.open("logo.png.jpg")
        logo_img = logo_img.resize((130, 130))
        logo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(header_frame, image=logo, bg=COLOR_FONDO)
        logo_label.image = logo
        logo_label.pack(side="left", padx=20)
    except:
        tk.Label(header_frame, text="(logo)", font=FONT_TEXTO,
                 bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(side="left", padx=20)

    titulo = tk.Label(
        header_frame,
        text="CUARTO DE MILLA",
        font=("Arial", 40, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_BOTON
    )
    titulo.pack(side="left", padx=100)

    linea = tk.Frame(main_container, bg=COLOR_BOTON, height=4)
    linea.pack(fill="x", pady=5)

    # ------------ ZONA DE CONTENIDO ------------
    main_frame = tk.Frame(main_container, bg=COLOR_FONDO)
    main_frame.pack(fill="both", expand=True)

    # ------------ PIE DE PÁGINA ------------
    pie = tk.Frame(main_container, bg=COLOR_BOTON)
    pie.pack(fill="x")
    pie_visible = True

    tk.Label(pie, text="Tel: +52 2215 6805 63 | WhatsApp: +52 222 987 6543",
             font=FONT_TEXTO, bg=COLOR_BOTON, fg="white").pack()

    tk.Label(pie, text="Facebook: @CuartoDeMilla | Instagram: @cuartodemilla_vaquero",
             font=FONT_TEXTO, bg=COLOR_BOTON, fg="white").pack()

    # ------------ FUNCIÓN CAMBIAR PANTALLAS ------------
    def mostrar_frame(frame_func, mostrar_pie=False):
        nonlocal pie_visible

        for w in main_frame.winfo_children():
            w.destroy()

        frame_func()

        if mostrar_pie:
            if not pie_visible:
                pie.pack(fill="x")
                pie_visible = True
        else:
            if pie_visible:
                pie.pack_forget()
                pie_visible = False

    # =========================================================
    #                       FRAMES
    # =========================================================

    def frame_inicio():
        tk.Label(
            main_frame,
            text="CUARTO DE MILLA",
            font=("Lucida Handwriting", 48, "bold"),
            bg=COLOR_FONDO,
            fg=COLOR_BOTON
        ).pack(pady=20)

        tk.Label(
            main_frame,
            text="Tienda especializada en ropa vaquera\nCalidad y estilo para el campo y la ciudad",
            font=("Arial", 15),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO
        ).pack(pady=10)

        info = "✔ Cuarto de milla ofrece una gran variedad de artículos enfocados a las necesidades de los vaqueros."

        tk.Label(
            main_frame,
            text=info,
            font=("Arial", 18),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            justify="center"
        ).pack(pady=20)

        tk.Label(
            main_frame,
            text="“Cuarto de Milla — Tradición, estilo y pasión por lo vaquero.”",
            font=("Arial", 18, "italic"),
            bg=COLOR_FONDO,
            fg=COLOR_BOTON
        ).pack(pady=10)

    # LOGIN
    def frame_login():
        tk.Label(main_frame, text="Usuario:", font=FONT_TEXTO, bg=COLOR_FONDO).pack(pady=5)
        usuario_entry = tk.Entry(main_frame, font=FONT_TEXTO)
        usuario_entry.pack(pady=5)

        tk.Label(main_frame, text="Contraseña:", font=FONT_TEXTO, bg=COLOR_FONDO).pack(pady=5)
        password_entry = tk.Entry(main_frame, font=FONT_TEXTO, show="*")
        password_entry.pack(pady=5)

        def validar():
            for u in usuarios:
                if usuario_entry.get() == u["usuario"] and password_entry.get() == u["password"]:
                    messagebox.showinfo("Acceso", "Bienvenido")
                    mostrar_frame(frame_perfil)
                    return
            messagebox.showerror("Error", "Credenciales incorrectas")

        tk.Button(main_frame, text="Ingresar", width=15, height=2,
                  bg=COLOR_BOTON, fg="white", font=FONT_BOTON,
                  command=validar).pack(pady=20)

    # CONTACTO
    def frame_contacto():
        tk.Label(main_frame, text="Nombre:", font=FONT_TEXTO, bg=COLOR_FONDO).pack(pady=5)
        nombre = tk.Entry(main_frame, font=FONT_TEXTO)
        nombre.pack(pady=5)

        tk.Label(main_frame, text="Correo:", font=FONT_TEXTO, bg=COLOR_FONDO).pack(pady=5)
        correo = tk.Entry(main_frame, font=FONT_TEXTO)
        correo.pack(pady=5)

        tk.Label(main_frame, text="Mensaje:", font=FONT_TEXTO, bg=COLOR_FONDO).pack(pady=5)
        mensaje = tk.Text(main_frame, width=40, height=5, font=FONT_TEXTO)
        mensaje.pack(pady=5)

        def enviar():
            contactos.append({
                "nombre": nombre.get(),
                "correo": correo.get(),
                "mensaje": mensaje.get("1.0", tk.END)
            })
            messagebox.showinfo("Éxito", "Mensaje enviado")

        tk.Button(main_frame, text="Enviar", bg=COLOR_BOTON, fg="white",
                  width=15, height=2, font=FONT_BOTON, command=enviar).pack(pady=20)

    # PERFIL
    def frame_perfil():
        usuario = usuarios[0]

        tk.Label(main_frame, text="Gestión de Perfil", font=FONT_SUBTITULO,
                 bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=15)

        foto_label = tk.Label(main_frame, bg=COLOR_FONDO)
        foto_label.pack(pady=10)

        if usuario["foto"]:
            img = Image.open(usuario["foto"])
            img = img.resize((150, 150))
            foto = ImageTk.PhotoImage(img)
            foto_label.config(image=foto)
            foto_label.image = foto

        def cambiar_foto():
            ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg")])
            if ruta:
                usuario["foto"] = ruta
                img = Image.open(ruta)
                img = img.resize((150, 150))
                foto = ImageTk.PhotoImage(img)
                foto_label.config(image=foto)
                foto_label.image = foto

        tk.Button(main_frame, text="Cambiar Foto", width=18, height=2,
                  bg=COLOR_BOTON, fg="white", font=FONT_BOTON,
                  command=cambiar_foto).pack(pady=10)

        tk.Label(main_frame, text="Nombre:", bg=COLOR_FONDO, font=FONT_TEXTO).pack()
        nombre_entry = tk.Entry(main_frame, font=FONT_TEXTO)
        nombre_entry.insert(0, usuario["usuario"])
        nombre_entry.pack(pady=5)

        tk.Label(main_frame, text="Correo:", bg=COLOR_FONDO, font=FONT_TEXTO).pack()
        correo_entry = tk.Entry(main_frame, font=FONT_TEXTO)
        correo_entry.insert(0, usuario["correo"])
        correo_entry.pack(pady=5)

        tk.Label(main_frame, text="Rol:", bg=COLOR_FONDO, font=FONT_TEXTO).pack()
        rol_entry = tk.Entry(main_frame, font=FONT_TEXTO)
        rol_entry.insert(0, usuario["rol"])
        rol_entry.pack(pady=5)

        def guardar_cambios():
            usuario["usuario"] = nombre_entry.get()
            usuario["correo"] = correo_entry.get()
            usuario["rol"] = rol_entry.get()
            messagebox.showinfo("Éxito", "Datos actualizados")

        tk.Button(main_frame, text="Guardar Cambios", bg=COLOR_BOTON, fg="white",
                  width=18, height=2, font=FONT_BOTON,
                  command=guardar_cambios).pack(pady=15)

    # ============================================================
    #                 GESTIÓN DE PRODUCTOS (CENTRADO + SCROLL)
    # ============================================================
    def frame_productos():

        contenedor = tk.Frame(main_frame, bg=COLOR_FONDO)
        contenedor.pack(expand=True)

        tk.Label(contenedor, text="Gestión de Productos",
                 font=FONT_SUBTITULO, bg=COLOR_FONDO).pack(pady=15)

        form = tk.Frame(contenedor, bg=COLOR_FONDO)
        form.pack(anchor="center")

        tk.Label(form, text="Nombre:", bg=COLOR_FONDO, font=FONT_TEXTO).pack()
        nombre = tk.Entry(form, font=FONT_TEXTO)
        nombre.pack(pady=5)

        tk.Label(form, text="Precio:", bg=COLOR_FONDO, font=FONT_TEXTO).pack()
        precio = tk.Entry(form, font=FONT_TEXTO)
        precio.pack(pady=5)

        foto_label = tk.Label(form, bg=COLOR_FONDO)
        foto_label.pack(pady=5)

        ruta_foto = {"path": None}

        def seleccionar():
            ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg")])
            if ruta:
                ruta_foto["path"] = ruta
                img = Image.open(ruta)
                img = img.resize((120, 120))
                imgTk = ImageTk.PhotoImage(img)
                foto_label.config(image=imgTk)
                foto_label.image = imgTk

        tk.Button(form, text="Agregar Foto", bg=COLOR_BOTON,
                  fg="white", width=15, height=2, font=FONT_BOTON,
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
            actualizar()

        tk.Button(form, text="Agregar Producto", bg=COLOR_BOTON,
                  fg="white", width=18, height=2, font=FONT_BOTON,
                  command=agregar).pack(pady=15)

        tk.Label(contenedor, text="Catálogo", font=FONT_SUBTITULO,
                 bg=COLOR_FONDO).pack(pady=10)

        # SCROLL SOLO AQUÍ
        canvas = tk.Canvas(contenedor, bg=COLOR_FONDO, highlightthickness=0)
        scrollbar = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, padx=40)
        scrollbar.pack(side="right", fill="y")

        catalogo = tk.Frame(canvas, bg=COLOR_FONDO)
        canvas.create_window((0, 0), window=catalogo, anchor="n")

        def actualizar():
            for w in catalogo.winfo_children():
                w.destroy()

            if not productos:
                tk.Label(catalogo, text="No hay productos.", bg=COLOR_FONDO,
                         font=FONT_TEXTO).pack(anchor="center", pady=10)
                return

            for i, p in enumerate(productos):
                card = tk.Frame(catalogo, bg="#ecd9a3", bd=2, relief="solid")
                card.pack(pady=10, padx=10, fill="x")

                if p["foto"]:
                    img = Image.open(p["foto"])
                    img = img.resize((90, 90))
                    imgTk = ImageTk.PhotoImage(img)
                    img_lbl = tk.Label(card, image=imgTk, bg="#ecd9a3")
                    img_lbl.image = imgTk
                    img_lbl.pack(side="left", padx=10)

                info = tk.Frame(card, bg="#ecd9a3")
                info.pack(side="left")

                tk.Label(info, text=f"Nombre: {p['nombre']}",
                         font=FONT_TEXTO, bg="#ecd9a3").pack(anchor="w")
                tk.Label(info, text=f"Precio: ${p['precio']}",
                         font=FONT_TEXTO, bg="#ecd9a3").pack(anchor="w")

                tk.Button(card, text="Eliminar", bg="red", fg="white",
                          command=lambda x=i: eliminar(x)).pack(side="right", padx=10)

            catalogo.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox("all"))

        def eliminar(i):
            productos.pop(i)
            actualizar()

        catalogo.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        actualizar()

    # ============================================================
    #             ATENCIÓN AL CLIENTE
    # ============================================================
    def frame_atencion():
        tk.Label(main_frame, text="Atención al Cliente",
                 font=FONT_SUBTITULO, bg=COLOR_FONDO).pack(pady=20)

        opciones = [
            ("Problemas con un pedido", "Lamentamos los inconvenientes."),
            ("Devoluciones", "Consulta nuestra política de cambios."),
            ("Seguimiento de envío", "Revisa tu número de guía."),
            ("Información de productos", "Consulta la sección de productos."),
            ("Soporte en tienda", "Visítanos en nuestro local."),
            ("WhatsApp", "Abriendo WhatsApp…")
        ]

        def accion(t, m):
            if t == "WhatsApp":
                webbrowser.open("https://wa.me/522229876543")
                return
            messagebox.showinfo(t, m)

        for t, m in opciones:
            tk.Button(main_frame, text=t, bg=COLOR_BOTON, fg="white",
                      width=25, height=2, font=FONT_BOTON,
                      command=lambda x=t, y=m: accion(x, y)).pack(pady=8)

    # ============================================================
    # MENÚ
    # ============================================================
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    menu = tk.Menu(menubar, tearoff=0, font=FONT_MENU)
    menubar.add_cascade(label="☰ MENÚ", menu=menu)

    menu.add_command(label="Inicio", command=lambda: mostrar_frame(frame_inicio, mostrar_pie=True))
    menu.add_command(label="Login", command=lambda: mostrar_frame(frame_login))
    menu.add_command(label="Contacto", command=lambda: mostrar_frame(frame_contacto))
    menu.add_command(label="Gestión de Perfil", command=lambda: mostrar_frame(frame_perfil))
    menu.add_command(label="Gestión de Productos", command=lambda: mostrar_frame(frame_productos))
    menu.add_command(label="Atención al Cliente", command=lambda: mostrar_frame(frame_atencion))

    mostrar_frame(frame_inicio, mostrar_pie=True)

    root.mainloop()


ventana_inicio()
