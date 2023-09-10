#Calcule a média de cada bimestre

nota01 = float(input("Digite a primeira nota"))
nota02 = float(input("Digite a segunda nota: "))
nota03 = float(input("Digite a terceira nota: "))
nota04 = float(input("Digite a quarta nota: "))
media = (nota01 + nota02 + nota03 + nota04)/4
print("A primeira nota é: ",5)
print("A segunda nota é : ",10)
print("A terceira nota é: ",7)
print("A quarta nota é: ",8)
print("A média final é: ", media)
if media >= 7:
    print("Aprovado")
else:
    print("Não Aprovado")
