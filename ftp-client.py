import socket
import re
import os

HOST = 'localhost'
PORT = 6161
END_FLAG = b"$$STREAM_FILE_END_FLAG$$"
FAIL_FLAG = b'$FAILED$'
login = input("Введите логин: ")
password = input("Введите пароль: ")
# login = "admin"
# password = "admin"
current_directory = "\\"
