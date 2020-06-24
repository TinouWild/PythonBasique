import socket


# Lire le fichier texte et récupérer une liste de machines
def read_file():
    return ""


# Scanner les ports d'une machine
def scan_machine(machine):
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(("192.168.0.1", port))
        if 0 == result:
            print("Port: {} Open".format(port))
        sock.close()
    return ''
