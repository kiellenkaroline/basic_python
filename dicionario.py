#Dicionário 

filmes = {
   1: ['Outono em NY','Romance', 789, 120],
   2: ['Exorcista', 'Terror', 456, 130],
   3: ['Ilha do medo','Suspense', 123, 120]
}

#print(filmes[1])

#for filme in filmes.values():
 #   print(filme)

for indice in filmes:
    print(f'Filme: {filmes[indice][0]}')
    print(f'Gênero: {filmes[indice][1]}')
    print(f'duração: {filmes[indice][3]}')
    print(f'--------')
