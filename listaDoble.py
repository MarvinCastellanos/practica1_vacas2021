from nodo import contacto
from graphviz import Digraph

class listaD:
    def __init__(self):
        self.head=None
    
    def push(self,nodo):
        aux=self.head
        
        while (True):
            if(self.head==None):
                self.head=nodo
                break
            elif(nodo.getTelefono() == aux.getTelefono()):
                print('ERROR! El contacto ya existe')
                break
         #compara apellidos
            elif(nodo.getApellido().lower() < aux.getApellido().lower()):
                if (aux==self.head):
                    aux.setAnterior(nodo)
                    nodo.setSiguiente(aux)
                    self.head=nodo
                    break
                else:
                    nodo.setAnterior(aux.getAnterior())
                    aux.getAnterior().setSiguiente(nodo)
                    nodo.setSiguiente(aux)
                    aux.setAnterior(nodo)
                    break
         #si apellidos son iguales
            elif(nodo.getApellido().lower() == aux.getApellido().lower()):
             #compara nombres
                if(nodo.getNombre().lower() < aux.getNombre().lower()):
                    if (aux==self.head):
                        aux.setAnterior(nodo)
                        nodo.setSiguiente(aux)
                        self.head=nodo
                        break
                    else:
                        nodo.setAnterior(aux.getAnterior())
                        aux.getAnterior().setSiguiente(nodo)
                        nodo.setSiguiente(aux)
                        aux.setAnterior(nodo)
                        break
             #Si nombres son iguales
                else:
                    nodo.setAnterior(aux.getAnterior())
                    aux.getAnterior().setSiguiente(nodo)
                    nodo.setSiguiente(aux)
                    aux.setAnterior(nodo)
                    break
            elif aux.getSiguiente()==None:
                nodo.setAnterior(aux)
                aux.setSiguiente(nodo)
                break
            else:
                aux=aux.getSiguiente()
    
    def busca(self, numero):
        aux=self.head
        if(self.head==None):
            print('La Agenda esta vacia')
            return 9999
        else:
            while(True):
                if(aux.getTelefono() == numero):
                    print('----------------------------------')
                    print('Contacto: ')
                    print('Nombre: '+ aux.getNombre())
                    print('Apellido: '+ aux.getApellido())
                    print('Telefono: '+ aux.getTelefono())
                    print('----------------------------------')
                    break
                elif(aux.getSiguiente()==None):
                    #print('El contacto no exite')
                    return 9999
                else:
                    aux=aux.getSiguiente()

    def imprime(self):
        aux=self.head
        dot=Digraph(comment='Lista de contactos')
        dot.node('Cabecera','Agenda')
        while(True):
            if self.head==None:
                break
            else:
                texto='Nombre: '+aux.getNombre()+'\nApellido: '+aux.getApellido()+'\nTelefono: '+aux.getTelefono()
                dot.node(aux.getTelefono(),texto)
                
                if(aux==self.head):
                    dot.edge('Cabecera',aux.getTelefono())
                    if aux.getSiguiente() is not None:
                        dot.edge(aux.getTelefono(),aux.getSiguiente().getTelefono())
                        aux=aux.getSiguiente()
                    else:
                        break
                elif(aux.getSiguiente()==None):
                    dot.edge(aux.getTelefono(),aux.getAnterior().getTelefono())
                    break
                else:
                    dot.edge(aux.getTelefono(),aux.getAnterior().getTelefono())
                    dot.edge(aux.getTelefono(),aux.getSiguiente().getTelefono())
                    aux=aux.getSiguiente()

        dot.render('Contactos',view=True)                  

            