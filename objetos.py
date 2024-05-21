class Humano:
    aspiracion = "viajar"

    def __init__ (self,name,edad):
        self.name = name
        self.edad = edad
   
class Empleado(Humano):
    def __init__(self,name,edad,salario,n_empleado,empresa):
        super().__init__(name,edad)
        self.n_empleado = n_empleado
        self.salario = salario
        self.empresa = empresa

    def m_imprime(self):
        x = self.name, self.salario
        return x #Return = regresa un valor . Valor de una variable que se regresa dentro de un metodo(metodo y funciones).

    def salario_calculado(self,salario,extra):
        tiempo_extra = 0
        try:#We use it when we know something is going to go wrong, we are trying to excecute
            if extra > 1:
              self.salario = self.salario/ (salario/10) + extra
        except ZeroDivisionError:  #Used for the differente types of erros, we are already predicting the types of errors. Varibale identifies different erros.
            print("NOOOO")
        finally: #This always executes
            print("corazon")
        
    def imp_detalles(self):
        print("\nName: ", self.name)
        print("Edad: ", self.edad)
        print("Salario: ", self.salario)
        print("Correo: ", self.correo)
        print("Empresa: ", self.empresa)
        print("-------------------------")

class Ingeniero(Empleado):
    def __init__(self,name,edad,salario,n_empleado,empresa,rol):
        super().__init__(name,edad,salario,empresa,rol)
        self.rol = rol
        self.empresa = empresa
    def imp_detalles_emp(self):
        print("\nName:",self.rol)

class Gerente(Ingeniero):
    def __init__(self,nombre,edad,n_empledo,salario,empresa,rol,empleados=None):
        super().__init__(nombre,edad,n_empledo,salario,empresa,rol)
        if empleados is None :
            self.empleados = [] #[]- this symbolizes a list (listas).
        else:
            self.empleados = empleados
    def agregar_empleado(self,emp):
        if emp not in self.empleados:
            self.empleados.append(emp) #append:It is a method from lists, it adds stuff to the list as long as it's there.
    def remover_empleado(self,emp):
        if emp in self.empleados:
            self.empleados.remove(emp)
    def imprmir_empleados(self):
        for emp in self.empleados:
            print("\n-->", emp.m_imprime())

    
'''
#Main
emp1 = Empleado("Juan","22",430,"caro@.com","CNN")
#print(emp1.name,emp1.edad,emp1.salario,emp1.correo,emp1.empresa)
print (Empleado.imp_detalles)
#emp1.nombre = "Juana"
emp2 = Ingeniero("Juana","24",430,"Juana@.com","Temu","Electrico")


emp1.salario_calculado(430,60)
'''