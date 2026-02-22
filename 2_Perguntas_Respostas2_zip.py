# EXERCICIO DE PERGUNTAS E RESPOSTAS

perguntas = [       # perguntas (lista)
    # dentro dicionário
    {                                           #indice0
        "Pergunta": "Quanto é 2 + 2 ?:",   
        "Opções": ["1", "2", "3", "4"],
        "Resposta": "d",
    },
    {                                           #indice1
        "Pergunta": "Quanto é 5 * 5 ?:",
        "Opções": ["25", "30", "45", "55"],
        "Resposta": "a",
    },
    {                                           #indice2
        "Pergunta": "Quanto é 10 / 2 ?:",
        "Opções": ["4", "2", "1", "5"],
        "Resposta": "d",
    },
]

while True:
    # PRIMEIRA PERGUNTA
    print(f'Pergunta: {perguntas[0]["Pergunta"]}')

    letras = ["a", "b", "c", "d"]
    for letras, opcao in zip(letras, perguntas[0]["Opções"]):
        print(f"{letras}-) {opcao}")

    resposta = input("Digite sua resposta: ").lower()

    if resposta == perguntas[0]["Resposta"]:
        print("PARABÉNS!!! VOCÊ ACERTOU")
    else:
        print("VOCÊ ERROU, MAS NÃO DESISTA!! TENTE NOVAMENTE")
        break

    # SEGUNDA PERGUNTA
    print(f'\nPergunta: {perguntas[1]["Pergunta"]}')

    letras = ["a", "b", "c", "d"]
    for letras, opcao in zip(letras, perguntas[1]["Opções"]):
        print(f"{letras}-) {opcao}")
  
    resposta = input("Digite sua resposta: ").lower()

    if resposta == perguntas[1]["Resposta"]:
        print("PARABÉNS!!! VOCÊ ACERTOU")
    else:
        print("VOCÊ ERROU, MAS NÃO DESISTA!! TENTE NOVAMENTE")
        break

    # TERCEIRA PERGUNTA
    print(f'\nPergunta: {perguntas[2]["Pergunta"]}')

    letras = ["a", "b", "c", "d"]
    for letras, opcao in zip(letras, perguntas[2]["Opções"]):
        print(f"{letras}-) {opcao}")

    resposta = input("Digite sua resposta: ").lower()

    if resposta == perguntas[2]["Resposta"]:
        print("PARABÉNS!!! VOCÊ ACERTOU")
    else:
        print("VOCÊ ERROU, MAS NÃO DESISTA!! TENTE NOVAMENTE")
        break
    break