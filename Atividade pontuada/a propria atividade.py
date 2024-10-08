import os
os.system("cls || clear")

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
faltalhe_academia=[]
# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    sobrenome=input("Digite seu sobrenome:")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    #calculando ou verificando
    altura_quadrada=altura**altura
    peso_ideal=peso/altura_quadrada
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    faltalhe_academia.append(peso_ideal)
# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome com sobrenome:", nomes[i],sobrenome[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print("Peso ideal:", round(faltalhe_academia[i]),2)
if peso_ideal < 18.5:
    print("Abaixo do peso.")
elif 18.5<= peso_ideal <25:
    print("Peso normal")
elif 25<= peso_ideal <30:
    print("Sobrepeso")
elif 30<= peso_ideal <35:
    print("Obesidade grau I")
elif 35<= peso_ideal <40:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")
    print()