# src/models/empleado.py
class Empleado:
    """Clase que representa a un empleado."""
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.dni = ""
        self.cargo = ""
        self.salario = 0.0

    def mostrar_detalles(self):
        """Muestra los detalles completos del empleado."""
        print(f"\n--- Detalles del Empleado ---")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: ${self.salario:,.2f}")
        print(f"----------------------------")
