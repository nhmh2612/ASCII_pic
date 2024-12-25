import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Danh sách các ký tự ASCII dùng để thay thế mức xám
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    """Thay đổi kích thước ảnh với tỷ lệ để chuyển sang ASCII."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    """Chuyển ảnh sang thang độ xám."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Chuyển đổi mức xám của pixel thành ký tự ASCII."""
    pixels = image.getdata()
    return "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])

def image_to_ascii(image_path, new_width=100):
    """Chuyển đổi một ảnh sang ASCII Art."""
    try:
        image = Image.open(image_path)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi mở ảnh: {e}")
        return None

    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    ascii_width = image.width
    return "\n".join([ascii_str[i:i + ascii_width] for i in range(0, len(ascii_str), ascii_width)])

def open_image():
    """Mở và hiển thị ảnh gốc, đồng thời chuyển đổi sang ASCII."""
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    if not file_path:
        return

    try:
        original_image = Image.open(file_path)
        original_image.thumbnail((300, 300))  # Resize for hiển thị
        original_photo = ImageTk.PhotoImage(original_image)
        lbl_original.config(image=original_photo)
        lbl_original.image = original_photo

        ascii_width = int(entry_width.get()) if entry_width.get().isdigit() else 100
        ascii_art = image_to_ascii(file_path, new_width=ascii_width)
        if ascii_art:
            txt_ascii.delete(1.0, tk.END)
            txt_ascii.insert(tk.END, ascii_art)
            btn_save.config(state=tk.NORMAL)
            btn_copy.config(state=tk.NORMAL)
            btn_reset.config(state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể xử lý ảnh: {e}")

def save_ascii():
    """Lưu ASCII Art thành file văn bản."""
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

def copy_to_clipboard():
    """Sao chép ASCII Art vào clipboard."""
    ascii_content = txt_ascii.get(1.0, tk.END).strip()
    if not ascii_content:
        messagebox.showerror("Lỗi", "Không có dữ liệu ASCII để sao chép.")
        return

    root.clipboard_clear()
    root.clipboard_append(ascii_content)
    root.update()  # Đảm bảo clipboard được cập nhật
    messagebox.showinfo("Thành công", "ASCII Art đã được sao chép vào clipboard.")

def reset_app():
    """Đặt lại giao diện về trạng thái ban đầu."""
    lbl_original.config(image="")
    lbl_original.image = None
    txt_ascii.delete(1.0, tk.END)
    btn_save.config(state=tk.DISABLED)
    btn_copy.config(state=tk.DISABLED)
    btn_reset.config(state=tk.DISABLED)

# Tạo giao diện chính
root = tk.Tk()
root.title("Chuyển đổi ảnh sang ASCII")
root.geometry("900x700")
root.configure(bg="#f0f0f0")

# Khung hình ảnh gốc
frame_original = tk.LabelFrame(root, text="Ảnh gốc", padx=10, pady=10, bg="#ffffff", font=("Arial", 12, "bold"))
frame_original.pack(side=tk.LEFT, padx=20, pady=20)

lbl_original = tk.Label(frame_original, bg="#ffffff")
lbl_original.pack()

# Khung ASCII art
frame_ascii = tk.LabelFrame(root, text="ASCII Art", padx=10, pady=10, bg="#ffffff", font=("Arial", 12, "bold"))
frame_ascii.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.BOTH, expand=True)

scroll_y = tk.Scrollbar(frame_ascii, orient=tk.VERTICAL)
scroll_x = tk.Scrollbar(frame_ascii, orient=tk.HORIZONTAL)

txt_ascii = tk.Text(frame_ascii, wrap=tk.NONE, font=("Courier", 10), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set, bg="#f7f7f7")
txt_ascii.pack(fill=tk.BOTH, expand=True)

scroll_y.config(command=txt_ascii.yview)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
scroll_x.config(command=txt_ascii.xview)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

# Khung nhập và nút chức năng
frame_controls = tk.Frame(root, bg="#f0f0f0")
frame_controls.pack(side=tk.BOTTOM, pady=10)

tk.Label(frame_controls, text="Độ rộng ASCII:", bg="#f0f0f0", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
entry_width = tk.Entry(frame_controls, width=5, font=("Arial", 10))
entry_width.insert(0, "100")  # Giá trị mặc định
entry_width.pack(side=tk.LEFT, padx=5)

btn_open = tk.Button(frame_controls, text="Chọn ảnh", command=open_image, bg="#4caf50", fg="white", font=("Arial", 10, "bold"))
btn_open.pack(side=tk.LEFT, padx=10)

btn_save = tk.Button(frame_controls, text="Lưu ASCII", command=save_ascii, state=tk.DISABLED, bg="#2196f3", fg="white", font=("Arial", 10, "bold"))
btn_save.pack(side=tk.LEFT, padx=10)

btn_copy = tk.Button(frame_controls, text="Sao chép ASCII", command=copy_to_clipboard, state=tk.DISABLED, bg="#ff9800", fg="white", font=("Arial", 10, "bold"))
btn_copy.pack(side=tk.LEFT, padx=10)

btn_reset = tk.Button(frame_controls, text="Đặt lại", command=reset_app, state=tk.DISABLED, bg="#f44336", fg="white", font=("Arial", 10, "bold"))
btn_reset.pack(side=tk.LEFT, padx=10)

root.mainloop()
