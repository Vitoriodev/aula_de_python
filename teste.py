nomes = []
idades = []

for i in range(5):
    nome = input("qual o seu nome? ")
    idade = int(input("qual a sua idade"))
    nomes.append(nome) 
    idades.append(idade)
    
for i in range(5):
    print(f"o seu nome e {nome[i]} e a sua idade e {idade[i]}  ")
    