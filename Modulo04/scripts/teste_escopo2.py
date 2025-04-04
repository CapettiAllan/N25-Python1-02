"""
Código de teste de escopo de variáveis no Python - 2
Author: Allan Capetti
Version: 2025-04-03
"""
from click import clear
# Definindo uma função
def calculo():
    global c, d # define que será usada uma var global c
    a = 5
    b = a + c
    c = 30
    d = 50
#programa principal
c = 10
print(calculo())
print("Valor de c =",c, "Valor de D =", d)