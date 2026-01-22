import tkinter as tk

window = tk.Tk()
window.geometry("200x200")
window.title("HexGen")
# generate a hex code
import random

def generate_hex():
    letters = "abcdef"
    numbers = "1234567890"

    hex_chars = letters + numbers

    hex_value = "#" + ''.join(random.choice(hex_chars) for _ in range(6))
    
    hex_entry.config(state="normal")
    hex_entry.delete(0, tk.END)
    hex_entry.insert(0, hex_value)
    hex_entry.config(state="readonly")
    window.config(bg=hex_value)

hex_entry = tk.Entry(
    window,
    justify="center",
    readonlybackground="white",
    fg="blue",
    borderwidth=0,
)

hex_entry.insert(0, "#??????")
hex_entry.config(state="readonly")


btn = tk.Button(
    window,
    text="Generate",
    command=generate_hex,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
)

hex_label = tk.Label(window)
hex_entry.pack(pady=40)
btn.pack()
window.mainloop()