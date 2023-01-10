import socket
import sys
from datetime import datetime
from tqdm import tqdm 
import fade
import time

# Banner do grupo
print(fade.fire("""
 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓     ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒   ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░      ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░    ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░      ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░       ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░░       ░ ░ ░ ▒    ░░   ░   ░         ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
             ░ ░     ░                       ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
                                                ░    """))

print(fade.fire("""*********************************************************************************************************

Port Scanner made by Berg and Neres, 2022
https://www.linkedin.com/in/lucas-lintz-869075208/ 
https://github.com/Berg777

*********************************************************************************************************
"""))

time.sleep(1)

print(fade.fire("Carregando Port Scanner"))

# Barra de carregamento
for i in tqdm(range(30), colour = "yellow"):
    time.sleep(0.05)

pegar_ip = input(fade.purpleblue("Qual ip você deseja escanear? \n"))

time.sleep(1)

def scanner_no_ip(endereco_ip, exibir_portas_fechadas = 0):
    # Realizar a varredura nas portas de um endereço IP
    
    # Portas que receberão uma tentativa de conexão
    porta_inicial = int(input(fade.purpleblue("Digite a porta inicial: ")))
    porta_final = int(input(fade.purpleblue("Digite a porta final: ")))

    print(fade.purpleblue(f"Scanner no IP {endereco_ip} da porta {porta_inicial} até {porta_final} "))
    time.sleep(1)

    # Escaneando
    try:
        for porta in range(porta_inicial, porta_final):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((endereco_ip, porta))
            if result == 0:
                print(fade.purpleblue(f"tcp/{porta} {socket.getservbyport(porta)} open"))
            else:
                if exibir_portas_fechadas > 0:
                    print(fade.purpleblue(f"tcp/{porta} closed"))
            sock.close()
    except KeyboardInterrupt:
        print(fade.fire("\nVocê pressionou <Ctrl> + <C>"))
        print(fade.fire("Saindo..."))
        sys.exit()

    except socket.gaierror:
        print(fade.fire("O hostname não pode ser resolvido"))
        sys.exit()

    except socket.error:
        print(fade.fire("Não foi possível conectar no servidor"))
        sys.exit()

# Execução principal do script
if __name__ == "__main__":
    # IP local da máquina

    # Buscando o IP de uma URL
    ip_do_alvo = socket.gethostbyname(pegar_ip)

    # Data e hora inicial do escaneamento
    t1 = datetime.now()

    scanner_no_ip(ip_do_alvo)

    # Data e hora final do escaneamento
    t2 = datetime.now()
    total = t2 - t1
    time.sleep(2)
    print(fade.greenblue(f"Scanner finalizado em: {total}"))
    
