
from datetime import datetime,date

"""
3. Realiza un programa que despliega un menú con las siguientes opciones:
● Registrar empleados, con las siguientes características: id, nombre,apellido
paterno, apellido materno, fecha de nacimiento.
● Obtener la edad de un empleado, pasando por parámetro de búsqueda el id.
● Obtener lista de empleados por orden alfabético apellido.
● Obtener lista de empleados por orden de edad.
Plus: Agregar validaciones por tipo de dato a introducir.
"""

class Empleado:

    def __init__(self,id,nombre,paterno,materno,nacimiento):
        self.id=id
        self.nombre=nombre
        self.paterno=paterno
        self.materno=materno
        self.nacimiento=nacimiento
        
class Lista:

    def __init__(self):
        self.lista=[]

    def registrar(self,empleado):
        self.lista.append(empleado)

    def obtenerEdad(self,id):
        noEncontrado = True
        for i in self.lista:
            if(i.id==id):
                hoy = date.today()
                fecNacimiento = datetime.strptime(i.nacimiento,'%d/%m/%Y')
                edad = hoy.year - fecNacimiento.year - ((hoy.month, hoy.day) < (fecNacimiento.month, fecNacimiento.day))
                print("La edad de ",i.nombre,i.paterno,i.materno,"es de",edad)
                noEncontrado = False
        if(noEncontrado):
            print("No se encontro el id")

    def obtenerOrdenAlfabetico(self):
         for i in sorted(self.lista, key = lambda x: x.paterno):
            print('ID:',i.id,'Nombre:',i.nombre,'Apellido Paterno:',i.paterno,'Apellido Materno:',i.materno,'Fecha de nacimiento:',i.nacimiento)

    def obtenerOrdenEdad(self):
        listaEdad = []
        for i in self.lista:
            
            hoy = date.today()
            fecNacimiento = datetime.strptime(i.nacimiento,'%d/%m/%Y')
            edad = hoy.year - fecNacimiento.year - ((hoy.month, hoy.day) < (fecNacimiento.month, fecNacimiento.day))
            listaEdad.append([i,edad])

        for i in sorted(listaEdad, key = lambda x: x[1]):
            print('ID:',i[0].id,'Nombre:',i[0].nombre,'Apellido Paterno:',i[0].paterno,'Apellido Materno:',i[0].materno,'Fecha de nacimiento:',i[0].nacimiento,'Edad: ',i[1])
            

if __name__=="__main__":
    
    empleados = Lista()

    while(True):
        print("1. Registrar empleados")
        print("2. Obtener la edad de un empleado")
        print("3. Obtener lista de empleados por orden alfabético apellido")
        print("4. Obtener lista de empleados por orden de edad")
        print("5. Salir")
        opcion = int(input())
        if(opcion==1):
            print("ID",end=': ')
            id = int(input())
            print("Nombre",end=': ')
            nombre = input()
            print("Apellido Paterno",end=': ')
            paterno = input()
            print("Apellido Materno",end=': ')
            materno = input()

            try:
                print("Fecha de nacimiento en el formato DD/MM/YYYY",end=': ')
                nacimiento = input()
                datetime.strptime(nacimiento,'%d/%m/%Y')
                objEmpleado = Empleado(id,nombre,paterno,materno,nacimiento)
                empleados.registrar(objEmpleado)
            except ValueError:
                print("Fecha inválida")


           

        elif(opcion==2):
            print("ID",end=': ')
            id = int(input())
            empleados.obtenerEdad(id)
        elif(opcion==3):
            empleados.obtenerOrdenAlfabetico()
        elif(opcion==4):
            empleados.obtenerOrdenEdad()
        elif(opcion==5):
            break
