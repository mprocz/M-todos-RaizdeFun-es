from metodoCalculoRaiz import MetodosCalculoRaiz as mtd
import math
from os import system

def equation(x: float) -> float:
    return ( pow(math.e, -pow(x, 2)) - ( math.cos(x) ))

def derivada(x: float) -> float:
    return ( math.cos(x) -  pow(math.e, -pow(x, 2)) + x)

def fi(x: float) -> float:
    return ( math.cos(x) -  pow(math.e, -pow(x, 2)) + x)

def main():
    on = True
    while on:
        system("cls | clear")
        print("###############################################\n###############################################\n#                                             #\n#               Cálculo Númerico              #\n#             Zero de Funções Reais           #\n#                                             #\n###############################################\n###############################################\n")
        print(" Escolha o método desejado: \n")
        print(" { 1 - Método da Bissecção }\n { 2 - Método MIL }\n { 3 - Método de Newton }\n { 4 - Método da Secante }\n { 5 - Método Regula-Falsi }\n { 6 - Todos os Métodos }\n { 7 - Sair }\n\n")
        
        option = input("... ")
        if option == '1':
            a = float(input("Qual o primeiro valor do intervalo?\n... "))
            b = float(input("Qual o segundo valor do intervalo?\n... "))
            precisao = float(input("Qual a precisão?\n... "))
            n = int(input("Qual o número máximo de iterações?\n..."))

            mb = mtd.metodoDaBisseccao(a, b, precisao, n, equation)

            with open("res.txt", "w") as file:
                file.write("  k - raiz")
                while(mb != []):
                    file.write(mb.pop(0))

            
        elif option == '2':
            x0 = float(input("Qual a aproximação inicial?\n... "))
            precisao = float(input("Qual a precisão?\n... "))
            n = int(input("Qual o número máximo de iterações?\n..."))

            mm = mtd.metodoMIL(x0, precisao, n, equation, fi)

            with open("res.txt", "w") as file:
                file.write("  k - raiz")
                while(mm != []):
                    file.write(mm.pop(0))

        elif option == '3':
            x0 = float(input("Qual a aproximação inicial?\n... "))
            precisao = float(input("Qual a precisão?\n... "))
            n = int(input("Qual o número máximo de iterações?\n..."))

            mn = mtd.metodoDeNewton(x0, precisao, n, equation, derivada)

            with open("res.txt", "w") as file:
                file.write("  k - raiz")
                while(mn != []):
                    file.write(mn.pop(0))

        elif option == '4':
            a = float(input("Qual o primeiro valor do intervalo?\n... "))
            b = float(input("Qual o segundo valor do intervalo?\n... "))
            precisao = float(input("Qual a precisão?\n... "))
            n = int(input("Qual o número máximo de iterações?\n..."))

            ms = mtd.metodoDaSecante(a, b, precisao, n, equation)

            with open("res.txt", "w") as file:
                file.write("  k - raiz")
                while(ms != []):
                    file.write(ms.pop(0))

        elif option == '5':
            a = float(input("Qual o primeiro valor do intervalo?\n... "))
            b = float(input("Qual o segundo valor do intervalo?\n... "))
            precisao = float(input("Qual a precisão?\n... "))
            n = int(input("Qual o número máximo de iterações?\n..."))

            mrf = mtd.metodoRegulaFalsi(a, b, precisao, n, equation)

            with open("res.txt", "w") as file:
                file.write("  k - raiz")
                while(mrf != []):
                    file.write(mrf.pop(0))

        elif option == '6':
            a = float(input("Qual o primeiro valor do intervalo?\n... "))
            b = float(input("Qual o segundo valor do intervalo?\n... "))
            x0 = float(input("Qual a aproximação inicial?\n... "))
            precisao = float(input("Qual a precisão?\n... "))
            n = int(input("Qual o número máximo de iterações?\n..."))

            mb = mtd.metodoDaBisseccao(a, b, precisao, n, equation)
            mm = mtd.metodoMIL(x0, precisao, n, equation, fi)
            mn = mtd.metodoDeNewton(x0, precisao, n, equation, derivada)
            ms = mtd.metodoDaSecante(a, b, precisao, n, equation)
            mrf = mtd.metodoRegulaFalsi(a, b, precisao, n, equation)

            with open("res.txt", "w") as file:
                file.write("  k - Bissecção - MIL - Newton - Secante - RegulaFalsi")
                while(mb != [] or mm != [] or mn != [] or ms != [] or mrf != []):
                    if (mb != []):
                        file.write(mb.pop(0), "  -  ")
                    else:
                        file.write("null  -  ")
                    if (mm != []):
                        file.write(mm.pop(0), "  -  ")
                    else:
                        file.write("null  -  ")
                    if (mn != []):
                        file.write(mn.pop(0), "  -  ")
                    else:
                        file.write("null  -  ")
                    if (ms != []):
                        file.write(ms.pop(0), "  -  ")
                    else:
                        file.write("null  -  ")
                    if (mrf != []):
                        file.write(mrf.pop(0), "  -  ")
                    else:
                        file.write("null  -  ")
                    
                
        elif option == '7':
            print("\n\n Finalizando...\n")
            on = False

if __name__ == "__main__":
    main()
