import string
import tkinter as tk
from tkinter import ttk, messagebox


alphabet = string.ascii_lowercase

def decrypt_caesar (cipherText: str, shift: int = 3) -> str:
   
    decryptedText=[]

    for char in cipherText:
        if char.isalpha():
            i = (alphabet.index(char) - shift)
            decryptedText.append(alphabet[i])
        else:
            decryptedText.append(char)
    return "".join(decryptedText)   

def on_decrypt():
    cipherText = cipherEntry.get("1.0", tk.END).strip().lower()

    if not cipherText:
        messagebox.showwarning("Input Error", "Please provide input")
        return
    try:
        plainText = decrypt_caesar(cipherText)  
        outputPlain.set(plainText)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def Copy():
    copyText=outputPlain.get()
    root.clipboard_clear()
    root.clipboard_append(copyText)
    root.update()



#GUI for decryption

root = tk.Tk()
root.title("Cipher Decryption")
root.geometry("500x350")
root.resizable(False, True)

labelCipher = ttk.Label(root, text="Enter Encrypted Text:")
labelCipher.pack(pady=(10, 0))

cipherEntry = tk.Text(root, height=5, width=50)
cipherEntry.pack(pady=2)

btnDecrypt = ttk.Button(root, text="Decrypt", command=on_decrypt)
btnDecrypt.pack(pady=10)

labelOutput = ttk.Label(root, text="Decrypted Message:")
labelOutput.pack(pady=(5, 5))

outputPlain = tk.StringVar()
outputLabel = ttk.Label(root, font=("Arial",10), textvariable=outputPlain, wraplength=400, background="white")
outputLabel.pack(pady=10, padx=50, fill=tk.BOTH, expand=False)

btnCopy = ttk.Button(root, text="Copy All", command=Copy)
btnCopy.pack(pady=10)

root.focus_force()
root.mainloop()

