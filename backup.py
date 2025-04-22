import os
import shutil
from datetime import datetime

def backup_database():
    try:
        db_dir = "./databases"
        backup_dir = "./backups"
        os.makedirs(backup_dir, exist_ok=True)

        for file in os.listdir(db_dir):
            if file.endswith(".sql") or file.endswith(".sqlite3"):
                # đường dẫn thư mục chứa file gốc cần backup
                # os.path.join() dùng để nối hai phần lại thành đường dẫn đầy đủ đến file gốc.
                src_path = os.path.join(db_dir, file)

                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
                backup_filename = f"{file}_backup_{timestamp}"
                dest_path = os.path.join(backup_dir, backup_filename)

                shutil.copy2(src_path, dest_path)

        return True, "Backup thành công!"
    except Exception as e:
        return False, f"Backup thất bại: {str(e)}"
