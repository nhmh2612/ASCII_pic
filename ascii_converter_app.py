import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    return "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])

def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi mở ảnh: {e}")
        return None

    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    ascii_width = image.width
    return "\n".join([ascii_str[i:i+ascii_width] for i in range(0, len(ascii_str), ascii_width)])

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return

    try:
        original_image = Image.open(file_path)
        original_image.thumbnail((300, 300))  # Resize for display
        original_photo = ImageTk.PhotoImage(original_image)
        lbl_original.config(image=original_photo)
        lbl_original.image = original_photo

        ascii_art = image_to_ascii(file_path, new_width=100)
        if ascii_art:
            txt_ascii.delete(1.0, tk.END)
            txt_ascii.insert(tk.END, ascii_art)
            btn_save.config(state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể xử lý ảnh: {e}")

def save_ascii():
    ascii_content = txt_ascii.get(1.0, tk.END).strip()
    if not ascii_content:
        messagebox.showerror("Lỗi", "Không có dữ liệu ASCII để lưu.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not file_path:
        return

    try:
        with open(file_path, "w") as file:
            file.write(ascii_content)
        messagebox.showinfo("Thành công", "ASCII Art đã được lưu.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi lưu file: {e}")

# Tạo giao diện chính
root = tk.Tk()
root.title("Chuyển đổi ảnh sang ASCII")
root.geometry("800x600")

# Khung hình ảnh gốc
frame_original = tk.LabelFrame(root, text="Ảnh gốc", padx=10, pady=10)
frame_original.pack(side=tk.LEFT, padx=10, pady=10)

lbl_original = tk.Label(frame_original)
lbl_original.pack()

# Khung ASCII art
frame_ascii = tk.LabelFrame(root, text="ASCII Art", padx=10, pady=10)
frame_ascii.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

txt_ascii = tk.Text(frame_ascii, wrap=tk.NONE, font=("Courier", 10))
txt_ascii.pack(fill=tk.BOTH, expand=True)

# Các nút
frame_buttons = tk.Frame(root)
frame_buttons.pack(side=tk.BOTTOM, pady=10)

btn_open = tk.Button(frame_buttons, text="Chọn ảnh", command=open_image)
btn_open.pack(side=tk.LEFT, padx=10)

btn_save = tk.Button(frame_buttons, text="Lưu ASCII", command=save_ascii, state=tk.DISABLED)
btn_save.pack(side=tk.RIGHT, padx=10)

root.mainloop()