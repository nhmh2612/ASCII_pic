# Chuyển đổi ảnh sang ASCII Art

Ứng dụng giao diện đồ họa (GUI) sử dụng Python và thư viện Tkinter để chuyển đổi ảnh thành ASCII Art. Ứng dụng hỗ trợ nhiều định dạng ảnh và cho phép người dùng tùy chỉnh độ rộng ASCII trực tiếp trên giao diện.

## Tính năng chính
- Chọn ảnh từ máy tính và chuyển đổi sang ASCII Art.
- Hiển thị ASCII Art trên giao diện.
- Tùy chỉnh độ rộng ASCII để thay đổi độ chi tiết của ASCII Art.
- Lưu ASCII Art dưới dạng tệp văn bản (`.txt`).
- Sao chép ASCII Art vào clipboard để sử dụng ngay.

## Hướng dẫn cài đặt

### Yêu cầu hệ thống
- Python 3.7 trở lên.
- Các thư viện Python:
  - `tkinter` (đi kèm với Python)
  - `Pillow` (thư viện xử lý ảnh)

### Cài đặt thư viện
Sử dụng pip để cài đặt thư viện cần thiết:
```bash
pip install Pillow
```

### Chạy ứng dụng
1. Tải mã nguồn xuống và lưu vào tệp Python, ví dụ: `image_to_ascii.py`.
2. Mở terminal hoặc command prompt, điều hướng đến thư mục chứa tệp.
3. Thực thi tệp bằng lệnh sau:
   ```bash
   python image_to_ascii.py
   ```
Khi chạy, cửa sổ giao diện sẽ xuất hiện, cho phép bạn thực hiện các bước chuyển đổi ảnh sang ASCII Art.
