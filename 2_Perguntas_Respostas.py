# EXERCICIO DE PERGUNTAS E RESPOSTAS

perguntas = [       # perguntas (lista)
    # dentro dicionário
    {                                           #indice0
        "Pergunta": "Quanto é 2 + 2 ?:",   
        "Opções": ["1", "2", "3", "4"],
        "Resposta": "4",
    },
    {                                           #indice1
        "Pergunta": "Quanto é 5 * 5 ?:",
        "Opções": ["25", "30", "45", "55"],
        "Resposta": "25",
    },
    {                                           #indice2
        "Pergunta": "Quanto é 10 / 2 ?:",
        "Opções": ["4", "2", "1", "5"],
        "Resposta": "5",
    },
]

while True:
    # PRIMEIRA PERGUNTA
    print(f'Pergunta: {perguntas[0]["Pergunta"]}')

    for opção in perguntas[0]["Opções"]:
        print(opção)

    resposta = input("Digite sua resposta: ")

    if resposta == perguntas[0]["Resposta"]:
        print("PARABÉNS!!! VOCÊ ACERTOU")
    else:
        print("VOCÊ ERROU, MAS NÃO DESISTA!! TENTE NOVAMENTE")
        break

    # SEGUNDA PERGUNTA
    print(f'\nPergunta: {perguntas[1]["Pergunta"]}')

    for opção in perguntas[1]["Opções"]:
        print(opção)
  
    resposta = input("Digite sua resposta: ")

    if resposta == perguntas[1]["Resposta"]:
        print("PARABÉNS!!! VOCÊ ACERTOU")
    else:
        print("VOCÊ ERROU, MAS NÃO DESISTA!! TENTE NOVAMENTE")
        break

    # TERCEIRA PERGUNTA
    print(f'\nPergunta: {perguntas[2]["Pergunta"]}')

    for opção in perguntas[2]["Opções"]:
        print(opção)

    resposta = input("Digite sua resposta: ")

    if resposta == perguntas[2]["Resposta"]:
        print("PARABÉNS!!! VOCÊ ACERTOU")
    else:
        print("VOCÊ ERROU, MAS NÃO DESISTA!! TENTE NOVAMENTE")
        break
    break