def main():
    x = int(input("Qual o valor do x: "))
    print(f"O valor do x ao quadrado é de {power(x)}")

def power(x):
    return pow(x, 2) 
main()