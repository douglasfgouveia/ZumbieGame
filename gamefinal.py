""" PUC PR - CURITIBA
DISCIPLINA - ANALISE E DESENVOLVIMENTO DE SISTEAS
ALUNO - DOUGLAS FERNANDO GOUVEIA
DESENVOLVIMENTO DO PROTOTIPO PROPOSTO PARA A ATP.
ESSE PROTOTIPO CONTEM A POSSIBILIDADE DE UM TURNO POR JOGADOR.
"""
import random
import time
from collections import namedtuple

# ----- Iniciando variaveis para armazenar os jogadores
num_jogadores = 0
jogadores = []

# ------ Variaveis onde faço o controle de turno e jogo finalizado, quando ficam True o turno acaba
jogo_finalizado = False
turno_finalizado = False
turno = 1

# ----- Listas que armazenam os dados do copo, e os já retirados na mesa
copo_dados = []
copo_retirados = []

dados_cerebro = []
dados_tiros = []
dados_pegadas = []



# Função que verifica se o jogador morreu por tiros no turno
def mortoPorTiros(tiros):
    if tiros >= 3:
        print('Infelizmente você tomou 3 tiros :X Você perdeu os pontos que conseguiu nessa rodada. Iremos ao próximo jogador.')

        return True
    return False


# Função que verifica o ganhador
def verificaGanhador(pontos):
    if pontos >= 13:
        print(f'Parabenssss {jogador["nome"]}, você foi o grande ganhador, uhuuu! Jogo finalizado. Iremos exibir as pontuações a seguir, ok?')
        jogador["pontos"] = jogador["pontos"] + cerebros

        return True
    return False

# pontuacao jogo
def listaPontuacaoJogadores(jogadores):
    print(f'Jogo encerrado ;D Veja como ficaram as pontuações finais:')
    print(f'{"Jogador":20}|{"Pontuação":^2}')
    for jogador in jogadores:
        print(f'{jogador["nome"]:20}|{jogador["pontos"]:^2}')

#---acionamento de dados
Dado = namedtuple('Dado', ['face', 'cor'])


print('Fazendo configuração inicial do jogo...')
for i in range(6):
    copo_dados.append(Dado(face='CPCTPC', cor='verde'))

for i in range(4):
    copo_dados.append(Dado(face='TPCTPC', cor='amarelo'))

for i in range(3):
    copo_dados.append(Dado(face='TPTCPT', cor='vermelho'))

print('Vamos lá!', end='\n')



while num_jogadores < 2:
    num_jogadores = int(input('Informe quantos jogadores irão jogar: '))
    if num_jogadores < 2:
        print('O jogo precisa de pelo menos dois jogadores.')


for i in range(num_jogadores):
    nome = input(f'Jogador { str(i+1) }, informe seu nome: ')
    jogadores.append({"posicao": i+1, "nome": nome, "pontos": 0})

print('\n')
print('| Confirmando jogadores e posições |', end='\n')


print(f'{"Jogador":20}|{"Posição":^2}')
for jogador in jogadores:
    print(f'{jogador["nome"]:20}|{jogador["posicao"]:^2}')

print('\n')



while not jogo_finalizado:
    print('\n')
    print(f'Iniciando turno { turno } | Se preparem')


    for jogador in jogadores:
        if jogo_finalizado:
            break
        print(f'Turno { turno } | Vez do jogador: { jogador["nome"] }')
        print('===================================================')

        turno_finalizado = False
        # Inicio as variaveis do 0, para ver as faces que o jogador está tirando e incrementar
        cerebros = 0
        passos = 0
        tiros = 0
        while not turno_finalizado:
            print('Mexendo os dados...')
            # Utilizo o shuffle para embaralhar a lista de dados, apenas para aumentar a randomização
            random.shuffle(copo_dados)


            # Dados pote insulficiente
            if len(copo_dados) < 3:
                for dado_retirado in copo_retirados:
                    copo_dados.append(dado_retirado)
                    copo_retirados.remove(dado_retirado)


            for i in range(0, 3):

                rand = random.randrange(0, len(copo_dados))
                dado = copo_dados[rand]
                print(f'Você tirou dado de cor: { dado.cor } | FACES: ({ dado.face })')

                #face dado
                face = random.choice(dado.face)
                print(f'Face: { face }')

                if face == 'C':
                    cerebros = cerebros + 1
                    copo_retirados.append(dado)
                elif face == 'P':
                    passos = passos + 1
                    copo_retirados.append(dado)
                elif face == 'T':
                    tiros = tiros + 1
                    copo_retirados.append(dado)


                copo_dados.remove(dado)


            print('\n')
            print(f'Sua pontuação no turno atual: {cerebros} CEREBROS | {passos} PASSOS | {tiros} TIROS')
            print('\n')


            if mortoPorTiros(tiros):
                turno_finalizado = True
                break


            if verificaGanhador(jogador["pontos"] + cerebros):
                jogo_finalizado = True
                break


            opcao = input('Deseja continuar? s/n => ')
            if opcao == 'n':
                turno_finalizado = True
                jogador["pontos"] = jogador["pontos"] + cerebros

    print('\n')
    if jogo_finalizado != True:

        print(f'Finalizamos o turno {turno} por aqui! Irei apresentar como estão as pontuações até então:')

        print(f'{"Jogador":20}|{"Pontuação":^2}')
        for jogador in jogadores:
            print(f'{jogador["nome"]:20}|{jogador["pontos"]:^2}')


    turno = turno + 1


print('\n')
listaPontuacaoJogadores(jogadores)

