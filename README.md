# KeyLogger-Mailer

## Overview
This project is a Python-based keylogger that logs keystrokes and periodically sends the log file via email. It is designed for educational purposes only and should be used responsibly.

## Features
- Logs all keystrokes, including special keys (like space, enter, etc.).
- Saves logs to a uniquely named text file based on the timestamp of execution.
- Sends logs via email at a specified interval.
- Deletes logs after sending (configurable).
- Secure credential management using environment variables.

## Ethical Considerations
- This tool is intended **strictly for educational purposes**.
- You must obtain **explicit permission** from the system owner before use.
- Unauthorized use of keyloggers is **illegal and unethical**.

## Requirements
- Python 3.x
- Required Python libraries:
  ```bash
  pip install pynput schedule dotenv
  ```

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone github.com/Zeousultra/KeyLogger-Mailer
   cd KeyLogger-Mailer
   ```
2. Set up environment variables in a `.env` file:
   ```plaintext
   SENDER_EMAIL=your-email@gmail.com
   SENDER_PASSWORD=your-email-password
   RECEIVER_EMAIL=receiver-email@gmail.com
   ```
3. Run the keylogger:
   ```bash
   python KeyLogger-Mailer.py
   ```

## Log Files
- Keystrokes are logged in `keylog_<timestamp>.txt`.
- The file is automatically deleted after being emailed (configurable in the script).

  
## Customization
- Change the EMAIL_INTERVAL in KeyLogger-Mailer.py to adjust email frequency.
- Set DELETE_LOG_AFTER_EMAIL = False if you want to keep logs after sending.

## Disclaimer
Use this project **responsibly and ethically**. The creator is not responsible for misuse. Ensure compliance with local laws and regulations regarding monitoring software.
