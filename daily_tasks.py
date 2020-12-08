import datetime
import os
import secrets
import shutil

# Backup database
shutil.copy2('database.db', 'database.db.bak')

# Generate new secret key
secret = secrets.token_hex(48)  # 384 bits
with open('secret_key.txt', 'w') as file:
    file.write(secret)

# rotate logs
timestamp = datetime.date.strftime(datetime.datetime.now(), "%d-%m-%Y")
shutil.copy2("logs/application.log", f"logs/{timestamp}-application.log")
os.remove("logs/application.log")