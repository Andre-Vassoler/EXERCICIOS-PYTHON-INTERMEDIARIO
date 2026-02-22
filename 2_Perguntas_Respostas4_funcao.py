# EXERCICIO DE PERGUNTAS E RESPOSTAS

perguntas = [
    {
        "Pergunta": "Quanto é 2 + 2 ?:",
        "Opções": ["1", "2", "3", "4"],
        "Resposta": "d",
    },
    {
        "Pergunta": "Quanto é 5 * 5 ?:",
        "Opções": ["25", "30", "45", "55"],
        "Resposta": "a",
    },
    {
        "Pergunta": "Quanto é 10 / 2 ?:",
        "Opções": ["4", "2", "1", "5"],
        "Resposta": "d",
    },
]

def fazer_pergunta(pergunta_dict):
    print(f"\nPergunta: {pergunta_dict['Pergunta']}")

    letras = ["a", "b", "c", "d"]

    for letra, opcao in zip(letras, pergunta_dict["Opções"]):
        print(f"{letra}-) {opcao}")

    resposta = input("Digite sua resposta: ").lower()

    if resposta == pergunta_dict["Resposta"]:
        print("PARABÉNS!!! VOCÊ ACERTOU")
        return True
    else:
        print("VOCÊ ERROU, MAS NÃO DESISTA!! TENTE NOVAMENTE")
        return False


for pergunta in perguntas:
    if not fazer_pergunta(pergunta):
        break