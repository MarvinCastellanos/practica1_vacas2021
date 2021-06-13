from listaDoble import listaD
from nodo import contacto

lista=listaD()

def agrega():
    nombre=input('Ingrese el nombre: ')
    apellido=input('Ingrese el apellido: ')
    telefono=input('Ingrese el Telefono: ')
    nodo=contacto(nombre,apellido,telefono)
    lista.push(nodo)

def busca():
    telefono = input('Ingrese el telefono: ')
    if(lista.busca(telefono)==9999):
        while(True):
            op=input('El usuario no existe, desea agregarlo?(S/N): ')
            if op=='s' or op=='S':
                 agrega()
                 break
            elif op=='n' or op=='N':
                break

def menu():
    while(True):
        print('----------------------------------')
        print('1. Ingresar un nuevo contacto')
        print('2. Buscar contacto')
        print('3. Visualizar agenda')
        print('4. Salir') 
        opcion=input('Ingrese una opcion: ')
        print('----------------------------------')

        if opcion== '1':
            agrega()

        elif(opcion=='2'):
            busca()
        
        elif(opcion=='3'):
            lista.imprime()
            
        elif(opcion=='4'):
            break
        else:
            print('Opcion invalida!')

menu()


    

    