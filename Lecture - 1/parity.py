# Criando a função para pegar os dados e chamando a função is_even
def main():
    x = int(input("Digite o valor do x: "))
    if is_even(x):
        print("Par")
    else:
        print("Impar")      
# Criando a função is_even para verificar ce o numero é par ou impar!
def is_even(x):
    return(x % 2 == 0)
main()        