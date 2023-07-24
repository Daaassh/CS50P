# Definindo a main, Pegando os valores total é o da porcentagem e chamando a função para calcular o preço
def main():
    total_value = float(input("How much was the meal? ").replace("$", ""))
    porcentage_value = float(input("What percentage would you like to tip? ").replace("%", ""))
    print(f"Leave: ${return_value(total_value, porcentage_value):.2f}")

# Criando a função para calcular o preço!

def return_value(total_value, porcentage_value):
    return total_value  * (porcentage_value / 100)


# Chamando a função para main  
main()