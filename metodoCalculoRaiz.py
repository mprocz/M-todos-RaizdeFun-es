from typing import List

class MetodosCalculoRaiz:
    def metodoDaBisseccao(a: float, b: float, precisao: float, n: int, equation) -> List:
        result = []
        k = 0
        meio = 0.0
        if (abs(b-a) > precisao):
            meio = 0.0
            while (abs(b-a) > precisao and k < n):
                k = k + 1
                finicio = equation(a)
                meio = (a+b)/2
                fmeio = equation(meio)

                if ((finicio * fmeio) < 0):
                    b = meio
                else:
                    a = meio
                result.append((k, meio))
                
        else:
            meio = a
            result.append((k, meio))

        return result

    def metodoMIL(x0: float, precisao: float, n: int, equation, fi) -> List:
        result = []
        x0 = float(input("X0: "))
        precisao = float(input("Precisão: "))
        it = 100
        e = 0.0
        k = 0
        
        if (abs(equation(x0)) < precisao):
            e = x0
            result.append((k, e))
        else:
            k=1
            x1 = fi(x0)
            e = x1
            result.append((k, e))
            while (equation(x1) > precisao and abs(x1-x0) > precisao and k < it):
                x1 = fi(x0)
                x0 = x1
                k += 1
                e = x1
            result.append((k, e))

        
        return result

    def metodoDeNewton(x0: float, precisao: float, n: int, equation, derivada) -> List:
        result = []
        x1 = None
        fx = None
        fxlinha = None 
        raiz = None

        k = 0
        fx = equation(x0)
        if (fx > precisao):

            k = 1
            fxlinha = derivada(x0)
            x1 = x0 - (fx / fxlinha)
            fx = equation(x1)
            raiz = x1
            result.append((k, raiz))
            while (abs(fx) > precisao and abs(x1 - x0) and k < n):
                k = k + 1
                x0 = x1
                fxlinha = derivada(x0)
                x1 = x0 - (fx / fxlinha)
                fx = equation(x1)
                raiz = x1
                result.append((k, raiz))

        else:
            raiz = x0
            result.append((k, raiz))

        return result

    def metodoDaSecante(x0: float, x1: float, precisao: float, n: int, equation) -> List:
        result = []
        raiz = None
        k = 0
        if (equation(x0) < precisao):
            raiz = x0
            result.append((k, raiz))
        elif (equation(x1) < precisao or abs(x1-x0) < precisao):
            raiz = x1
        else:
            k = 1
            while (abs(x1 - x0) > precisao and equation(x1) > precisao and k < n):
                x2 = (x1 - ((equation(x1)*(x1-x0)) / (equation(x1)-equation(x0))))
                x0 = x1
                x1 = x2
                raiz = x1
                result.append((k, raiz))
                k += 1
        
        return result

    def metodoRegulaFalsi(a: float, b: float, precisao: float, n: int, equation) -> List:
        result = []
        raiz = None
        k = 0
        if (abs(b - a) < precisao):
            raiz = a
            result.append((k, raiz))
        elif (abs(equation(a)) < precisao or abs(equation(b)) < precisao): 
            raiz = a
            result.append((k, raiz))
        else: 
            k = 1
            x = a

            while(abs(equation(x)) > precisao and abs(b-a) > precisao and k < n):
                m = equation(a)
                x = (( a*equation(b) - b*equation(a) ) / (equation(b) - equation(a)))
                if (m*equation(x) > 0):
                    a = x
                else:
                    b = x
                result.append((k, raiz))
                k += 1

        return result
