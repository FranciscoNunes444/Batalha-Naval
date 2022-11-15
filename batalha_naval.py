'''#func pc atacar // sorteia um indice , se o indice for igual a o do barco na matriz, ele atira, se acertar, i+1.
func pc definir barco // sorteia um indice , para colocar os barcos na matriz.
func usuario atacar
func usuario definir barco
func verificar pedaços do barco
func proximo tiro do pc
func descolar barco'''
import random


BP = '🛳️'
BM = '🛳️'
BG = '🛳️'
print("💣 💣 💣 💣 💣 💣 💣 💣 💣 💣 BATALHA NAVAL 🚢 🚢 🚢 🚢 🚢 🚢 🚢 🚢 🚢\n ")
print(''' Você tem três navios diferentes\n BARCO PEQUENO: ocupa 2 lugares no tabuleiro e vale 2 pontos\n BARCO MÉDIO: ocupa 3 lugares no tabuleiro e vale 4 pontos\n BARCO GRANDE: ocupa 4 lugares no tabuleiro e vale 6 pontos''')
print(" ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ O SEU OPONENTE SERÁ O MR.MZR 🤖 ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️\n")

matriz_bn = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]] 

matriz_pc = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]] 
        

for i in range(len(matriz_bn)):
    print(matriz_bn[i], sep='\n')
print('')


def definirBarco():

    linhaBp = int(
        input('''Digite o numero da linha que deseja posicionar o barco pequeno: '''))
    colunaBp = int(
        input('''Digite o numero da coluna que deseja posicionar o barco pequeno: '''))  

    linhaBm = int(
        input('''Digite o numero da linha que deseja posicionar o barco médio: '''))
    colunaBm = int(
        input('''Digite o numero da coluna que deseja posicionar o barco médio: '''))  

    if colunaBm == colunaBp:   
        while True:
            colunaBm = int(
                input('''Digite o numero da coluna que deseja posicionar o barco médio: '''))  
            if colunaBm != colunaBp: 
                break
    if colunaBm == colunaBp + 1: 
        colunaBm = int(
            input('''Digite o numero da coluna que deseja posicionar o barco médio: '''))  
        while True:
            colunaBm = int(
                input('''Digite o numero da coluna que deseja posicionar o barco médio: '''))  
            if colunaBm != colunaBp + 1: 
                break

    linhaBg = int(
        input('''Digite o numero da linha que deseja posicionar o barco grande: '''))
    colunaBg = int(
        input('''Digite o numero da coluna que deseja posicionar o barco grande: ''')) 
 
    if colunaBg == colunaBp: 
        colunaBg = int(
            input('''Digite o numero da coluna que deseja posicionar o barco grande: '''))  
        while True:
            colunaBg = int(
                input('''Digite o numero da coluna que deseja posicionar o barco grande: '''))  
            if colunaBm != colunaBp: 
                break
    if colunaBg == colunaBp + 1: 
        colunaBg = int(
            input('''Digite o numero da coluna que deseja posicionar o barco grande: '''))    
        while True:
            colunaBg = int(
                input('''Digite o numero da coluna que deseja posicionar o barco grande: '''))  
            if colunaBg != colunaBp + 1: 
                break 

    if colunaBg == colunaBm: 
        colunaBg = int(
            input('''Digite o numero da coluna que deseja posicionar o barco grande: '''))  
        while True:
            colunaBg = int(
                input('''Digite o numero da coluna que deseja posicionar o barco grande: '''))  
            if colunaBm != colunaBm: 
                break
    if colunaBg == colunaBm + 1: 
        colunaBg = int(
            input('''Digite o numero da coluna que deseja posicionar o barco grande: '''))   
        while True:
            colunaBg = int(
                input('''Digite o numero da coluna que deseja posicionar o barco grande: '''))  
            if colunaBg != colunaBm + 1: 
                break 
    if linhaBp == 5: 
        linhaBp -= 1  
    if linhaBm == 5: 
        linhaBm -= 2 
    if linhaBg == 5 or linhaBg == 4: 
        linhaBg -= 3

    matriz_bn[colunaBp][linhaBp] = BP
    matriz_bn[colunaBp][linhaBp+1] = BP 
    matriz_bn[colunaBm][linhaBm] = BM
    matriz_bn[colunaBm][linhaBm+1] = BM   
    matriz_bn[colunaBm][linhaBm+2] = BM
    matriz_bn[colunaBg][linhaBg] = BG
    matriz_bn[colunaBg][linhaBg+1] = BG 
    matriz_bn[colunaBg][linhaBg+2] = BG 
    matriz_bn[colunaBg][linhaBg+3] = BG
    for i in range(len(matriz_bn)):
        print(matriz_bn[i], sep='\n')

