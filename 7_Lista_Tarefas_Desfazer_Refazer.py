# EXERCICIO - lista de tarefas com desfazer e refazer
lista = []
refazer_lista = []

while True:
    print("Comandos: desfazer, refazer, sair")
    comando = input("Digite uma tarefa ou comando: ").lower()

    print("\nTAREFAS:")
    

    if comando == "desfazer":
        if lista:           # se a lista tiver valor
            tarefa = lista.pop()                #remove a ultima tarefa adicionada
            refazer_lista.append(tarefa)        #guarda essa taarefa na lista de refazer
        else:
            print("Nada para desfazer")

    elif comando == "refazer":
        if refazer_lista:
            tarefa = refazer_lista.pop()    #pega a ultima tarefa que foi desfeita
            lista.append(tarefa)        #adiciona ela na lista
        else:
            "Nada para refazer" 
    
    elif comando == "sair":
        break
    
    else:
        lista.append(comando)
        refazer_lista.clear()   #nova tarefa apaga histórico de refazer
        

    for item in lista:
        print(f"- {item}")
    print("")
        

