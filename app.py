import tkinter as tk
from tkinter import messagebox

def on_click():
    messagebox.showinfo("Chào bạn", "Xin chào từ GitHub Actions! 🎉")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Ứng dụng của tôi")
window.geometry("300x200")
window.configure(bg='lightblue')

# Thêm label
label = tk.Label(window, text="Chào mừng bạn đến với GUI app!", 
                 bg='lightblue', font=("Arial", 12))
label.pack(pady=20)

# Thêm nút bấm
button = tk.Button(window, text="Bấm vào tôi!", 
                   command=on_click, font=("Arial", 11))
button.pack(pady=10)

# Chạy ứng dụng
window.mainloop()
