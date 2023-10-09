#lista de contatos

contatos = [['Mãe', '83 9 88888888', '27/20/1982'],
['policia', '190'],
['samu','192']]

print(contatos[0][0])

for contato in contatos:
    print(f'Nome:{contato[0]} | Telefone: {contato[1]}' )