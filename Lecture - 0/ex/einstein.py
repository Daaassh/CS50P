# Criando a função main, é printando o valor!
def main():
    number = int(input("m: "))
    print(f"E: {multiply(number)}")

# Multiplicando pelo valor do bagulho do einstein
def multiply(number):
    number = int(number * 90000000000000000)
    return number

# Chamando a função main
main()