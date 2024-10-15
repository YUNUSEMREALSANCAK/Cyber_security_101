import tkinter as tk
from tkinter import filedialog

def create_wordlist():
    string_input = entry_string.get()
    start_num = int(entry_start.get())
    end_num = int(entry_end.get())
    
    wordlist = [f"{string_input}{i}" for i in range(start_num, end_num + 1)]
    
    # Dosya kaydetme
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            for word in wordlist:
                file.write(word + "\n")
        label_result.config(text="Wordlist başarıyla kaydedildi!")

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("Wi-Fi Şifre Tahmin Programı")

# Giriş kutuları
tk.Label(root, text="String Girişi:").pack()
entry_string = tk.Entry(root)
entry_string.pack()

tk.Label(root, text="Başlangıç Numarası:").pack()
entry_start = tk.Entry(root)
entry_start.pack()

tk.Label(root, text="Bitiş Numarası:").pack()
entry_end = tk.Entry(root)
entry_end.pack()

# Wordlist oluşturma butonu
btn_create = tk.Button(root, text="Wordlist Oluştur ve Kaydet", command=create_wordlist)
btn_create.pack()

# Sonuç etiketi
label_result = tk.Label(root, text="")
label_result.pack()

# Tkinter döngüsü
root.mainloop()
