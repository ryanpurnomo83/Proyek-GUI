import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan pesan
def show_message():
    messagebox.showinfo("Message", "This is an example of message!")

# Membuat jendela utama
root = tk.Tk()
root.title("Simple GUI Application")

# Membuat label
label = tk.Label(root, text="This is my First GUI Application")
label.pack(pady=10)

# Membuat tombol
button = tk.Button(root, text="Click to See the message", command=show_message)
button.pack(pady=5)

# Menampilkan jendela
root.mainloop()
