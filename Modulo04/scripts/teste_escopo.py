"""
Código para demonstrar escopo de variável no Python
Author: Allan Capetti
Version: 2025-04-03
"""
from click import clear
# Definindo uma função
def calculo():
    a = 5
    b = a + c
#   c = 30                         #| se colocar a variável for definida após a conta que usa ela, da erro.
#                                  #| se definida dentro da função é uma variável local, se setar ela no programa principal, vira uma variável global
    return b
# Programa principal
clear()
c = 10 # as variáveis a e b só existem dentro da função, após a execução ela libera essas variáveis
print(calculo())