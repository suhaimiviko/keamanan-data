import tkinter as tk
from tkinter import ttk
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

def decrypt(encrypted_text, key):
    des = DES.new(key, DES.MODE_ECB)
    decoded_encrypted_text = base64.b64decode(encrypted_text)
    decrypted_text = des.decrypt(decoded_encrypted_text).decode('utf-8')
    return decrypted_text.rstrip()

class DESApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Program Enkripsi & Dekripsi - DES")
        self.root.geometry("600x500")
        self.root.configure(bg="#DDEEFF")  # Warna biru muda

        self.key = tk.StringVar()

        self.tab_control = ttk.Notebook(root)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab1, text='Enkripsi')
        self.tab_control.add(self.tab2, text='Dekripsi')
        self.tab_control.pack(expand=1, fill="both")

        self.setup_encryption_tab()
        self.setup_decryption_tab()

    def setup_encryption_tab(self):
        canvas = tk.Canvas(self.tab1, bg="#DDEEFF", highlightthickness=0)
        canvas.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(canvas, text="Masukkan Key (8 karakter):", bg="#B0E0E6", fg="black").place(x=40, y=20)
        self.key_entry = tk.Entry(canvas, textvariable=self.key, width=30, bg="#E6F7FF", fg="black")
        self.key_entry.place(x=200, y=20)

        tk.Label(canvas, text="Masukkan Plainteks:", bg="#B0E0E6", fg="black").place(x=40, y=60)
        self.plaintext_input = tk.Text(canvas, height=5, width=55, bg="#E6F7FF", fg="black", wrap="word", borderwidth=1, relief="solid")
        self.plaintext_input.place(x=40, y=90)

        tk.Button(canvas, text="Enkripsi", command=self.encrypt_text, bg="#87CEEB", fg="black").place(x=260, y=200)

        tk.Label(canvas, text="Hasil Enkripsi (Cipherteks):", bg="#B0E0E6", fg="black").place(x=40, y=250)
        self.cipher_output = tk.Text(canvas, height=5, width=55, bg="#E6F7FF", fg="black", wrap="word", borderwidth=1, relief="solid")
        self.cipher_output.place(x=40, y=280)

    def setup_decryption_tab(self):
        canvas = tk.Canvas(self.tab2, bg="#DDEEFF", highlightthickness=0)
        canvas.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(canvas, text="Masukkan Key (8 karakter):", bg="#B0E0E6", fg="black").place(x=40, y=20)
        self.key_entry_decrypt = tk.Entry(canvas, textvariable=self.key, width=30, bg="#E6F7FF", fg="black")
        self.key_entry_decrypt.place(x=200, y=20)

        tk.Label(canvas, text="Masukkan Cipherteks:", bg="#B0E0E6", fg="black").place(x=40, y=60)
        self.cipher_input = tk.Text(canvas, height=5, width=55, bg="#E6F7FF", fg="black", wrap="word", borderwidth=1, relief="solid")
        self.cipher_input.place(x=40, y=90)

        tk.Button(canvas, text="Dekripsi", command=self.decrypt_text, bg="#87CEEB", fg="black").place(x=260, y=200)

        tk.Label(canvas, text="Hasil Dekripsi (Plainteks):", bg="#B0E0E6", fg="black").place(x=40, y=250)
        self.plain_output = tk.Text(canvas, height=5, width=55, bg="#E6F7FF", fg="black", wrap="word", borderwidth=1, relief="solid")
        self.plain_output.place(x=40, y=280)

    def encrypt_text(self):
        key = self.key.get()
        plaintext = self.plaintext_input.get("1.0", tk.END).strip()
        
        if len(key) != 8:
            self.cipher_output.delete("1.0", tk.END)
            self.cipher_output.insert("1.0", "Error: Key harus memiliki panjang 8 karakter.")
            return

        try:
            encrypted_text = encrypt(plaintext, key.encode('utf-8'))
            self.cipher_output.delete("1.0", tk.END)
            self.cipher_output.insert("1.0", encrypted_text)
        except Exception as e:
            self.cipher_output.delete("1.0", tk.END)
            self.cipher_output.insert("1.0", f"Error: {str(e)}")

    def decrypt_text(self):
        key = self.key.get()
        ciphertext = self.cipher_input.get("1.0", tk.END).strip()

        if len(key) != 8:
            self.plain_output.delete("1.0", tk.END)
            self.plain_output.insert("1.0", "Error: Key harus memiliki panjang 8 karakter.")
            return

        try:
            decrypted_text = decrypt(ciphertext, key.encode('utf-8'))
            self.plain_output.delete("1.0", tk.END)
            self.plain_output.insert("1.0", decrypted_text)
        except Exception as e:
            self.plain_output.delete("1.0", tk.END)
            self.plain_output.insert("1.0", f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DESApp(root)
    root.mainloop()