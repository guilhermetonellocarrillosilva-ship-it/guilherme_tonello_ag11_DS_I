import colorama
from colorama import Fore, Style


colorama.init()

def exibir_alerta(nivel):
    """
    Define a cor e a mensagem com base no nível do reservatório.
    """
    
    situacoes = [
        "Muito baixo (crítico)", # Nível 1
        "Baixo",                # Nível 2
        "Médio",                # Nível 3
        "Alto",                 # Nível 4
        "Muito alto (alerta)"   # Nível 5
    ]
    
    
    cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE]

    
    indice = nivel - 1
    
    if 0 <= indice < len(situacoes):
        print(f"Status do Reservatório (Nível {nivel}): {cores[indice]}{situacoes[indice]}{Style.RESET_ALL}")
    else:
        print("Nível inválido detectado.")


def simular_sistema():
    print("--- SISTEMA DE MONITORAMENTO DE RESERVATÓRIO ---\n")
    
    
    niveis_leitura = [1, 2, 3, 4, 5]
    
    for nivel in niveis_leitura:
        exibir_alerta(nivel)

if __name__ == "__main__":
    simular_sistema()




