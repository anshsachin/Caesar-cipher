import tkinter as tk
from tkinter import filedialog, messagebox

# ---------------- Caesar Cipher Logic ---------------- #
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # केवल letters shift होंगे
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # symbols, numbers वैसे ही रहेंगे
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# ---------------- GUI Functions ---------------- #
def encrypt_text():
    text = entry_text.get()
    if not text.strip():
        messagebox.showwarning("Warning", "⚠️ Please enter some text!")
        return
    
    try:
        shift = int(entry_key.get())
        encrypted = caesar_encrypt(text, shift)
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, encrypted)
    except ValueError:
        messagebox.showerror("Error", "⚠️ Shift key must be a valid number!")

def decrypt_text():
    text = entry_text.get()
    if not text.strip():
        messagebox.showwarning("Warning", "⚠️ Please enter some text!")
        return

    try:
        shift = int(entry_key.get())
        decrypted = caesar_decrypt(text, shift)
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, decrypted)
    except ValueError:
        messagebox.showerror("Error", "⚠️ Shift key must be a valid number!")

def clear_all():
    entry_text.delete(0, tk.END)
    entry_key.delete(0, tk.END)
    output_box.delete(1.0, tk.END)

def save_to_file():
    text = output_box.get(1.0, tk.END).strip()
    if text:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text)
            messagebox.showinfo("Success", "✅ File saved successfully!")
    else:
        messagebox.showwarning("Warning", "⚠️ No output text to save!")

# ---------------- Tkinter GUI ---------------- #
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("550x500")
root.configure(bg="#f5f5f5")

heading = tk.Label(root, text="🔐 Caesar Cipher Encryption Tool", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333")
heading.pack(pady=15)

# Input Text
label_input = tk.Label(root, text="Enter your text:", font=("Arial", 12), bg="#f5f5f5")
label_input.pack()
entry_text = tk.Entry(root, width=50, font=("Arial", 12))
entry_text.pack(pady=5)

# Shift Key
label_key = tk.Label(root, text="Enter Shift Key (number):", font=("Arial", 12), bg="#f5f5f5")
label_key.pack()
entry_key = tk.Entry(root, width=10, font=("Arial", 12))
entry_key.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=15)

encrypt_btn = tk.Button(button_frame, text="Encrypt", command=encrypt_text, bg="#90EE90", font=("Arial", 11, "bold"), width=10)
encrypt_btn.grid(row=0, column=0, padx=5)

decrypt_btn = tk.Button(button_frame, text="Decrypt", command=decrypt_text, bg="#ADD8E6", font=("Arial", 11, "bold"), width=10)
decrypt_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(button_frame, text="Clear", command=clear_all, bg="#FF7F7F", font=("Arial", 11, "bold"), width=10)
clear_btn.grid(row=0, column=2, padx=5)

save_btn = tk.Button(button_frame, text="Save", command=save_to_file, bg="#FFD580", font=("Arial", 11, "bold"), width=10)
save_btn.grid(row=0, column=3, padx=5)

# Output
label_output = tk.Label(root, text="Output:", font=("Arial", 12), bg="#f5f5f5")
label_output.pack()
output_box = tk.Text(root, height=10, width=60, font=("Courier", 12))
output_box.pack(pady=10)

root.mainloop()
