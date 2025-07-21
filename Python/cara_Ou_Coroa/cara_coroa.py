from random import choice
from time import sleep
import csv
import os

# Verifica se o arquivo ranking.csv já existe
arquivo_existe = os.path.exists('ranking.csv')

# -------------------------------
# Mensagens e textos fixos do jogo
# -------------------------------

introducao = ("""
    Bem vindo ao Cara Ou Coroa com Python, aqui você pode jogar por horas!
 ===============================
         MODOS DE JOGO         
===============================

 [1] PC vs PC          
      Dois computadores jogam entre si.

 [2] PC vs PLAYER      
      Você joga contra o computador.

 [3] PLAYER vs PLAYER  
      Dois jogadores humanos se enfrentam.

 [4] INSANIDADE ⚡      
      Um modo caótico e imprevisível.

 [5] COMPETIÇÃO  
      Os jogadores se enfrentam e competem pela maior pontuação.

 [6] RANKING    
      Exibição das pontuações do Modo Competição.

 [7] SAIR     
      Nossos jogos acabam por aqui!.

 ===============================

""")

finalmssg = (""""  
    🌟 Espero que tenha se divertido, jogador!
    ================================================
    ⏹️ Encerrando a sessão...
    💾 Salvando suas moedas imaginárias...
    🚀 Voltando para o lobby...

    Até a próxima rodada de sorte 🍀
    ================================================
""")

aixai = (""""  
    MODO 1: IA vs IA 🤖⚔️
    ===============================
    Conectando cérebros eletrônicos...
    Calculando probabilidades...
    A disputa entre máquinas vai começar!
""")

playerxai = ("""
    MODO 2: VOCÊ vs IA 🧠🆚🤖
    ===============================
    Posicione-se, jogador...
    A inteligência artificial está pronta.
    Que comece o duelo!
""")

playerxplayer = (""""  
    MODO 3: JOGADOR vs JOGADOR 🧑‍🤝‍🧑
    ===============================
    Que vença o mais sortudo!
    Dois jogadores entram...
    Apenas um sai vitorioso!
""")

insanidade = ("""
    MODO 4: INSANIDADE ⚡😵‍💫
    ===============================
    As regras são quebradas...
    O caos reina... 🍀💥
    Prepare-se para o inesperado!
""")

competicao = ("""
    MODO 5: COMPETIÇÃO 🏆
    ===============================
    Duelo com ranking e pontuação!
    Prepare-se para a batalha!
    """)

erro = ("""
    🤔 Você acabou de inventar um modo novo?
    Infelizmente ele ainda não foi programado.
    Tente um número válido, de 1 a 5.
""")

erro_none = ("""
    🤔 Você esqueceu de colocar um valor? Sem problema.
    Tente um número válido, de 1 a 5.
""")


# ------------------------------------------
# Funções dos modos de jogo
# Cada função implementa a lógica de um modo
# ------------------------------------------

def modo_ia_vs_ia():
    """Modo 1: Computador vs Computador, as duas IAs jogam entre si."""
    while True:
        escolhas = ['cara', 'coroa']
        jogada_ia1 = choice(escolhas)
        jogada_ia2 = choice([e for e in escolhas if e != jogada_ia1])
        resultado_moeda = choice(escolhas)
        print(aixai)
        sleep(1.8)  # introdução maior
        print(f'A escolha da IA-1 foi: {jogada_ia1}')
        sleep(1.2)
        print(f'A escolha da IA-2 foi: {jogada_ia2}')
        sleep(1)
        print(f'A moeda caiu: {resultado_moeda}')
        sleep(0.8)

        if resultado_moeda == jogada_ia1:
            print(f'A vencedora foi a IA-1! Sua escolha foi: {jogada_ia1}')
            sleep(0.8)
        else:
            print(f'A vencedora foi a IA-2! Sua escolha foi: {jogada_ia2}')
            sleep(0.8)

        print('\nQuer Jogar Novamente ou Trocar de Modo?')
        sleep(0.3)
        novamente = int(input('1 - Jogar Novamente\n2 - Trocar de Modo\n>>> '))

        if novamente == 1:
            continue
        elif novamente == 2:
            break
        else:
            print("Opção inválida, voltando ao menu...")
            break


def modo_ia_vs_player():
    """Modo 2: Jogador humano contra IA."""
    while True:
        escolhas = ['cara', 'coroa']
        resultado_moeda = choice(escolhas)
        print(playerxai)
        sleep(1.8)  # introdução modo jogador
        escolha_player = int(input('Qual você escolhe jogador?\n1 - Cara\n2 - Coroa\n>>> '))
        sleep(0.8)
        if escolha_player == 1:
            escolha_str = 'cara'
        elif escolha_player == 2:
            escolha_str = 'coroa'
        else:
            print('Escolha um número válido')
            continue
        escolha_ai = choice([e for e in escolhas if e != escolha_str])
        print('Você escolheu:', escolha_str)
        sleep(0.5)
        print('A IA escolheu:', escolha_ai)
        sleep(0.7)
        print('A moeda caiu:', resultado_moeda)
        sleep(0.8)
        if escolha_str == resultado_moeda:
            print('Parabéns! Você ganhou da IA')
            sleep(0.7)
        else:
            print('Que pena, a IA ganhou de você')
            sleep(0.7)
            print('Ela escolheu: ', escolha_ai)
        print('\nQuer Jogar Novamente ou Trocar de Modo?')
        sleep(0.3)
        novamente = int(input('1 - Jogar Novamente\n2 - Trocar de Modo\n>>> '))

        if novamente == 1:
            continue
        elif novamente == 2:
            break
        else:
            print("Opção inválida, voltando ao menu...")
            break


