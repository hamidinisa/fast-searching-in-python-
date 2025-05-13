import csv
from tkinter import ttk, messagebox
import tkinter as tk
from bisect import bisect_left

class BPlusTreeIndex:
    def __init__(self):
        self.keys = []
        self.values = []

    def insert(self, key, book_id):
        key = key.lower()
        idx = bisect_left(self.keys, key)
        if idx < len(self.keys) and self.keys[idx] == key:
            self.values[idx].append(book_id)
        else:
            self.keys.insert(idx, key)
            self.values.insert(idx, [book_id])

    def search(self, key):
        key = key.lower()
        idx = bisect_left(self.keys, key)
        if idx < len(self.keys) and self.keys[idx] == key:
            return self.values[idx]
        return []

def build_indexes_with_bptree(file_path):
    index_title = BPlusTreeIndex()
    index_author = BPlusTreeIndex()
    index_category = BPlusTreeIndex()
    books = {}

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 5:
                    continue
                book_id, title, author, category, year = [x.strip() for x in row]
                books[book_id] = (title, author, category, year)

                index_title.insert(title, book_id)
                index_author.insert(author, book_id)
                index_category.insert(category, book_id)
    except FileNotFoundError:
        messagebox.showerror("Hata", f"Dosya bulunamadı: {file_path}")
    except Exception as e:
        messagebox.showerror("Hata", f"Beklenmedik hata: {e}")

    return books, index_title, index_author, index_category

def search_bptree(index, keyword, books):
    results = index.search(keyword)
    if not results:
        return ["Sonuç bulunamadı."]
    output = []
    for book_id in results:
        title, author, category, year = books[book_id]
        output.append(f"[{book_id}] {title} | {author} | {category} | {year}")
    return output

def on_search():
    search_type = search_type_var.get()
    keyword = keyword_entry.get().strip()

    if not keyword:
        messagebox.showwarning("Uyarı", "Lütfen bir anahtar kelime girin.")
        return

    if search_type == "Title":
        results = search_bptree(index_title, keyword, books)
    elif search_type == "Author":
        results = search_bptree(index_author, keyword, books)
    elif search_type == "Category":
        results = search_bptree(index_category, keyword, books)
    else:
        results = ["Geçersiz arama türü."]

    result_text.delete(1.0, tk.END)
    for line in results:
        result_text.insert(tk.END, line + "\n")

# Ana program
file_path = "books_dataset.txt"
books, index_title, index_author, index_category = build_indexes_with_bptree(file_path)

# Arayüz Başlatılıyor
root = tk.Tk()
root.title("📚 Kitap Arama (B+ Tree)")
root.geometry("720x500")
root.configure(bg="#f7f7f7")

# Başlık
tk.Label(root, text="Kitap Arama Uygulaması", font=("Helvetica", 16, "bold"), bg="#f7f7f7", fg="#003366").pack(pady=10)

# Arama Türü
tk.Label(root, text="Arama Türü:", font=("Helvetica", 11), bg="#f7f7f7").pack()
search_type_var = tk.StringVar(value="Title")
search_type_menu = ttk.Combobox(root, textvariable=search_type_var, values=["Title", "Author", "Category"], state="readonly")
search_type_menu.pack(pady=5)

# Anahtar Kelime Girişi
tk.Label(root, text="Anahtar Kelime:", font=("Helvetica", 11), bg="#f7f7f7").pack()
keyword_entry = tk.Entry(root, font=("Helvetica", 11), width=50)
keyword_entry.pack(pady=5)
keyword_entry.bind("<Return>", lambda event: on_search())

# Arama Butonu
search_button = tk.Button(root, text="Ara", font=("Helvetica", 11, "bold"), bg="#004c99", fg="white", command=on_search)
search_button.pack(pady=10)

# Sonuçlar Paneli
text_frame = tk.Frame(root)
text_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_text = tk.Text(text_frame, font=("Courier New", 10), wrap=tk.WORD, yscrollcommand=scrollbar.set, bg="#fff", relief=tk.SUNKEN, borderwidth=1)
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=result_text.yview)

root.mainloop()