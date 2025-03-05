# KeyLogger-Mailer

## Overview
This project is a simple keylogger that records keystrokes and automatically sends the log file to a specified email address. It is intended for **educational purposes only** and should only be used with the explicit permission of the system owner.

## Features
- Logs all keystrokes, including special keys (e.g., Enter, Space, etc.).
- Saves logs in a uniquely named file based on timestamp.
- Sends logs to a specified email upon stopping the keylogger.
- Secure email sending via SMTP with TLS encryption.

## Ethical Considerations
🔴 **Use this project responsibly and ethically. Unauthorized use of keyloggers is illegal!**

## Requirements
- Python 3.x
- `pynput` library for key logging
- `smtplib` for email functionality
- A Gmail account (with App Password enabled for secure login)

### Install Dependencies:
```sh
pip install pynput
```

## Usage
### 1. Clone the repository:
```sh
git clone https://github.com/Zeousultra/KeyLogger-Mailer
cd KeyLogger-Mailer
```

### 2. Configure Email Credentials
Edit `keylogger.py` and replace:
- `EMAIL_ADDRESS` with your Gmail
- `EMAIL_PASSWORD` with your **Google App Password**
- `SEND_TO` with the recipient's email

### 3. Run the keylogger:
```sh
python keylogger.py
```
Press `ESC` to stop logging and send the email.

## Log Files
- Logs are saved as `keylog_<timestamp>.txt`
- Automatically emailed to the specified recipient.

## Disclaimer
This project is for **educational and ethical use only**. The creator is **not responsible** for any misuse. Always comply with legal and ethical guidelines.
