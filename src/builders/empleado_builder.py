# src/builders/empleado_builder.py
from src.models.empleado import Empleado

class EmpleadoBuilder:
    """Builder para construir objetos Empleado de forma incremental."""
    def __init__(self):
        self.empleado = Empleado()

    def con_nombre(self, nombre):
        self.empleado.nombre = nombre
        return self # Permite encadenamiento

    def con_apellido(self, apellido):
        self.empleado.apellido = apellido
        return self

    def con_dni(self, dni):
        self.empleado.dni = dni
        return self

    def con_cargo(self, cargo):
        self.empleado.cargo = cargo
        return self

    def con_salario(self, salario):
        self.empleado.salario = salario
        return self

    def construir(self):
        """Retorna el objeto Empleado construido."""
        return self.empleado
