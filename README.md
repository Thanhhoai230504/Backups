# Tự động Backup Database Hằng Ngày + Gửi Mail Thông Báo

Dự án này tự động sao lưu (backup) các file cơ sở dữ liệu (`.sql`, `.sqlite3`) vào lúc **00:00 AM mỗi ngày** và **gửi email thông báo** về kết quả (thành công hoặc thất bại).

---

## Tính năng

- Tự động sao lưu các file `.sql`, `.sqlite3` trong thư mục `./databases`.
- Lưu file backup có timestamp vào thư mục `./backups`.
- Gửi email thông báo thành công/thất bại tới người nhận.
- Lên lịch chạy tự động mỗi ngày lúc **00:00 AM**.

---

## Công nghệ sử dụng

- **Python 3**: Ngôn ngữ lập trình chính.
- **`schedule`**: Lập lịch chạy task.
- **`python-dotenv`**: Đọc biến môi trường từ file `.env`.
- **`smtplib` + `email`**: Gửi email thông báo.

---

## Cấu trúc thư mục

📁 BT_BUOI5  
├── `backup.py` # Hàm thực hiện backup database  
├── `send_email.py` # Hàm gửi email thông báo kết quả backup  
├── `scheduler.py` # File chính chạy định kỳ để tự động backup  
├── `.env` # Chứa thông tin email  
├── `requirements.txt` # Danh sách các thư viện cần thiết  
├── `databases/` # Chứa các file database gốc  
└── `backups/` # Được tạo tự động, chứa các file backup

---

## Hướng dẫn cài đặt

### 1. Cài đặt Python

- Tải và cài đặt Python 3 từ [python.org](https://www.python.org/downloads/).
- Đảm bảo đã thêm Python vào `PATH` khi cài đặt.

### 2. Clone dự án

Sử dụng lệnh sau để clone dự án về máy:

```bash
git clone https://github.com/your-username/BT_BUOI5.git
cd BT_BUOI5
```

### 3. Cài đặt thư viện

Cài đặt các thư viện cần thiết từ file requirements.txt:

### 4. Cấu hình file .env

Tạo file .env trong thư mục gốc và thêm thông tin email như sau:
sender_email=your_email@gmail.com
receiver=receiver_email@gmail.com
app_password=your_app_password

sender_email: Email của bạn (người gửi).
receiver: Email người nhận.
app_password: Mật khẩu ứng dụng (App Password) của email (nếu dùng Gmail, bạn cần bật chế độ App Password trong tài khoản Google).

### 5. Tạo thư mục cần thiết

Đảm bảo các thư mục sau tồn tại:

databases/: Chứa các file database cần backup.
backups/: Thư mục này sẽ được tạo tự động để lưu file backup.

### 6.Chạy chương trình

Chạy file scheduler.py để bắt đầu quá trình tự động backup:



Ghi chú
Đảm bảo máy tính của bạn đang chạy vào thời điểm 00:00 AM để chương trình hoạt động.

```python
schedule.every().day.at("00:00").do(job)
```
Nếu muốn thay đổi thời gian backup, sửa dòng sau trong file scheduler.py:
Thay "00:00" bằng thời gian mong muốn (định dạng 24 giờ, ví dụ: "14:30" cho 2:30 PM).

Nếu bạn gặp vấn đề hoặc có câu hỏi, vui lòng liên hệ qua email: nguyenthanhhoai230504@gmail.com.

 