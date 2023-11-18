import tkinter as tk
from tkinter import messagebox

class SubstitutionCipherGUI:
    def __init__(self, master):
        self.master = master
        master.title("Substitution Cipher GUI")

        # Create widgets
        self.label_key = tk.Label(master, text="Enter Key:")
        self.entry_key = tk.Entry(master)
        self.label_message = tk.Label(master, text="Enter Message:")
        self.entry_message = tk.Entry(master)
        self.label_result = tk.Label(master, text="Result:")
        self.result_text = tk.Text(master, height=5, width=40)
        self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt_message)
        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt_message)

        # Arrange widgets
        self.label_key.grid(row=0, column=0, sticky=tk.E)
        self.entry_key.grid(row=0, column=1, padx=10, pady=10)
        self.label_message.grid(row=1, column=0, sticky=tk.E)
        self.entry_message.grid(row=1, column=1, padx=10, pady=10)
        self.label_result.grid(row=2, column=0, sticky=tk.E)
        self.result_text.grid(row=2, column=1, padx=10, pady=10)
        self.encrypt_button.grid(row=3, column=0, pady=10)
        self.decrypt_button.grid(row=3, column=1, pady=10)

    def encrypt_message(self):
        key = self.entry_key.get()
        message = self.entry_message.get().upper()
        encrypted_message = self.substitution_cipher(message, key)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, encrypted_message)

    def decrypt_message(self):
        key = self.entry_key.get()
        message = self.result_text.get(1.0, tk.END).strip()
        decrypted_message = self.substitution_cipher(message, key, decrypt=True)
        self.entry_message.delete(0, tk.END)
        self.entry_message.insert(0, decrypted_message)

    def substitution_cipher(self, message, key, decrypt=False):
        result = ""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = key.upper()

        for char in message:
            if char in alphabet:
                index = (alphabet.index(char) - alphabet.index(key[0])) if decrypt else (alphabet.index(char) + alphabet.index(key[0]))
                index = index % 26  # Ensure it stays within the range of the alphabet
                result += alphabet[index]
            else:
                result += char

        return result

def main():
    root = tk.Tk()
    app = SubstitutionCipherGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()