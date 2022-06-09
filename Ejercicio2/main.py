"""
2. Realiza un programa, el usuario puede introducir una cadena de caracteres y le
mostraras de salida cuántos números existen en la cadena.
Ejemplo:
Entrada : jj@dud324khsa123h12
Salida: 8
"""

def contar(entrada):
    return len([ 1  for i in entrada if i.isdigit()])
    

if __name__=="__main__":
    print("Entrada",end=': ')
    entrada = input()
    print( "Salida: ",contar(entrada))