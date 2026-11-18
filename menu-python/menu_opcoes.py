# -*- coding: utf-8 -*-
"""
Programa de Menu de Opções em Python.

Opções:
 1 - Nome e Sobrenome do usuário (mostra o sobrenome antes do nome)
 2 - Calculadora
 3 - Média (4 notas, média e menção MB, B, R, I)
 4 - Hipotenusa
 5 - Triângulo
 6 - Equação do 2º Grau
 7 - Tabuada (escolher qual, de quanto até quanto)
 8 - Joguinho da Adivinhação (0 a 100)
 9 - Sair
"""

import math
import random


# ---------------------------------------------------------------------------
# Funções auxiliares de leitura
# ---------------------------------------------------------------------------
def ler_float(mensagem):
    """Lê um número real, repetindo a pergunta até o valor ser válido."""
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("  Valor inválido! Digite um número.")


def ler_int(mensagem):
    """Lê um número inteiro, repetindo a pergunta até o valor ser válido."""
    while True:
        valor = input(mensagem).strip()
        try:
            return int(valor)
        except ValueError:
            print("  Valor inválido! Digite um número inteiro.")


def fmt(numero):
    """Formata um número: sem casas decimais se for inteiro, senão 2 casas."""
    if float(numero).is_integer():
        return str(int(numero))
    return f"{numero:.2f}"


def titulo(texto):
    print()
    print("=" * 50)
    print(texto.center(50))
    print("=" * 50)


def pausa():
    input("\nPressione ENTER para voltar ao menu...")


# ---------------------------------------------------------------------------
# 1 - Nome e Sobrenome
# ---------------------------------------------------------------------------
def nome_sobrenome():
    titulo("NOME E SOBRENOME")
    nome = input("Digite o seu nome: ").strip()
    sobrenome = input("Digite o seu sobrenome: ").strip()
    print(f"\nSobrenome, Nome: {sobrenome.upper()}, {nome.title()}")
    print(f"Forma completa invertida: {sobrenome.title()} {nome.title()}")


# ---------------------------------------------------------------------------
# 2 - Calculadora
# ---------------------------------------------------------------------------
def calculadora():
    titulo("CALCULADORA")
    n1 = ler_float("Digite o 1º número: ")
    n2 = ler_float("Digite o 2º número: ")
    print("\nOperações:  +  Soma   -  Subtração   *  Multiplicação")
    print("            /  Divisão   **  Potência")
    op = input("Escolha a operação: ").strip()

    if op == "+":
        resultado = n1 + n2
    elif op == "-":
        resultado = n1 - n2
    elif op == "*":
        resultado = n1 * n2
    elif op == "/":
        if n2 == 0:
            print("\nErro: não é possível dividir por zero!")
            return
        resultado = n1 / n2
    elif op == "**":
        resultado = n1 ** n2
    else:
        print("\nOperação inválida!")
        return

    print(f"\nResultado: {fmt(n1)} {op} {fmt(n2)} = {fmt(resultado)}")


# ---------------------------------------------------------------------------
# 3 - Média com menção
# ---------------------------------------------------------------------------
def mencao(media):
    if media >= 9:
        return "MB", "Muito Bom"
    elif media >= 7:
        return "B", "Bom"
    elif media >= 5:
        return "R", "Regular"
    else:
        return "I", "Insuficiente"


def media_notas():
    titulo("MÉDIA DAS NOTAS")
    notas = []
    for i in range(1, 5):
        while True:
            nota = ler_float(f"Digite a {i}ª nota (0 a 10): ")
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            print("  A nota deve estar entre 0 e 10!")

    media = sum(notas) / 4
    sigla, descricao = mencao(media)
    print(f"\nNotas: {', '.join(fmt(n) for n in notas)}")
    print(f"Média: {media:.2f}")
    print(f"Menção: {sigla} ({descricao})")
    print("\nCritério: MB >= 9 | B >= 7 | R >= 5 | I < 5")


# ---------------------------------------------------------------------------
# 4 - Hipotenusa
# ---------------------------------------------------------------------------
def hipotenusa():
    titulo("HIPOTENUSA")
    print("Teorema de Pitágoras: h² = a² + b²\n")
    while True:
        a = ler_float("Digite o cateto a: ")
        b = ler_float("Digite o cateto b: ")
        if a > 0 and b > 0:
            break
        print("  Os catetos devem ser maiores que zero!\n")
    h = math.sqrt(a ** 2 + b ** 2)
    print(f"\nh² = {fmt(a)}² + {fmt(b)}² = {fmt(a ** 2 + b ** 2)}")
    print(f"Hipotenusa = {fmt(h)}")


