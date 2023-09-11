"""
Jogo da velha com um tabuleiro 4x4

Estratégia utlizada:
- A ideia inicial foi de primeiramente mostrar um tabuleiro 4x4 com cada casa recebendo um número de 1 a 16
- E depois é pedido para o jogador inicial escolher o número referente a posição em que ele quer ocupar
- Após o jogador "x" escolher sua posição, ocorre uma verificação se a posição é valida ou não, e se houve vencedor ou empate
- Em seguida troca a vez para o jogador "o" e repete o processo de escolher a posição do tabuleiro
- Quando houver algum vencedor ou empate o valor do while é alterado para "false" e é impresso na tela o resultado do jogo
"""

def imprimir_tabuleiro(tabuleiro):
    """
    Essa é a função utliziada para imprimir o tabuleiro
    """
    for i in range(len(tabuleiro)):
        print(tabuleiro[i], end=" ")
        if i % 4 == 3:
            print(" ")

def logica_jogo():
    """
    Essa é a função onde ocorre toda a logica do jogo, mostrando o tabuleiro atualizado a cada rodada, verifica se houve algum vencedor ou se houve empate
    e faz a alternancia entre os dois jogadores 
    """

    tabuleiro = ["_"] * 16
    jogador = "x"
    jogo = True

    while jogo == True:
        imprimir_tabuleiro(tabuleiro)
        escolha = int(input("Escolha uma posição de 1 a 16: "))

        if 1 <= escolha <= 16 and tabuleiro[escolha - 1] == "_":
            tabuleiro[escolha - 1] = jogador
        else:
            print("Escolha inválida. Tente novamente.")

        if (
            (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == tabuleiro[3] != "_")
            or (tabuleiro[4] == tabuleiro[5] == tabuleiro[6] == tabuleiro[7] != "_")
            or (tabuleiro[8] == tabuleiro[9] == tabuleiro[10] == tabuleiro[11] != "_")
            or (tabuleiro[12] == tabuleiro[13] == tabuleiro[14] == tabuleiro[15] != "_")
            or (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == tabuleiro[12] != "_")
            or (tabuleiro[1] == tabuleiro[5] == tabuleiro[9] == tabuleiro[13] != "_")
            or (tabuleiro[2] == tabuleiro[6] == tabuleiro[10] == tabuleiro[14] != "_")
            or (tabuleiro[3] == tabuleiro[7] == tabuleiro[11] == tabuleiro[15] != "_")
            or (tabuleiro[0] == tabuleiro[5] == tabuleiro[10] == tabuleiro[15] != "_")
            or (tabuleiro[3] == tabuleiro[6] == tabuleiro[9] == tabuleiro[12] != "_")
        ):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador} venceu!")
            jogo = False
        elif "_" not in tabuleiro:
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            jogo = False

        jogador = "o" if jogador == "x" else "x"

print("Escolha uma casa de 1 a 16 de acordo com o tabuleiro a seguir")
print("1  2  3  4")
print("5  6  7  8")
print("9  10 11 12")
print("13 14 15 16")

logica_jogo()
