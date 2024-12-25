import tkinter as tk
from tkinter import ttk

class CaesarCipherApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Program Enkripsi & Dekripsi - Caesar Cipher")
        self.root.geometry("600x500")
        self.root.configure(bg="#DDEEFF")  # warna biru muda untuk latar belakang utama

        self.shift_value = tk.IntVar(value=3)  # otomatis 3 (default)

        self.tab_control = ttk.Notebook(root)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.tab1, text='Enkripsi')
        self.tab_control.add(self.tab2, text='Dekripsi')
        self.tab_control.pack(expand=1, fill="both")
        
        self.setup_enkripsi_tab()
        self.setup_dekripsi_tab()

    def create_rounded_rectangle(self, canvas, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1 + radius, y1,
            x1 + radius, y1,
            x2 - radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1 + radius,
            x1, y1
        ]
        return canvas.create_polygon(points, smooth=True, **kwargs)

    def create_textbox_with_border(self, canvas, x1, y1, x2, y2, text_var=None, **kwargs):
        """Create a textbox with rounded borders"""
        self.create_rounded_rectangle(canvas, x1, y1, x2, y2, **kwargs)
        textbox = tk.Text(canvas, height=5, width=55, bg="#DDEEFF", fg="#000080", wrap="word", borderwidth=0, relief="flat")
        textbox.place(x=x1 + 10, y=y1 + 10, width=x2 - x1 - 20, height=y2 - y1 - 20)
        return textbox

    def setup_enkripsi_tab(self):
        canvas = tk.Canvas(self.tab1, bg="#DDEEFF", highlightthickness=0)
        canvas.pack(fill="both", expand=True, padx=10, pady=10)

        self.create_rounded_rectangle(canvas, 20, 20, 560, 100, radius=20, fill="#B0E0E6", outline="#87CEEB")
        tk.Label(canvas, text="Jumlah Pergeseran:", bg="#B0E0E6", fg="black").place(x=40, y=40)
        shift_spinbox = ttk.Spinbox(canvas, from_=1, to=25, width=5, textvariable=self.shift_value)
        shift_spinbox.place(x=160, y=40)

        self.create_rounded_rectangle(canvas, 20, 110, 560, 230, radius=20, fill="#B0E0E6", outline="#87CEEB")
        tk.Label(canvas, text="Masukkan Plainteks:", bg="#B0E0E6", fg="black").place(x=40, y=130)
        self.plaintext_input = self.create_textbox_with_border(canvas, 40, 150, 540, 220, fill="#DDEEFF", outline="#87CEEB")

        tk.Button(canvas, text="Enkripsi", command=self.encrypt, bg="#87CEEB", fg="black").place(x=260, y=250)

        self.create_rounded_rectangle(canvas, 20, 290, 560, 410, radius=20, fill="#B0E0E6", outline="#87CEEB")
        tk.Label(canvas, text="Hasil Enkripsi (Cipherteks):", bg="#B0E0E6", fg="black").place(x=40, y=310)
        self.cipher_output = self.create_textbox_with_border(canvas, 40, 330, 540, 400, fill="#DDEEFF", outline="#87CEEB")

    def setup_dekripsi_tab(self):
        canvas = tk.Canvas(self.tab2, bg="#DDEEFF", highlightthickness=0)
        canvas.pack(fill="both", expand=True, padx=10, pady=10)

        self.create_rounded_rectangle(canvas, 20, 20, 560, 100, radius=20, fill="#B0E0E6", outline="#87CEEB")
        tk.Label(canvas, text="Jumlah Pergeseran:", bg="#B0E0E6", fg="black").place(x=40, y=40)
        shift_spinbox = ttk.Spinbox(canvas, from_=1, to=25, width=5, textvariable=self.shift_value)
        shift_spinbox.place(x=160, y=40)

        self.create_rounded_rectangle(canvas, 20, 110, 560, 180, radius=20, fill="#B0E0E6", outline="#87CEEB")
        tk.Label(canvas, text="Masukkan Cipherteks:", bg="#B0E0E6", fg="black").place(x=40, y=130)
        self.cipher_input = self.create_textbox_with_border(canvas, 40, 150, 540, 170, fill="#DDEEFF", outline="#87CEEB")

        tk.Button(canvas, text="Dekripsi", command=self.decrypt, bg="#87CEEB", fg="black").place(x=260, y=200)

        self.create_rounded_rectangle(canvas, 20, 240, 560, 310, radius=20, fill="#B0E0E6", outline="#87CEEB")
        tk.Label(canvas, text="Hasil Dekripsi (Plainteks):", bg="#B0E0E6", fg="black").place(x=40, y=260)
        self.plain_output = self.create_textbox_with_border(canvas, 40, 280, 540, 300, fill="#DDEEFF", outline="#87CEEB")

    def shift_character(self, char, shift, encrypt=True):
        if not char.isalpha():
            return char
            
        ascii_base = 97 if char.islower() else 65
        if not encrypt:
            shift = -shift
        shifted = (ord(char) - ascii_base + shift) % 26
        return chr(shifted + ascii_base)
    
    def process_text(self, text, encrypt=True):
        shift = self.shift_value.get()
        result = ''
        for char in text:
            result += self.shift_character(char, shift, encrypt)
        return result
    
    def encrypt(self):
        plaintext = self.plaintext_input.get("1.0", tk.END).strip()
        ciphertext = self.process_text(plaintext, encrypt=True)
        self.cipher_output.delete("1.0", tk.END)
        self.cipher_output.insert("1.0", ciphertext)
    
    def decrypt(self):
        ciphertext = self.cipher_input.get("1.0", tk.END).strip()
        plaintext = self.process_text(ciphertext, encrypt=False)
        self.plain_output.delete("1.0", tk.END)
        self.plain_output.insert("1.0", plaintext)

if _name_ == "_main_":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()