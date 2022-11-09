def novoNome(menu):
    
    novonome = input('Informe o novo nome. ')
    telefone = input('Informe o telefone dessa pessoa. ')
    lista.append(telefone)

    outrotel = input('Deseja acrescentar outro número ao nome? sim/nao ')
    while outrotel == 'sim':
        tel2 = input('Informe o número. ')
        lista.append(tel2)
        repetir = input('Deseja acrescentar mais um? ')
        if repetir == 'sim':
            outrotel = 'sim'
        else:
            break
    agenda[novonome] = lista
    print('')
    print(agenda)
    print('A agenda goi atualizada.')
  

def incluirTelefone(menu):
    contato = input('Informe o nome ao qual deseja acrescentar o telefone. ')
    if contato in agenda:
        lista2 = [agenda[contato]]
        telefone = input('Informe o telefone. ')
        lista.append(telefone)
        agenda[contato] = lista2 #substitui o telefone anterior errada
    
    else: #else funciona
        incluir = input('O contato não está na agenda. Deseja incluí-lo? ')
        if incluir == 'sim':
            telefone = input('Informe o telefone. ')
            agenda[contato] = telefone 
        
        else:
            telefone = input('Você precisa adicionar o contato à agenda para incluir o telefone. ')
    
    print(agenda)

def excluirTelefone(menu):
    print(agenda)
    contato  = input('De quem é o telefone que deseja excluir da agenda acima? ')
    telefone = input('Qual o telefone que deseja exluir? ')
    agenda[contato].remove(telefone) 

    if agenda[contato] == []:
        agenda.pop(contato)

    
def excluirNome(menu):
    contato = input('Qual contato deseja excluir da agenda? ')
    agenda.pop(contato)
    print(agenda)
    print()


def consultaTelefone(menu):
    contato = input('A quem deseja consultar na agenda? ')
    print('O contato foi excluído com sucesso.')
    print(agenda[contato])



agenda = {'eliane' : 10203040}
lista = []

while True:
    menu = (int(input("""Qual ação deseja realizar?
    1.Incluir novo nome
    2.Incluir Telefone
    3.Excluir telefone
    4.Excluir nome
    5.Consultar telefone
    0.Sair.  """)))

    if menu == 0:
        break
    
    elif menu == 1:
        novoNome(menu)
    
    elif menu == 2: #incompleto
        incluirTelefone(menu)
    
    elif menu == 3:
        excluirTelefone(menu)

    elif menu == 4:
        excluirNome(menu)
    
    elif menu == 5:
        consultaTelefone(menu)