# 🎭 Evil_Keylogger 🎭

**epykey.py** is a Python script designed to capture keystrokes and send them to a remote server or save them locally in case of connection issues.

⚠️ **This project is strictly for educational and ethical purposes.** Using this script for malicious activities is prohibited and may violate applicable laws.

---

## ✨ Features

- 📌 Real-time keystroke capture.  
- 🌐 Sends data to a configured server via POST requests.  
- 💾 Local backup in case of server connection failure.  
- 🔄 Runs in the background and periodically sends data.  

---

## 🛠️ Prerequisites

- **Python 3.7+**  
- The following Python libraries:  

  ```bash
  pip install pynput requests
  ```
    pynput: to capture keyboard events.

    requests: to send HTTP requests.

    threading: to manage periodic tasks.

    json: to format data into JSON.

⚙️ Configuration

    Open the file epykey.py.

    Modify the following values:
    ```python
      ip_address = "IP"  # Replace with your server's IP address.
      port_number = "Port"  # Replace with your server's port.
      time_interval = 10  # Set the interval for sending data (in seconds).
    ```
If no server is configured, the keystrokes will be saved locally in a file named keystrokes_backup.txt.


🚀 Usage

    Run the script in a terminal:
    ```bash
    python3 epykey.py
    ```
    The keylogger will start capturing keystrokes.
    Press ESC to stop.

    Data will be sent to the configured server or saved locally.

⚠️ Warnings

    This script is intended for responsible and legal use only.

    Any unauthorized or malicious use is strictly prohibited.

🤝 Contributions

Contributions to enhance this project are welcome! 🎉

    Submit a pull request.

    Open an issue on this GitHub repository.



  
