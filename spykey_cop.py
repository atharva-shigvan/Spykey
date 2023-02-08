import os
import fnmatch

def detect_keylogger():
    current_dir = os.getcwd()
    files = os.listdir(current_dir)

    keylogger_keywords = ['keylog*', 'key*log', 'key*stroke*log','key*','log*','*key*']
    for keyword in keylogger_keywords:
        for name in fnmatch.filter(files, keyword):
            if name != "spykey_cop.py":
                file_path = os.path.join(current_dir, name)
                print(f"[ALERT] Potential keylogger file detected: {file_path}")
    return

    print("No keylogger detected")

if __name__ == '__main__':
    detect_keylogger()
