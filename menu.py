import calculadora
def menu():  
    print("\n=== Calculadora ===")  
    print("1. Somar")  
    print("2. Subtrair")  
    print("3. Multiplicar")  
    print("4. Dividir")  
    print("0. Sair")  
    escolha = input("Escolha uma opção: ")  

    if escolha == "1":  
        num1 = float(input("Digite o primeiro número: "))  
        num2 = float(input("Digite o segundo número: "))
        resultado = calculadora.somar(num1, num2)  
        print(f"Resultado: {resultado}") 
    elif escolha == "0":
        return
    elif escolha == "2":  
        num1 = float(input("Digite o primeiro número: "))  
        num2 = float(input("Digite o segundo número: "))  
        resultado = calculadora.subtrair(num1, num2)  
        print(f"Resultado: {resultado}")  
        return

if __name__ == "__main__":  
    menu()