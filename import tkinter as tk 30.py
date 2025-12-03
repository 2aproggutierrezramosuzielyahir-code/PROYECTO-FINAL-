import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import webbrowser
from datetime import datetime
import os

# --- ARREGLOS EN MEMORIA ---
usuarios = [
    {"usuario": "Empleado de mostrador", "password": "1111", "rol": "Ventas en mostrador",
     "correo": "empleado@cuartodemilla.com", "foto": None}
]

contactos = []
productos = []
ventas = []

# NUEVA VARIABLE PARA CONTROLAR LOGIN
logged_in = False

# --- COLORES Y FUENTES ---
COLOR_FONDO = "#f3d58e"
COLOR_BOTON = "#8B4513"
COLOR_TEXTO = "#3e2723"

FONT_TITULO = ("Arial", 30, "bold")
FONT_SUBTITULO = ("Arial", 22, "bold")
FONT_TEXTO = ("Arial", 14)
FONT_BOTON = ("Arial", 14, "bold")
FONT_MENU = ("Arial", 18, "bold")


# ============================================================
#     FUNCIÓN PARA ABRIR IMAGEN EN GRANDE
# ============================================================
def abrir_imagen(ruta):
    if not ruta or not os.path.exists(ruta):
        messagebox.showerror("Error", "No se encontró la imagen.")
        return
    top = tk.Toplevel()
    top.title("Vista de Imagen")
    top.configure(bg=COLOR_FONDO)

    img = Image.open(ruta)
    max_size = (700, 700)
    img.thumbnail(max_size, Image.LANCZOS)
    imgTk = ImageTk.PhotoImage(img)

    lbl = tk.Label(top, image=imgTk, bg=COLOR_FONDO)
    lbl.image = imgTk
    lbl.pack(padx=10, pady=10)


