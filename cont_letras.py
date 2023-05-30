from unidecode import unidecode
import string
def carregar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        return arquivo.read()
    
def obtendo_letras(texto):
    texto = unidecode(texto)
    texto = texto.upper().split()
    palavras = []
    for i in texto:
        i = i.translate(str.maketrans('', '', string.punctuation))
        palavras.append(i)
    letras = []
    for i in palavras:
        for l in i:
            letras.append(l)
    return letras

def contar_letras(letra):
    contador = {}
    for l in letra:
        if l in contador:
            contador[l] += 1
        else:
            contador[l] = 1
    return sorted(contador.items(), key=lambda x: x[1], reverse=True)

def consultas(letras_ordenadas):
    while True:
        print("Digite uma letra para consultar se tem no texto e quantas vezes aparece")
        print("Ou digite SAIR para terminar")
        letra_escolhida = input(str()).upper().strip()
        if letra_escolhida == 'SAIR':
            break
        letra_encontrada = False
        for letra, ocorrencias in letras_ordenadas:
            if letra_escolhida == letra:
                print(f"A letra {letra} aparece {ocorrencias} vezes")
                print(' ')
                letra_encontrada = True
                break
        if not letra_encontrada:
            print('Letra não encontrada no texto, tente novamente')
            print(' ')

def exibir_letras_frequentes(letras_ordenadas):
    letras = [p[0] for p in letras_ordenadas]
    print(f"A letra mais frequente é: {letras[0]}, com {letras_ordenadas[0][1]} ocorrência(s)")
    print(f"A letra menos frequente é: {letras[-1]}, com {letras_ordenadas[-1][1]} ocorrência(s)")

def opcoes():
    print('Texto: ')
    texto = carregar_arquivo('teste.txt')
    print(texto)
    print(' ')
    print('O que quer fazer com o texto. Escolha uma das opções abaixo:')
    print('1 - Retirar os acentos')
    print('2 - Contar as letras')
    print('3 - Escolher qual(is) letra(s) deseja ver e quantas vezes aparece')
    print('4 - Exibir as letras com mais aparição e com menos aparição')
    print('0 - Sair')


texto = carregar_arquivo('teste.txt')
opcoes()

while True:
    letras = obtendo_letras(texto)
    ordenando = contar_letras(letras)
    
    opcao = input(str('Opção escolhida: '))
    if opcao == '1':
        print(letras)
    elif opcao == '2':
        print(ordenando)
    elif opcao == '3':
        consultas(ordenando)
    elif opcao == '4':
        exibir_letras_frequentes(ordenando)
    elif opcao == '0':
        print('Obrigada! Até a próxima!')
        break