def modo_player_vs_player():
    """Modo 3: Dois jogadores humanos jogam entre si."""
    while True:
        escolhas = ['cara', 'coroa']
        resultado_moeda = choice(escolhas)
        print(playerxplayer)
        sleep(1.8)
        escolha_player = int(input('Qual você escolhe jogador?\n1 - Cara\n2 - Coroa\n>>> '))
        sleep(0.8)
        if escolha_player == 1:
            escolha_str = 'cara'
        elif escolha_player == 2:
            escolha_str = 'coroa'
        else:
            print('Escolha um número válido')
            continue
        escolhas.remove(escolha_str)
        print('Jogador 1 Escolheu:', escolha_str)
        sleep(0.5)
        jogador2_escolha = escolhas[0]
        print('Jogador 2, automaticamente, sua escolha se tornou:', jogador2_escolha)
        sleep(0.7)
        print('A moeda saiu:', resultado_moeda)
        sleep(0.8)

        if escolha_str == resultado_moeda:
            print('Parabéns Jogador 1! Você ganhou')
            sleep(0.5)
            print('Você escolheu:', resultado_moeda)
        else:
            print('Parabéns Jogador 2! Você ganhou')
            sleep(0.5)
            print('Você escolheu:', resultado_moeda)
        print('\nQuer Jogar Novamente ou Trocar de Modo?')
        sleep(0.3)
        novamente = int(input('1 - Jogar Novamente\n2 - Trocar de Modo\n>>> '))

        if novamente == 1:
            continue
        elif novamente == 2:
            break
        else:
            print("Opção inválida, voltando ao menu...")
            break


def modo_insanidade():
    """Modo 4: Modo caótico com resultados imprevisíveis."""
    while True:
        escolhas = ['cara', 'coroa', 'em pé', 'fora da mesa', 'lados iguais', 'explodiu']
        escolhas_validas = ['cara', 'coroa']
        resultado_moeda = choice(escolhas)
        print(insanidade)
        sleep(1.8)
        escolha_player = choice(escolhas_validas)
        print("Você nem escolheu... Mas escolheu:", escolha_player)
        sleep(1)
        escolha_ai = choice([e for e in escolhas_validas if e != escolha_player])
        print("A IA escolheu:", escolha_ai)
        sleep(0.5)

        if resultado_moeda in ['cara', 'coroa']:
            if resultado_moeda == escolha_player:
                print("🎉 Você venceu essa rodada maluca!")
                sleep(0.7)
            elif resultado_moeda == escolha_ai:
                print("🤖 A IA venceu... por sorte (ou caos).")
                sleep(0.7)
            else:
                print("🌀 Algo deu errado... Isso não deveria acontecer!")
                sleep(0.7)

        elif resultado_moeda == 'em pé':
            print("😱 A moeda ficou em pé! É um empate!")
            sleep(0.7)

        elif resultado_moeda == 'fora da mesa':
            print("🪙 A moeda caiu no chão e desapareceu... Ninguém ganha.")
            sleep(0.7)

        elif resultado_moeda == 'lados iguais':
            print("🪞 A moeda tinha dois lados iguais! A rodada está corrompida!")
            sleep(0.7)
            print("⚖️ Ambos ganham... ou será que ninguém ganhou?")
            sleep(0.7)

        elif resultado_moeda == 'explodiu':
            print("💥 A moeda EXPLODIU! Caos total!")
            sleep(0.7)
            print("Todos perdem... mas ganham experiência (talvez).")
            sleep(0.7)

        else:
            print("❓ Resultado desconhecido. A insanidade tomou conta...")
            sleep(0.7)

        novamente = int(input('1 - Jogar Novamente\n2 - Trocar de Modo\n>>> '))

        if novamente == 1:
            continue
        elif novamente == 2:
            break
        else:
            print("Opção inválida, voltando ao menu...")
            break


