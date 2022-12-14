import socket
import os
import shutil
import csv
import re

dirname = os.path.join(os.getcwd(), 'docs')
END_FLAG = b"$$STREAM_FILE_END_FLAG$$"
FAIL_FLAG = b'$FAILED$'
PORT = 6161
global_root = os.path.join(os.getcwd())
usersfile = os.path.join(global_root, "users.csv")
log_file = os.path.join(global_root, "log.txt")