def definirBarcoPC(): 
    linhaBp = random.randint(0, 5) 
    colunaBp = random.randint(0,5) 
    linhasBm = random.randint(0, 5) 
    colunaBm = random.randint(0,5) 
    linhaBg = random.randint(0, 5) 
    colunaBg = random.randint(0,5)    
    if colunaBp == colunaBm: 
        valor_ant = colunaBp  
        while True:
            colunaBp = random.randint(0,5) 
            if colunaBp != colunaBm and colunaBp != valor_ant: 
                break
    if colunaBp == colunaBm + 1:     
        valor_ant = colunaBp
        while True:
            colunaBp = random.randint(0,5)
            if colunaBp != colunaBm and colunaBp != colunaBm + 1 and colunaBp != valor_ant: 
                break 
    if colunaBp == colunaBg: 
        valor_ant = colunaBp  
        while True:
            colunaBp = random.randint(0,5) 
            if colunaBp != colunaBg and colunaBp != valor_ant: 
                break
    if colunaBp == colunaBg + 1:     
        valor_ant = colunaBp
        while True:
            colunaBp = random.randint(0,5)
            if colunaBp != colunaBg and colunaBp != colunaBg + 1 and colunaBp != valor_ant: 
                break 
    
    if colunaBm == colunaBp: 
        valor_ant = colunaBm   
        while True:
            colunaBm = random.randint(0,5) 
            if colunaBm != colunaBp and colunaBm != valor_ant: 
                break
    if colunaBm == colunaBp + 1:  
        valor_ant = colunaBm
        while True:
            colunaBm = random.randint(0,5)
            if colunaBm != colunaBp and colunaBm != colunaBp + 1 and colunaBm != valor_ant: 
                break 
    
    if colunaBm == colunaBg: 
        valor_ant = colunaBm   
        while True:
            colunaBm = random.randint(0,5) 
            if colunaBm != colunaBg and colunaBm != valor_ant: 
                break
    if colunaBm == colunaBg + 1:  
        valor_ant = colunaBm
        while True:
            colunaBm = random.randint(0,5)
            if colunaBm != colunaBg and colunaBm != colunaBg + 1 and colunaBm != valor_ant: 
                break

    if colunaBg == colunaBp:  
        valor_ant = colunaBg
        while True:
            colunaBg = random.randint(0,5) 
            if colunaBg != colunaBp and colunaBg != valor_ant: 
                break
    if colunaBg == colunaBp + 1:     
        valor_ant = colunaBg
        while True:
            colunaBg = random.randint(0,5)  
            if colunaBg != colunaBp and colunaBg != colunaBp + 1 and colunaBg != valor_ant: 
                break 

    if colunaBg == colunaBm: 
        valor_ant = colunaBg  
        while True:
            colunaBg = random.randint(0,5) 
            if colunaBg != colunaBm and colunaBg != valor_ant: 
                break
    if colunaBg == colunaBm + 1:     
        valor_ant = colunaBg
        while True:
            colunaBg = random.randint(0,5)
            if colunaBg != colunaBm and colunaBg != colunaBm + 1 and colunaBg != valor_ant: 
                break 
    
    if linhaBp == 5: 
        linhaBp -= 1  
    if linhasBm == 5 or linhasBm == 4: 
        linhasBm -= 2 
    if linhaBg == 5 or linhaBg == 4 or linhaBg == 3: 
        linhaBg -= 3
    matriz_pc[colunaBp][linhaBp] = BP
    matriz_pc[colunaBp][linhaBp+1] = BP 
    matriz_pc[colunaBm][linhasBm] = BM
    matriz_pc[colunaBm][linhasBm+1] = BM   
    matriz_pc[colunaBm][linhasBm+2] = BM
    matriz_pc[colunaBg][linhaBg] = BG
    matriz_pc[colunaBg][linhaBg+1] = BG 
    matriz_pc[colunaBg][linhaBg+2] = BG 
    matriz_pc[colunaBg][linhaBg+3] = BG
    for i in range(len(matriz_pc)):
        print(matriz_pc[i], sep='\n')

while True:
    definirBarco()  
    definirBarcoPC()