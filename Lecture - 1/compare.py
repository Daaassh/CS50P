# Definindo a função para verificar ce o valor é igual!
def valor_igual(x,y):
    if x == y:
        print("X é igual a y")
    else:
        print("X não é igual a y")   

def main():
# Pegando os valores deles
    x = int(input("Digite o valor do x: "))
    y = int(input("Digite o valor do y: "))
    valor_igual(x,y)        
main()    