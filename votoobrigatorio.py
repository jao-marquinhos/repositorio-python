nome = str(input("Qual o seu nome?"))
idade = int(input("Quantos anos você tem?"))

print("Olá,", nome,"\n", idade, "anos")

if idade >= 18 and  idade < 65:
    print("Seu voto é obrigatório")
elif idade >= 16 or idade >= 65:
    print("Seu voto não é obrigatório")
else:
    print("Você não pode votar")