# ============================================================
#               VENTANA PRINCIPAL (APP)
# ============================================================
def ventana_inicio():
    global logged_in

    root = tk.Tk()
    root.title("CUARTO DE MILLA")
    root.geometry("1130x700")
    root.configure(bg=COLOR_FONDO)

    main_container = tk.Frame(root, bg=COLOR_FONDO)
    main_container.pack(fill="both", expand=True)

    # ------------ ENCABEZADO ------------
    header_frame = tk.Frame(main_container, bg=COLOR_FONDO)
    header_frame.pack(fill="x", pady=10)

    # LOGO
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

    # TÍTULO CENTRO
    titulo = tk.Label(
        header_frame,
        text="CUARTO DE MILLA",
        font=("Arial", 40, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_BOTON
    )
    titulo.pack(side="left", padx=100)

    # *** NUEVO LABEL PARA MOSTRAR EL ROL ***
    rol_label = tk.Label(
        header_frame,
        text="",            # Se actualiza al logearse
        font=("Arial", 14, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    rol_label.pack(side="right", padx=20)

    linea = tk.Frame(main_container, bg=COLOR_BOTON, height=4)
    linea.pack(fill="x", pady=5)

    main_frame = tk.Frame(main_container, bg=COLOR_FONDO)
    main_frame.pack(fill="both", expand=True)

    pie = tk.Frame(main_container, bg=COLOR_BOTON)
    pie.pack(fill="x")
    pie_visible = True

    tk.Label(pie, text="Tel: +52 2215 6805 63 | WhatsApp: +52 222 987 6543",
             font=FONT_TEXTO, bg=COLOR_BOTON, fg="white").pack()

    tk.Label(pie, text="Facebook: @CuartoDeMilla | Instagram: @cuartodemilla_vaquero",
             font=FONT_TEXTO, bg=COLOR_BOTON, fg="white").pack()

    # ----------- FUNCIÓN CAMBIAR PANTALLAS -----------
    def mostrar_frame(frame_func, mostrar_pie=False):
        nonlocal pie_visible
        for w in main_frame.winfo_children():
            w.destroy()
        frame_func()
        if mostrar_pie and not pie_visible:
            pie.pack(fill="x")
            pie_visible = True
        elif not mostrar_pie and pie_visible:
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

        # ================================
        #  NUEVA IMAGEN EN LA PANTALLA DE INICIO
        # ================================
        try:
            img2 = Image.open("LOGO WRANGLER.png")   # ← usa aquí tu imagen
            img2 = img2.resize((250, 150))
            img2Tk = ImageTk.PhotoImage(img2)

            lbl_img2 = tk.Label(main_frame, image=img2Tk, bg=COLOR_FONDO)
            lbl_img2.image = img2Tk
            lbl_img2.pack(pady=20)

        except:
            tk.Label(main_frame, text="(Imagen no encontrada)",
                     bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_TEXTO).pack(pady=20)

    # LOGIN
    def frame_login():
        tk.Label(main_frame, text="Usuario:", font=FONT_TEXTO, bg=COLOR_FONDO).pack(pady=5)
        usuario_entry = tk.Entry(main_frame, font=FONT_TEXTO)
        usuario_entry.pack(pady=5)

        tk.Label(main_frame, text="Contraseña:", font=FONT_TEXTO, bg=COLOR_FONDO).pack(pady=5)
        password_entry = tk.Entry(main_frame, font=FONT_TEXTO, show="*")
        password_entry.pack(pady=5)

        def validar():
            nonlocal perfil_index, productos_index, caja_index, atencion_index
            global logged_in

            for u in usuarios:
                if usuario_entry.get() == u["usuario"] and password_entry.get() == u["password"]:
                    logged_in = True
                    messagebox.showinfo("Acceso", "Bienvenido")

                    # ACTIVAR MENU COMPLETO
                    menu.entryconfig(perfil_index, state="normal")
                    menu.entryconfig(productos_index, state="normal")
                    menu.entryconfig(caja_index, state="normal")
                    menu.entryconfig(atencion_index, state="normal")

                    # *** MOSTRAR EL ROL ARRIBA A LA DERECHA ***
                    rol_label.config(text=f"Rol: {u['rol']}")

                    mostrar_frame(frame_inicio, mostrar_pie=True)
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

            # *** ACTUALIZAR EL ROL EN LA ESQUINA DERECHA ***
            if logged_in:
                rol_label.config(text=f"Rol: {usuario['rol']}")

            messagebox.showinfo("Éxito", "Datos actualizados")

        tk.Button(main_frame, text="Guardar Cambios", bg=COLOR_BOTON, fg="white",
                  width=18, height=2, font=FONT_BOTON,
                  command=guardar_cambios).pack(pady=15)

    # PRODUCTOS
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
                    try:
                        img = Image.open(p["foto"])
                        img = img.resize((90, 90))
                        imgTk = ImageTk.PhotoImage(img)
                        img_lbl = tk.Label(card, image=imgTk, bg="#ecd9a3", cursor="hand2")
                        img_lbl.image = imgTk
                        img_lbl.pack(side="left", padx=10)
                        img_lbl.bind("<Button-1>", lambda e, ruta=p["foto"]: abrir_imagen(ruta))
                    except:
                        pass

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

    # ------------ MANEJO DE CAJA / VENTAS ------------
    def frame_manejo_caja():
        cont = tk.Frame(main_frame, bg=COLOR_FONDO)
        cont.pack(fill="both", expand=True, pady=10)

        tk.Label(cont, text="Manejo de Caja", font=FONT_SUBTITULO, bg=COLOR_FONDO).pack(pady=10)

        form = tk.Frame(cont, bg=COLOR_FONDO)
        form.pack(pady=5)

        producto_var = tk.StringVar(value="")

        tk.Label(form, text="Producto:", bg=COLOR_FONDO, font=FONT_TEXTO).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        option_menu_holder = tk.Frame(form, bg=COLOR_FONDO)
        option_menu_holder.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        producto_menu = None

        def rebuild_product_menu():
            nonlocal producto_menu
            nombres = [p["nombre"] for p in productos]
            if not nombres:
                nombres = ["(Sin productos)"]
            for w in option_menu_holder.winfo_children():
                w.destroy()
            producto_var.set(nombres[0])
            producto_menu = tk.OptionMenu(option_menu_holder, producto_var, *nombres)
            producto_menu.config(font=FONT_TEXTO)
            producto_menu.pack()

        tk.Label(form, text="Cantidad:", bg=COLOR_FONDO, font=FONT_TEXTO).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        cantidad_entry = tk.Entry(form, font=FONT_TEXTO, width=10)
        cantidad_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        cantidad_entry.insert(0, "1")

        tk.Label(form, text="Precio unitario:", bg=COLOR_FONDO, font=FONT_TEXTO).grid(row=2, column=0, sticky="e", padx=5, pady=5)
        precio_var = tk.StringVar(value="0.00")
        tk.Label(form, textvariable=precio_var, bg=COLOR_FONDO, font=FONT_TEXTO).grid(row=2, column=1, sticky="w", padx=5, pady=5)

        tk.Label(form, text="Total:", bg=COLOR_FONDO, font=FONT_TEXTO).grid(row=3, column=0, sticky="e", padx=5, pady=5)
        total_var = tk.StringVar(value="0.00")
        tk.Label(form, textvariable=total_var, bg=COLOR_FONDO, font=FONT_TEXTO).grid(row=3, column=1, sticky="w", padx=5, pady=5)

        def actualizar_precio_y_total(*_):
            nombre = producto_var.get()
            p = next((x for x in productos if x["nombre"] == nombre), None)
            precio = 0.0
            if p:
                try:
                    precio = float(str(p["precio"]).replace(",", "."))
                except:
                    precio = 0.0
            precio_var.set(f"{precio:.2f}")

            try:
                qty = int(cantidad_entry.get())
            except:
                qty = 0
            total_var.set(f"{precio * qty:.2f}")

        def registrar_venta():
            nombre = producto_var.get()
            if nombre == "(Sin productos)":
                messagebox.showwarning("Atención", "No hay productos en el catálogo.")
                return

            p = next((x for x in productos if x["nombre"] == nombre), None)
            if not p:
                messagebox.showerror("Error", "Producto no encontrado.")
                return

            try:
                precio_u = float(str(p["precio"]).replace(",", "."))
            except:
                messagebox.showerror("Error", "Precio inválido.")
                return

            try:
                qty = int(cantidad_entry.get())
                if qty <= 0: raise ValueError
            except:
                messagebox.showerror("Error", "Cantidad inválida.")
                return

            total = round(precio_u * qty, 2)
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ventas.append({"producto": nombre, "precio": precio_u, "cantidad": qty, "total": total, "fecha": fecha})

            messagebox.showinfo("Venta registrada", f"{nombre} x{qty} = ${total:.2f}")

        btn_frame = tk.Frame(cont, bg=COLOR_FONDO)
        btn_frame.pack(pady=8)
        tk.Button(btn_frame, text="Registrar Venta", bg=COLOR_BOTON, fg="white", font=FONT_BOTON,
                  command=registrar_venta).pack(side="left", padx=8)
        tk.Button(btn_frame, text="Actualizar catálogo", bg="#5a5", fg="white", font=FONT_BOTON,
                  command=lambda: (rebuild_product_menu(), actualizar_precio_y_total())).pack(side="left", padx=8)

        tk.Label(cont, text="Historial de Ventas", font=FONT_SUBTITULO, bg=COLOR_FONDO).pack(pady=6)
        hist_container = tk.Frame(cont, bg=COLOR_FONDO)
        hist_container.pack(fill="both", expand=True, padx=10, pady=6)

        hist_canvas = tk.Canvas(hist_container, bg=COLOR_FONDO, highlightthickness=0)
        hist_canvas.pack(side="left", fill="both", expand=True)
        hist_scroll = tk.Scrollbar(hist_container, orient="vertical", command=hist_canvas.yview)
        hist_scroll.pack(side="right", fill="y")
        hist_canvas.configure(yscrollcommand=hist_scroll.set)

        historial_frame = tk.Frame(hist_canvas, bg=COLOR_FONDO)
        hist_canvas.create_window((0, 0), window=historial_frame, anchor="nw")

        def actualizar_historial():
            for w in historial_frame.winfo_children():
                w.destroy()

            if not ventas:
                tk.Label(historial_frame, text="No hay ventas registradas.",
                         bg=COLOR_FONDO, font=FONT_TEXTO).pack(pady=6)
                return

            for v in reversed(ventas):
                txt = f"{v['fecha']} - {v['producto']} x{v['cantidad']}  |  ${v['total']:.2f}"
                tk.Label(historial_frame, text=txt, bg=COLOR_FONDO,
                         font=FONT_TEXTO, anchor="w").pack(fill="x", padx=6, pady=3)

        rebuild_product_menu()
        actualizar_precio_y_total()
        actualizar_historial()

        producto_var.trace_add("write", actualizar_precio_y_total)
        cantidad_entry.bind("<KeyRelease>", lambda e: actualizar_precio_y_total())

    # ATENCIÓN AL CLIENTE
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

    # MENU PÚBLICO
    menu.add_command(label="Inicio", command=lambda: mostrar_frame(frame_inicio, mostrar_pie=True))
    menu.add_command(label="Login", command=lambda: mostrar_frame(frame_login))
    menu.add_command(label="Contacto", command=lambda: mostrar_frame(frame_contacto))

    # ----------- OPCIONES RESTRINGIDAS AL INICIO -----------
    perfil_index = menu.index("end") + 1
    menu.add_command(label="Gestión de Perfil", state="disabled",
                     command=lambda: mostrar_frame(frame_perfil))

    productos_index = menu.index("end") + 1
    menu.add_command(label="Gestión de Productos", state="disabled",
                     command=lambda: mostrar_frame(frame_productos))

    caja_index = menu.index("end") + 1
    menu.add_command(label="Manejo de Caja", state="disabled",
                     command=lambda: mostrar_frame(frame_manejo_caja))

    atencion_index = menu.index("end") + 1
    menu.add_command(label="Atención al Cliente", state="disabled",
                     command=lambda: mostrar_frame(frame_atencion))

    mostrar_frame(frame_inicio, mostrar_pie=True)

    root.mainloop()


# Ejecutar la app
ventana_inicio()
