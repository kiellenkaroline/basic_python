#Lista dos clubes

lista_de_clubes = ['ibis',
 'Flamengo', 
 'perilina', 
 'volta redonda', 
 'nacional de patos'
 ]
print(lista_de_clubes)

#Perguntar qual o clube o usuário vai verificar
clube_pesquisado = input('Digite o clube:')

for clube in lista_de_clubes:

    if clube == clube_pesquisado:
        print('Achei')
    else:
        print('Ainda não achei!')