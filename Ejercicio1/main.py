import datetime


"""
1. Realiza un programa, valida si es una fecha válida y formato.
Formato esperado dd/MM/yyyy
Entradas: 45/13/2002, 03/02/2001, 01/20/2010, 02-04-2010
"""

def validar(fecha):
    
    dividir = fecha.split('/')
    if(len(dividir)!=3):
        return False
    d,m,a = dividir

    try:
        datetime.datetime(int(a),int(m),int(d))
        return True
    except ValueError:
        return False






if __name__=="__main__":
    print("Ingresar fecha",end=': ')
    fecha = input()
    if(validar(fecha)):
        print("fecha válida")
    else:
        print("fecha no válida")