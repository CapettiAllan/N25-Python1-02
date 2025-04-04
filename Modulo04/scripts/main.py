"""
Programa principal.
Author: Allan Capetti
Version: 2025-04-03
"""
import funcoes
from click import clear # importando somente a função clear
clear() # Limpa o console
funcoes.cabecalho(colunas=50, titulo="Bem vindo!")
funcoes.cabecalho("Olá turma, boa noite!", 30)
funcoes.cabecalho()
funcoes.cabecalho(colunas=15)
print("fatorial de 5 =",funcoes.fatorial(5))
print("fatorial de 5 =",funcoes.fatorial_rec(999)) # com valor 1000 da erro de stack overflow - estouro