# Nome: Marcela de Mendonca
# Projeto: Calculadora simples com Python
# Objetivo: Entregar uma calculadora simples que faça operações com adição, subtração, multiplicação e divisão.


from colorama import init, Fore, Back, Style

# Inicializa a biblioteca Colorama
init()

# Definição de cores para os textos e fundos
cor_texto = Fore.WHITE
cor_fundo = Back.MAGENTA
cor_resultado = Back.GREEN

''' Cores disponíveis: 
Fore.BLACK       Back.BLACK
Fore.RED:        Back.RED
Fore.GREEN:      Back.GREEN
Fore.YELLOW      Back.YELLOW
Fore.BLUE        Back.BLUE
Fore.MAGENTA     Back.MAGENTA
Fore.CYAN        Back.CYAN
Fore.WHITE       Back.WHITE '''

# Função para realizar as operações


def calcular(num1, num2, operador):
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        resultado = num1 / num2
    else:
        resultado = None
    return resultado


# Loop para pedir ao usuário os números e operador
while True:
    # Limpa a tela
    print(Style.RESET_ALL)
    print(cor_fundo + cor_texto + " CALCULADORA " + Style.RESET_ALL)
    print()

    # Lê o primeiro número
    try:
        num1 = float(input("Digite o primeiro número: "))
    except ValueError:
        print(Fore.RED + "Valor inválido!" + Style.RESET_ALL)
        continue

    # Lê o operador
    operador = input("Digite o operador (+, -, *, /): ")
    if operador not in ["+", "-", "*", "/"]:
        print(Fore.RED + "Operador inválido!" + Style.RESET_ALL)
        continue

    # Lê o segundo número
    try:
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print(Fore.RED + "Valor inválido!" + Style.RESET_ALL)
        continue

    # Calcula o resultado
    resultado = calcular(num1, num2, operador)

    # Imprime o resultado
    if resultado is not None:
        print(cor_resultado + cor_texto +
              f"Resultado: {resultado}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Operação inválida!" + Style.RESET_ALL)

    # Pergunta se o usuário quer continuar
    continuar = input("Deseja continuar? (s/n) ")
    if continuar.lower() != "s":
        break
