# Tự động Backup Database Hằng Ngày + Gửi Mail Thông Báo

Dự án này tự động sao lưu (backup) các file cơ sở dữ liệu (`.sql`, `.sqlite3`) vào lúc **00:00 AM mỗi ngày** và **gửi email thông báo** về kết quả (thành công hoặc thất bại).

## Tính năng

- Tự động sao lưu các file `.sql`, `.sqlite3` trong thư mục `./databases`
- Lưu file backup có timestamp vào thư mục `./backups`
- Gửi email thông báo thành công/thất bại tới người nhận
- Lên lịch chạy tự động mỗi ngày lúc **00:00 AM**

---

## Công nghệ sử dụng

- Python 3
- `schedule` – lập lịch chạy task
- `python-dotenv` – đọc biến môi trường từ file `.env`
- `smtplib` + `email` – gửi mail

---

## Cấu trúc thư mục

. ├── backup.py # Hàm backup database ├── send_email.py # Hàm gửi email thông báo ├── scheduler.py # File chạy chính để tự động backup ├── .env # Thông tin email (KHÔNG đẩy lên GitHub) ├── requirements.txt # Danh sách thư viện cần cài ├── databases/ # Chứa các file database gốc └── backups/ # Tự tạo, chứa các file backup