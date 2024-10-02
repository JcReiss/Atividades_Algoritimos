
#* função média
'''
def media(a,b,c):
    return ((a + b + c) / 3)
resultado = media(7, 8, 10)

print(resultado)
'''

#* função se idade é maior ou não
'''
def maior_idade(idades):
    if idades >=18:
        resultado = (f"a idade {idades} é maior ou igual a 18!")
    else:
        resultado = (f"a idade {idades} é menor que 18!")
    
    return resultado
print (maior_idade(17))
'''


#TODO  MÓDULOS
#TODO raiz quadrada    import math...  print (math.sqrt(25))
'''
import math 
print(math.sqrt(25))
'''



from  python meu_modulo.py import dobro
print(dobro(10))