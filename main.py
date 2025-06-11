# main.py
from src.controllers.sistema_gestion import SistemaGestionEmpleados

def main():
    """Función principal para ejecutar el sistema de gestión de empleados."""
    sistema = SistemaGestionEmpleados()
    sistema.ejecutar()

if __name__ == "__main__":
    main()
