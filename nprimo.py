#Descubra se um numero é primo ou não

numero = int(input("Digite um numero inteiro: "))
primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        print(f"{numero} não é primo!")
        break
if primo:
    print(f"{numero} é primo!")