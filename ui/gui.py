import tkinter as tk
from tkinter import messagebox

from services.password_services import PasswordService
from storage.file_storage import FileStorage


service = PasswordService()


def generar():

    try:

        length = int(length_entry.get())

        result = service.create_password(
            length,
            lowercase_var.get(),
            uppercase_var.get(),
            digits_var.get(),
            symbols_var.get(),
        )

        password = result["password"]
        entropy = result["entropy"]
        strength = result["strength"]

        result_label.config(text=f"Contraseña: {password}")

        entropy_label.config(text=f"Entropía: {entropy} bits")

        strength_label.config(text=f"Seguridad: {strength}")

        if save_var.get():
            FileStorage.save_password(password)

    except Exception as e:

        messagebox.showerror("Error", str(e))


def start_gui():

    global length_entry
    global result_label
    global entropy_label
    global strength_label
    global lowercase_var
    global uppercase_var
    global digits_var
    global symbols_var
    global save_var

    root = tk.Tk()
    root.title("Password Generator")

    tk.Label(root, text="Longitud").pack()

    length_entry = tk.Entry(root)
    length_entry.pack()

    lowercase_var = tk.BooleanVar(value=True)
    uppercase_var = tk.BooleanVar(value=True)
    digits_var = tk.BooleanVar(value=True)
    symbols_var = tk.BooleanVar(value=False)

    tk.Checkbutton(root, text="Minúsculas", variable=lowercase_var).pack(anchor="w")
    tk.Checkbutton(root, text="Mayúsculas", variable=uppercase_var).pack(anchor="w")
    tk.Checkbutton(root, text="Números", variable=digits_var).pack(anchor="w")
    tk.Checkbutton(root, text="Símbolos", variable=symbols_var).pack(anchor="w")

    save_var = tk.BooleanVar()

    tk.Checkbutton(root, text="Guardar contraseña", variable=save_var).pack(anchor="w")

    tk.Button(root, text="Generar", command=generar).pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    entropy_label = tk.Label(root, text="")
    entropy_label.pack()

    strength_label = tk.Label(root, text="")
    strength_label.pack()

    root.mainloop()
