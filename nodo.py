class contacto:
    def __init__(self,nombre,apellido,telefono):
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        self.siguiente=None
        self.anterior=None
    
    def setSiguiente(self,nodo):
        self.siguiente=nodo
    
    def getSiguiente(self):
        return self.siguiente

    def setAnterior(self,nodo):
        self.anterior=nodo
    
    def getAnterior(self):
        return self.anterior

    def getTelefono(self):
        return self.telefono
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido