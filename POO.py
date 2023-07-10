class Persona():
    def inicializar(self, nom):
        self.nombre = nom

    def imprimir(self):
        print ("nombre: ", self.nombre)

#objeto1
Persona1 = Persona()
Persona1.inicializar("Eliam")
Persona1.imprimir()

#objeto2
Persona2 = Persona()
Persona2.inicializar("Nata")
Persona2.imprimir()
