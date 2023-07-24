# Criando a função main para pegar os dados. 
def main():
    x = int(input("Qual o valor do x: "))
    print(f"O valor do x ao quadrado é de {power(x)}")

# Função para verificar o valor do x ao quadrado!
def power(x):
    return pow(x, 2) 

# Iniciando a função main
main()