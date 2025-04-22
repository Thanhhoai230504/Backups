import schedule
import time
from backup import backup_database
from send_email import send_email
from dotenv import load_dotenv
import os


load_dotenv()
sender_email = os.getenv("sender_email")
receiver_email = os.getenv("receiver")
app_password = os.getenv("app_password")

def job():
    success, message = backup_database()
    subject = "THÔNG BÁO BACKUP DATABASE"

    if success:
        full_message = f"[THÀNH CÔNG] {message}"
    else:
        full_message = f"[THẤT BẠI] {message}"

    send_email(sender_email, receiver_email, subject, full_message, app_password)
    print(full_message)

schedule.every().day.at("00:00").do(job)

print("Hệ thống backup đã sẵn sàng chạy mỗi 00:00 AM...")

while True:
    schedule.run_pending()
    time.sleep(60)
