from objetos import Humano
from objetos import Empleado
from objetos import Ingeniero
from objetos import Gerente

emp1 = Empleado("Carlos", 33, 7839876, 2700, "Parker")
emp2 = Ingeniero("Jose", 32, 765432, 4000, "Parker", "Mecatronica")
emp3 = Ingeniero("Pablo", 34, 890765, 4000, "Parker", "Mecatronica")
mgr1 = Gerente("Paco",55,567867,8000,"Parker","Mecatronica",[emp1])
#imprimir
mgr1.imprmir_empleados()
#mgr1.remover_empleado(emp1)