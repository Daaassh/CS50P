# Criando a função para verificar os valores
def matching(name):
    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("E oque?")   

# Pegando os dados é executando a função matching

def main():
    name = input("Qual seu nome? ")
    matching(name)
main()
