# EXERCICIO DE PERGUNTAS E RESPOSTAS

perguntas = [
    {
        "Pergunta": "Quanto é 2 + 2 ?:",
        "Opções": ["1", "2", "3", "4"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5 * 5 ?:",
        "Opções": ["25", "30", "45", "55"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10 / 2 ?:",
        "Opções": ["4", "2", "1", "5"],
        "Resposta": "5",
    },
]

def fazer_pergunta(pergunta_dict):
    print(f"\nPergunta: {pergunta_dict['Pergunta']}")

    for opcao in pergunta_dict["Opções"]:
        print(opcao)

    resposta = input("Digite sua resposta: ")

    if resposta == pergunta_dict["Resposta"]:
        print("PARABÉNS!!! VOCÊ ACERTOU")
        return True
    else:
        print("VOCÊ ERROU, MAS NÃO DESISTA!! TENTE NOVAMENTE")
        return False


# loop principal
for pergunta in perguntas:
    acertou = fazer_pergunta(pergunta)
    if not acertou:
        break
    