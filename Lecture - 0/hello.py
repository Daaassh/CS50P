def main():
    # Pergunta ao usuario o seu nome, Remove os espaços em branco e adiciona as 1 letras das palavras para maisculo!
    name = input("Qual é o seu nome? ").strip().title()
    # Diz olá ao mundo!
    return name

# Definindo uma função
def hello(to="world"):
    print(f"Olá, {main()}")



hello()
