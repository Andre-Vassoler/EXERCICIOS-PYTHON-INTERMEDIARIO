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

# Loop principal: percorre todas as perguntas
for pergunta in perguntas:

    # Mostra o texto da pergunta
    print(f"\nPergunta: {pergunta['Pergunta']}")

    # enumerate percorre a lista de opções
    # i  -> índice (0, 1, 2, 3)
    # opcao -> valor da lista ("1", "2", "3", "4", etc.)
    for i, opcao in enumerate(pergunta["Opções"]):

        # Converte o índice em letra:
        # 97 é o código ASCII da letra 'a'
        # 97 + 0 = a
        # 97 + 1 = b
        # 97 + 2 = c
        # 97 + 3 = d
        letra = chr(97 + i)

        # Exibe a opção no formato: a-) opção
        print(f"{letra}-) {opcao}")

    # Lê a resposta do usuário e converte para minúscula
    resposta = input("Digite sua resposta: ").lower()

    # Verifica se a resposta está correta
    if resposta == pergunta["Resposta"]:
        print("PARABÉNS!!! VOCÊ ACERTOU")
    else:
        print("VOCÊ ERROU, MAS NÃO DESISTA!! TENTE NOVAMENTE")
        break  # Encerra o jogo se errar