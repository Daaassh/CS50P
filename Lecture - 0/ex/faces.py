# Criando a função main que ira pegar os dados e passar para a função faces_check!
def main():
    result = input().capitalize()
    print(faces_check(result))

# Verificando o dado é vendo ce a string e tal e inserir uma carinha caso for
def faces_check(result):
    if result == "Hello :)":
        result = result.replace("Hello :)", "Hello 🙂")
    elif result == "Goodbye :(":
        result = result.replace("Goodbye :(", "Goodbye 🙁")
    else:
        result = "Hello 🙂 Goodbye 🙁"
    return result    
# Chamando a função main
main()