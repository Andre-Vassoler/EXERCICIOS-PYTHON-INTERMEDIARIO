import os  # importa o módulo os para executar comandos do sistema (ex: limpar tela)


def listar(tarefas):
    print()  # apenas uma linha em branco para estética
    if not tarefas:  # verifica se a lista está vazia (Falsy)
        print('Nenhuma tarefa para listar')
        return  # sai da função sem continuar

    print('Tarefas:')
    for tarefa in tarefas:  # percorre cada tarefa na lista
        print(f'\t{tarefa}')  # imprime com tabulação
    print()  # linha em branco final


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:  # se não houver tarefas, não há o que desfazer
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()  # remove a última tarefa da lista principal
    print(f'{tarefa=} removida da lista de tarefas.')  
    # tarefa= mostra "tarefa='nome_da_tarefa'" (f-string moderna)

    tarefas_refazer.append(tarefa)  
    # guarda a tarefa removida na lista de refazer (pilha de refazer)

    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:  # se não houver nada para refazer
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()  
    # pega a última tarefa que foi desfeita

    print(f'{tarefa=} adicionada na lista de tarefas.')

    tarefas.append(tarefa)  
    # devolve a tarefa para a lista principal (refaz a ação)

    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()  
    # remove espaços do começo e do fim (ex: "   estudar  " -> "estudar")

    if not tarefa:  # se o usuário só apertou enter ou digitou espaços
        print('Você não digitou uma tarefa.')
        return

    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)  # adiciona nova tarefa na lista principal
    print()


# listas principais
tarefas = []           # lista atual de tarefas
tarefas_refazer = []   # lista que guarda tarefas desfeitas (para refazer)


while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)  # chama a função que mostra as tarefas
        continue  # volta para o início do loop

    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)  # remove da lista principal e guarda para refazer
        listar(tarefas)  # mostra a lista atualizada
        continue

    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)  # pega da pilha de refazer e devolve para tarefas
        listar(tarefas)  # mostra a lista atualizada
        continue

    elif tarefa == 'clear':
        os.system('clear')  
        # limpa o terminal (no Windows geralmente seria 'cls')
        continue

    else:
        adicionar(tarefa, tarefas)  # qualquer outro texto vira uma nova tarefa
        listar(tarefas)  # mostra a lista depois de adicionar
        continue
