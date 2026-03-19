import tkinter as tk
from tkinter import messagebox

from services.password_services import PasswordService
from storage.file_storage import FileStorage
from utils.clipboard import ClipboardManager

root = None
current_password = ""
mode_var = None
words_entry = None

service = PasswordService()


def generar():

    global current_password

    try:

        mode = mode_var.get()

        if mode == "password":

            length = int(length_entry.get())

            result = service.create_password(
                length,
                lowercase_var.get(),
                uppercase_var.get(),
                digits_var.get(),
                symbols_var.get(),
            )

        else:

            words = int(words_entry.get())

            result = service.create_passphrase(words)

        password = result["password"]
        entropy = result["entropy"]
        strength = result["strength"]
        is_weak = result["is_weak"]

        current_password = password

        result_label.config(text=f"Contraseña: {password}")

        entropy_label.config(text=f"Entropía: {entropy} bits")

        strength_label.config(text=f"Seguridad: {strength}")

        if is_weak:
            weak_label.config(text="⚠️ Contraseña común (insegura)")
        else:
            weak_label.config(text="✔ No encontrada en lista de rockyou")

        if save_var.get():
            FileStorage.save_password(password)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def copiar_contraseña():

    global current_password

    if not current_password:
        messagebox.showwarning("Aviso", "Primero genera una contraseña")
        return

    ClipboardManager.copy_to_clipboard(root, current_password)
    messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles")


def start_gui():

    global root
    global mode_var
    global words_entry
    global length_entry
    global result_label
    global entropy_label
    global strength_label
    global lowercase_var
    global uppercase_var
    global digits_var
    global symbols_var
    global save_var
    global weak_label

    root = tk.Tk()
    root.title("Password Generator")

    tk.Label(root, text="Longitud").pack()

    length_entry = tk.Entry(root)
    length_entry.pack()

    tk.Label(root, text="Número de palabras (passphrase)").pack()

    words_entry = tk.Entry(root)
    words_entry.insert(0, "4")
    words_entry.pack()

    lowercase_var = tk.BooleanVar(value=True)
    uppercase_var = tk.BooleanVar(value=True)
    digits_var = tk.BooleanVar(value=True)
    symbols_var = tk.BooleanVar(value=False)
    mode_var = tk.StringVar(value="password")

    tk.Label(root, text="Tipo de generación").pack()

    tk.Radiobutton(
        root, text="Contraseña aleatoria", variable=mode_var, value="password"
    ).pack(anchor="w")

    tk.Radiobutton(
        root, text="Passphrase (Diceware)", variable=mode_var, value="passphrase"
    ).pack(anchor="w")

    tk.Checkbutton(root, text="Minúsculas", variable=lowercase_var).pack(anchor="w")
    tk.Checkbutton(root, text="Mayúsculas", variable=uppercase_var).pack(anchor="w")
    tk.Checkbutton(root, text="Números", variable=digits_var).pack(anchor="w")
    tk.Checkbutton(root, text="Símbolos", variable=symbols_var).pack(anchor="w")

    save_var = tk.BooleanVar()

    tk.Checkbutton(root, text="Guardar contraseña", variable=save_var).pack(anchor="w")

    tk.Button(root, text="Generar", command=generar).pack()

    tk.Button(root, text="Copiar contraseña", command=copiar_contraseña).pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    entropy_label = tk.Label(root, text="")
    entropy_label.pack()

    strength_label = tk.Label(root, text="")
    strength_label.pack()

    weak_label = tk.Label(root, text="")
    weak_label.pack()

    root.mainloop()
