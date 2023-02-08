# Spykey- A keylogger
A keylogger is a program that records every keystroke made on a computer and is often used for malicious purposes. However, it can also be used for legitimate purposes such as monitoring computer usage in a company or tracking the productivity of remote workers. The keylogger project is made with Python and it records every keystroke made on a computer and stores it in a *key_log.txt* file. This log file can then be accessed by the user to view the recorded data. The keylogger runs in the background and can be made invisible to the user, making it ideal for monitoring purposes. The project I have made is GUI based which has buttons *START* & *STOP* for keylogging activities. It also shows the status of keylogging activities.

Along with the key-logger project I have also made a project to detect the keylogger which is *spykey_cop.py*. When executed it looks for files in current folder with potential keylogging activities. 

User of this program are advised to use or modify this program only for educational purposes. Any illegal modification or usage of this program or any part of this program will be sole responsibility of the user or modifier and not the author. Author discourages illegal activities using this program.

Usage:  
Clone the repository on your local device using Git.  
>git clone https://github.com/atharva-shigvan/Spykey.git  

Give the neccessary executable permissions to the files
>chmod +x spykey.py spykey_cop.py

Install the required libraries of python for succesful

For getting the keylogs execute **spykey.py**
> python3 spykey.py

For detecting any file of potential keylogging file in current directory execute **spykey_cop.py**
>python3 spykey_cop.py

All the keylogged input will be saved in a file name 
>key_log.txt
