# Criando uma função para verificar a nota

def check_score(score):
    if score >= 90:
        result = print("Nota: A")
    elif score >= 80:
        result = print("Nota: B")    
    elif score >= 70:
        result = print("Nota: C")   
    elif score >= 60:
        result = print("Nota: D")
    else:
        result = print("Nota: F") 
    return result
# Pegando a score é executando a função para verificar as notas

score = int(input("Qual foi a sua nota: "))
check_score(score)