def modo_competicao():
    """Modo 5: Competição entre vários jogadores com pontuação e ranking."""
    while True:
        class Jogador:
            def __init__(self, nome):
                self.nome = nome
                self.pontos = 0

            def exibir_info(self):
                print(f'Nome: {self.nome} | Pontos: {self.pontos}')

            def ganhar_ponto(self):
                self.pontos += 1

        escolhas = ['cara', 'coroa']
        jogadores = []
        print(competicao)
        sleep(1.5)

        try:
            qtd_jogadores = int(input('Quantos Jogadores Teremos Nessa Competição? (mín. 2) >>> '))
            if qtd_jogadores < 2:
                print("É necessário pelo menos 2 jogadores.")
                return
        except ValueError:
            print("Por favor, digite um número válido.")
            return

        for qtd in range(qtd_jogadores):
            nome_player = input(f'Digite o nome do Jogador {qtd + 1}:').strip()
            jogadores.append(Jogador(nome_player))

        try:
            rodadas = int(input('Quantas Rodadas Quer Jogar? (mín. 1) >>> '))
            if rodadas < 1:
                print("Número de rodadas inválido.")
                return
        except ValueError:
            print('Insira um valor válido')
            return

        for rodada in range(1, rodadas + 1):
            print(f'\n----RODADA {rodada}----')
            sleep(0.5)
            resultado_moedas = choice(escolhas)
            for jogador in jogadores:
                try:
                    escolha_player = int(input(f'{jogador.nome}, qual você escolhe?\n1 - Cara\n2 - Coroa\n>>> '))

                    if escolha_player == 1:
                        escolha_str = 'cara'
                    elif escolha_player == 2:
                        escolha_str = 'coroa'
                    else:
                        print('Escolha Inválida! Nenhum ponto nessa rodada!')
                        continue

                    if escolha_str == resultado_moedas:
                        jogador.ganhar_ponto()
                        print(f'O jogador {jogador.nome} acertou e ganhou +1 ponto.')
                    else:
                        print(f'O jogador {jogador.nome} não ganhou nenhum ponto.')
                        sleep(0.5)
                except ValueError:
                    print('Escolha um número válido')
        print('Salvando Ranking...')
        sleep(1)
        salvar_ranking(jogadores)
        print('Ranking Salvo!')
        sleep(0.5)

        novamente = int(input('1 - Jogar Novamente\n2 - Trocar de Modo\n>>> '))

        if novamente == 1:
            continue
        elif novamente == 2:
            break
        else:
            print("Opção inválida, voltando ao menu...")
            break


# -------------------------
# Funções auxiliares do jogo
# -------------------------

def ranking():
    """Exibe o ranking salvo no arquivo CSV."""
    while True:
        try:
            with open('ranking.csv', 'r') as ranking_arquivo:
                leitor_csv = csv.reader(ranking_arquivo, delimiter=",")
                print(f"{'Nome':<15} | {'Pontos':<6}")
                print('-' * 25)
                for i, linha in enumerate(leitor_csv):
                    if i == 0:
                        continue
                    if len(linha) >= 2:
                        print(f"{linha[0]:<15} | {linha[1]:<6}")

        except FileNotFoundError:
            print(
                'O Ranking ainda é inexistente. Jogue ao menos uma partida no modo competição para dar início ao Ranking')

        novamente = int(input('1 - Jogar Novamente\n2 - Trocar de Modo\n>>> '))
        if novamente == 1:
            continue
        elif novamente == 2:
            return
        else:
            print("Opção inválida, voltando ao menu...")
            return


def salvar_ranking(jogadores):
    """Salva ou atualiza o ranking dos jogadores no arquivo CSV."""
    ranking_path = 'ranking.csv'
    ranking_atual = {}

    # 1. Lê o ranking atual se o arquivo existir
    if os.path.exists(ranking_path):
        with open(ranking_path, 'r') as arquivo:
            leitor_csv = csv.reader(arquivo)
            next(leitor_csv, None)  # Pular cabeçalho
            for linha in leitor_csv:
                if len(linha) >= 2:
                    nome, pontos = linha[0], int(linha[1])
                    ranking_atual[nome] = pontos

    # 2. Atualiza ou adiciona jogadores
    for jogador in jogadores:
        if jogador.nome in ranking_atual:
            ranking_atual[jogador.nome] += jogador.pontos
        else:
            ranking_atual[jogador.nome] = jogador.pontos

    # 3. Escreve de volta no CSV
    with open(ranking_path, 'w', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow(['Nome', 'Pontos'])
        for nome, pontos in sorted(ranking_atual.items(), key=lambda x: x[1], reverse=True):
            escritor_csv.writerow([nome, pontos])


def sair():
    """Mensagem de encerramento do jogo."""
    print('FINALIZANDO...')
    sleep(2)
    print(finalmssg)
    sleep(1)


def error():
    """Tratamento simples de erro para entradas inválidas."""
    if modo_De_Jogo == '':
        print(erro_none)
    elif modo_De_Jogo == ValueError:
        print(erro)


# ------------------------
# Loop principal do programa
# ------------------------

while True:
    print(introducao)
    modo_De_Jogo = input('Qual Modo de Jogo Está Interessado em Jogar Hoje?').strip()

    if modo_De_Jogo == "":
        print(erro_none)
        continue
    else:
        try:
            modo_De_Jogo = int(modo_De_Jogo)
        except ValueError:
            print(erro)
            continue  # volta ao menu

    match modo_De_Jogo:
        case 1:
            modo_ia_vs_ia()
        case 2:
            modo_ia_vs_player()
        case 3:
            modo_player_vs_player()
        case 4:
            modo_insanidade()
        case 5:
            modo_competicao()
        case 6:
            ranking()
        case 7:
            sair()
            break
        case _:
            print(erro)
