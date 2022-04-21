from maxHeap import *
import os, numpy


clear = lambda: os.system('cls')

class Pessoa:
    def __init__(self, nome_completo, tipo_sanguineo, data_nascimento):
        self.nome_completo = nome_completo
        self.tipo_sanguineo = tipo_sanguineo
        self.data_nascimento = data_nascimento


h = MaxHeap()
tamH = numpy.size(h)
aux = []
listaChamar = []
priArray = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
contador = 999
while True:
    print("1 - Novo Paciente")
    print("2 - Chamar novo paciente")
    print("3 - Ver o proximo paciente a ser chamado")
    print("4 - Listar os ultimos 5 pacientes chamados")
    print("5 - Limpar tela")         
    print("6 - Sair")                         
    menu = (input())
    if menu == '1':
        print('\n\n')
                   
        nomeCompleto = str(input("Qual o nome do paciente? "))
        tipoSanguineo = str(input("Tipo sanguineo? "))
        dataNascimento = str(input("Data de nascimento? "))
        
        while True:
            prioridade = str(input("Qual a ordem de prioridade do paciente? (1 a 10) "))
            if prioridade in priArray:
                prioridade = int(prioridade)
                newPerson = Pessoa(nomeCompleto, tipoSanguineo, dataNascimento)
                newPacient = (prioridade, contador, (newPerson.nome_completo, newPerson.tipo_sanguineo, newPerson.data_nascimento))
                listaChamar.insert(0, 'Possui')
                h.put(newPacient)
                contador -= 1

                break
            else:
                print('Você precisa digitar um número.')

        
    elif menu == '2':
        if listaChamar != []:
            print('\n\n')  
            aux.append(h.peek())
            del(listaChamar[0])
            print(h.get())
        else:
            print('\n\nNão temos pacientes a serem chamados')

    elif menu == '3':
        if listaChamar != []:
            print('\n\n')
            print(h.peek())
        else:
            print('\n\nNão temos pacientes a serem chamados')

        
    elif menu == '4':
        print('\n\n')
        while len(aux) > 5:
            aux.pop(0)
        for i in range(len(aux)):
            print(aux[i])
        
    elif menu == '5':
        clear()
    elif menu == '6':
        break
    else:
        print('\nDesculpe, não entendi')

            
                
                
