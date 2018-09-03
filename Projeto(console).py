### Precisa do SymPy e do MpMath
from decimal import Decimal
from sympy import *
import os
import math

metodo = 0          # Seleção do método de integração
indice = 0          # Para quarda o  valor de i nos for's para mostrar caso não seja continua em i
continuar = 'S'     # Continuar S ou N
menu = 'N'
x = symbols('x')    # Definição de x como um símbolo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

###### Método dos Retângulos #####

def mtdRetangulo(a, b, n): # a = limite inferior, b = limite superior e n = subintervalos
    integral = 0
    base = Decimal(str(abs(b-a)/n)) # Base do retângulo
    inicio = Decimal(a)                        

    for i in range(n):
        inicio += base
        integral += (funcao2.evalf(subs={x:(inicio)}))*base     # Soma a área de cada retângulo ao valor da integral
        indice = i
    return integral          

###### Método dos Trapézios #####

def mtdTrapezio(a, b, n): # a = limite inferior, b = limite superior e n = subintervalos
    integral = 0 
    base = Decimal(str(abs(b-a)/n)) # Base do Trapézio
    inicio = Decimal(a)
           
    for i in range(n):
        integral += (((funcao2.evalf(subs={x:(inicio)})) + funcao2.evalf(subs={x:(inicio+base)})) * base)/2
        inicio += base
        indice = i
        
    return integral

###### Método de Simpson ######

def mtdSimpson(a,b,n):
    integral = 0
    base = Decimal(str(abs(b-a)/n))
    inicio = Decimal(a)

    for i in range(n+1):

        #Integral = (1/3)*((b-a)/n)(f(a) + f(b) + 2*f(X(2n)) + 4*(f(X(2n+1))
        if(inicio != a and inicio != b):
            if(i % 2 == 0):                                                             # Se Xi, com i par então então f(Xi)*2
                #print("f(",inicio,") 1=",funcao2.evalf(subs={x:(inicio)})) #teste
                integral += ((2*base)/3)*(funcao2.evalf(subs={x:(inicio)})) # Soma dos valores em índices pares
            else:                                                                       # Se Xi, com i impar então f(Xi)*4
                #print("f(",inicio,") 2=",funcao2.evalf(subs={x:(inicio)})) #teste
                integral += ((4*base)/3)*(funcao2.evalf(subs={x:(inicio)})) # Soma dos Valores em índices ímpares
                                          
        elif (inicio == a):                                                             # X1
            #print("f(",limite1,") 3=",funcao2.evalf(subs={x:(a)})) #teste
            integral += (base/3)*(funcao2.evalf(subs={x:(a)}))  # Soma do primeiro valor
                                          
        elif (inicio == b):                                                             # Xn
            #print("f(",limite2,") 4=",funcao2.evalf(subs={x:(b)})) #teste
            integral += (base/3)*(funcao2.evalf(subs={x:(b)}))  # Soma do ultimo valor
        
        inicio += base
        indice = i
    return integral

###################################



while(continuar == 'S' or continuar == 's'):
    try:
        if(menu == 'n' or menu == 'N'):
            funcao = input("Entre com uma função continua para ser integrada f(x)= ")   # Função
            limite1 = float(input("Informe o limite inferior: "))                   # Limite inferior de integração
            limite2 = float(input("Informe o limite superior: "))                   # Limite superior de integração
            subintervalos = int(input("Informe a quantidade de subintervalos: "))   # Quantidade de subintervalos
        if(subintervalos >0):
            clear()    # Limpar a tela
                        
            # Menu    
            print("Deseja cálcular a integral definida de f(x)=", funcao,"de",limite1,"até",limite2,"usando qual método?")
            print("(1) - MÉTODO DOS RETÂNGULOS")
            print("(2) - MÉTODO DOS TRAPÉZIOS")
            print("(3) - MÉTODO DE SIMPSON")
            print("(4) - TODOS OS MÉTODOS")
            metodo = int(input("Digite o número relacionado ao método: "))      # Escolha do método
        
            funcao2 = sympify(funcao)   #  Conversão da string para uma expressão algébrica usando o SymPy

            clear()     # Limpar a tela
            
            if(metodo == 1):
                valorIntegral = mtdRetangulo(limite1, limite2, subintervalos)
                if(math.isinf(valorIntegral)):
                    print("A integral da função: f(x) =", funcao,"de",limite1,"até",limite2, "não converge")
                else:
                    print("A integral da função: f(x) =", funcao,"de",limite1,"até",limite2, "é aproximadamente %.3f" % valorIntegral)
                            
            elif(metodo == 2):        
                valorIntegral = mtdTrapezio(limite1, limite2, subintervalos)
                if(math.isinf(valorIntegral)):
                    print("A integral da função: f(x) =", funcao,"de",limite1,"até",limite2, "não converge")
                else:
                    print("A integral da função: f(x) =", funcao,"de",limite1,"até",limite2, "é aproximadamente %.3f" % valorIntegral)
                
            elif(metodo == 3):
                valorIntegral = mtdSimpson(limite1, limite2, subintervalos)
                if(math.isinf(valorIntegral)):
                    print("A integral da função: f(x) =", funcao,"de",limite1,"até",limite2, "não converge")
                else:
                    print("A integral da função: f(x) =", funcao,"de",limite1,"até",limite2, "é aproximadamente %.3f" % valorIntegral)
                
            elif(metodo == 4):
                valorIntegral = mtdRetangulo(limite1, limite2, subintervalos)
                valorIntegral1 = mtdTrapezio(limite1, limite2, subintervalos)
                valorIntegral2 = mtdSimpson(limite1, limite2, subintervalos)
                
                print("A integral da função f(x) =",funcao,"de",limite1,"até",limite2,"é aproximadamente:")
                
                if(math.isinf(valorIntegral) or math.isinf(valorIntegral1) or math.isinf(valorIntegral2)): #Se o valor das integrais forem números infinitos
                    print("A integral da função: f(x) =", funcao,"de",limite1,"até",limite2, "não converge")
                else:
                    print("Usando o método dos Retângulos = %.5f" % valorIntegral)
                    print("Usando o método dos Trapézios = %.5f" % valorIntegral1)
                    print("Usando o método de Simpson = %.5f" % valorIntegral2)
    
        else:
            clear()     # Limpar a tela  
            print("Subintervalo inválido")
        if(metodo != 4):
            print("\n\nDeseja calcular a integral de f(x)=",funcao,"de",limite1,"até",limite2,"usando outro método? (S/N):")
            menu = input()  
        if(menu == 'n' or menu == 'N'):
            continuar = input("\n\nDeseja calcular mais uma integral? (S/N): ")
        
        clear()     # Limpar a tela  
    except ZeroDivisionError:
        print("A função não é continua no intervalo [",limite1,",",limite2,"] em x = ",indice)
    except (RuntimeError, TypeError, NameError):
        print("Entrada inválida! \nf(x) = ",funcao)


        


        