# ---------------------------------------------------------------------------
# 5 - Triângulo
# ---------------------------------------------------------------------------
def triangulo():
    titulo("TRIÂNGULO")
    a = ler_float("Digite o lado A: ")
    b = ler_float("Digite o lado B: ")
    c = ler_float("Digite o lado C: ")

    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        print("\nOs lados informados NÃO formam um triângulo!")
        print("(cada lado deve ser menor que a soma dos outros dois)")
        return

    print("\nOs lados formam um triângulo!")
    if a == b == c:
        tipo = "EQUILÁTERO (3 lados iguais)"
    elif a == b or a == c or b == c:
        tipo = "ISÓSCELES (2 lados iguais)"
    else:
        tipo = "ESCALENO (3 lados diferentes)"
    print(f"Classificação: {tipo}")

    # Perímetro e área (fórmula de Heron)
    perimetro = a + b + c
    s = perimetro / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Perímetro: {fmt(perimetro)}")
    print(f"Área: {area:.2f}")


# ---------------------------------------------------------------------------
# 6 - Equação do 2º Grau
# ---------------------------------------------------------------------------
def equacao_2grau():
    titulo("EQUAÇÃO DO 2º GRAU")
    print("Forma: ax² + bx + c = 0\n")
    a = ler_float("Digite o valor de a: ")
    while a == 0:
        print("  'a' não pode ser zero numa equação do 2º grau!")
        a = ler_float("Digite o valor de a: ")
    b = ler_float("Digite o valor de b: ")
    c = ler_float("Digite o valor de c: ")

    delta = b ** 2 - 4 * a * c
    print(f"\nEquação: {fmt(a)}x² + ({fmt(b)})x + ({fmt(c)}) = 0")
    print(f"Δ = b² - 4ac = {fmt(delta)}")

    if delta < 0:
        print("Δ < 0: a equação NÃO possui raízes reais.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Δ = 0: a equação possui uma raiz real.\nx = {fmt(x)}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Δ > 0: a equação possui duas raízes reais.")
        print(f"x1 = {fmt(x1)}")
        print(f"x2 = {fmt(x2)}")


# ---------------------------------------------------------------------------
# 7 - Tabuada
# ---------------------------------------------------------------------------
def tabuada():
    titulo("TABUADA")
    numero = ler_int("Qual tabuada deseja ver? ")
    inicio = ler_int("De quanto? ")
    fim = ler_int("Até quanto? ")
    if inicio > fim:
        inicio, fim = fim, inicio

    print(f"\nTabuada do {numero} (de {inicio} até {fim}):\n")
    for i in range(inicio, fim + 1):
        print(f"  {numero:>3} x {i:>3} = {numero * i:>5}")


# ---------------------------------------------------------------------------
# 8 - Joguinho da Adivinhação
# ---------------------------------------------------------------------------
def adivinhacao():
    titulo("JOGO DA ADIVINHAÇÃO")
    print("Pensei em um número entre 0 e 100. Tente adivinhar!\n")
    secreto = random.randint(0, 100)
    tentativas = 0

    while True:
        palpite = ler_int("Seu palpite: ")
        if palpite < 0 or palpite > 100:
            print("  Digite um número entre 0 e 100!")
            continue
        tentativas += 1
        if palpite < secreto:
            print("  É MAIOR que", palpite)
        elif palpite > secreto:
            print("  É MENOR que", palpite)
        else:
            print(f"\nPARABÉNS! Você acertou! O número era {secreto}.")
            print(f"Você tentou {tentativas} vez(es) até acertar.")
            break


# ---------------------------------------------------------------------------
# Menu principal
# ---------------------------------------------------------------------------
def mostrar_menu():
    print()
    print("=" * 50)
    print("MENU PRINCIPAL".center(50))
    print("=" * 50)
    print(" 1 - Nome e Sobrenome")
    print(" 2 - Calculadora")
    print(" 3 - Média")
    print(" 4 - Hipotenusa")
    print(" 5 - Triângulo")
    print(" 6 - Equação do 2º Grau")
    print(" 7 - Tabuada")
    print(" 8 - Joguinho da Adivinhação")
    print(" 9 - Sair")
    print("=" * 50)


def main():
    opcoes = {
        "1": nome_sobrenome,
        "2": calculadora,
        "3": media_notas,
        "4": hipotenusa,
        "5": triangulo,
        "6": equacao_2grau,
        "7": tabuada,
        "8": adivinhacao,
    }

    while True:
        mostrar_menu()
        opcao = input("    Digite a opção desejada: ").strip()

        if opcao == "9":
            print("\nObrigado por usar o programa. Até logo!")
            break
        elif opcao in opcoes:
            opcoes[opcao]()
            pausa()
        else:
            print("\nOpção inválida! Escolha um número de 1 a 9.")


if __name__ == "__main__":
    main()
