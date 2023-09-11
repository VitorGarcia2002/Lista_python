"""
Jogo da velha com um tabuleiro NxN onde o tamanho do tabuleiro é decidido pelo jogador

Estratégia utlizada:
- A abordagem nesse exercicio foi um pouco parecida com o do primeiro tabuleiro,mas nesse as posições são definidas por numeros de 1 até o valor do tamanho do tabuleiro
- Unica diferença é que nesse não foi possível inserir um tabuleiro inicial que mostra as posições e os seus respectivos numeros, pois o tamanho do tabuleiro não é fixo
- Assim como no primeiro foi feito uma função que imprime o tabuleiro
- Em seguida na função "logica_jogo" é pedido para o úsuario informar o tamanho do tabuleiro desejado, imprimindo o tabuleiro dentro da função while e iniciando o jogo pelo jogador "x" 
- A verificação é feita semelhante ao tabuleiro 4x4, se houve algum vencedor ou empate ou se a posição escolhida por "x" é valida
- Após toda a verificação é trocada a vez para o jogador "o"
- A grande diferença desse codico está na verificação de vitória ou empate, pois o tamanho do tabuleiro não é estatico então foi necessario criar estruturas que percorrem o tabuleiro
e verificam se houve alguma vitória em colunas, linhas ou diagonais

"""
def imprimir_tabuleiro(tabuleiro):
    """
    Função utilizada para imprimir o tabuleiro
    """
    n = len(tabuleiro)
    tamanho = int(n ** 0.5) 
    for i in range(n):
        print(tabuleiro[i], end=" ")
        if (i + 1) % tamanho == 0:
            print(" ")

def logica_jogo():
    """
    Função que executa a logica do jogo, agora maior que a do tabuleiro anterior, devido as dimensões não serem fixas, mas a logica é parecida
    """
    tamanho_tabuleiro = int(input("Escolha o tamanho do tabuleiro (ex. 3 para 3x3): "))
    if tamanho_tabuleiro < 2:
        print("Tamanho do tabuleiro inválido. Deve ser pelo menos 2x2.")
        return

    total_posicoes = tamanho_tabuleiro ** 2
    tabuleiro = ["_"] * total_posicoes
    jogador = "x"
    jogo = True

    while jogo == True:
        imprimir_tabuleiro(tabuleiro)
        escolha = int(input(f"Escolha uma posição de 1 a {total_posicoes}: ")) - 1

        if 0 <= escolha < total_posicoes and tabuleiro[escolha] == "_":
            tabuleiro[escolha] = jogador
        else:
            print("Escolha inválida. Tente novamente.")

        for i in range(0, total_posicoes, tamanho_tabuleiro):
            linha = tabuleiro[i:i + tamanho_tabuleiro]
            if all(celula == jogador for celula in linha):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador} venceu!")
                jogo = False
                break

        for coluna in range(tamanho_tabuleiro):
            coluna_check = [tabuleiro[i * tamanho_tabuleiro + coluna] for i in range(tamanho_tabuleiro)]
            if all(celula == jogador for celula in coluna_check):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador} venceu!")
                jogo = False
                break

        if all(tabuleiro[i * tamanho_tabuleiro + i] == jogador for i in range(tamanho_tabuleiro)):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador} venceu!")
            jogo = False
        elif all(tabuleiro[i * tamanho_tabuleiro + (tamanho_tabuleiro - 1 - i)] == jogador for i in range(tamanho_tabuleiro)):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador} venceu!")
            jogo = False

        if "_" not in tabuleiro:
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            jogo = False

        jogador = "o" if jogador == "x" else "x"

logica_jogo()

