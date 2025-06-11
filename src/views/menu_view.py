# src/views/menu_view.py
import os

class MenuView:
    """Clase encargada de la interfaz de usuario y la presentación del menú."""
    def _limpiar_pantalla(self):
        """Limpia la consola para una mejor experiencia de usuario."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_menu(self):
        """Muestra las opciones principales del menú."""
        print("\n=== Sistema de Gestión de Empleados ===")
        print("1. Agregar Nuevo Empleado")
        print("2. Listar Todos los Empleados")
        print("3. Ver Detalles de Empleado")
        print("4. Salir")
        print("=======================================")

    def obtener_opcion_menu(self):
        """Solicita y retorna la opción seleccionada por el usuario."""
        return input("Seleccione una opción: ")

    def solicitar_datos_empleado(self):
        """Solicita al usuario los datos para crear un nuevo empleado."""
        print("\n--- Agregar Nuevo Empleado ---")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI: ")
        cargo = input("Cargo: ")
        while True:
            try:
                salario = float(input("Salario: "))
                break
            except ValueError:
                print("Salario inválido. Por favor, ingrese un número.")
        return {'nombre': nombre, 'apellido': apellido, 'dni': dni, 'cargo': cargo, 'salario': salario}

    def solicitar_indice_empleado(self):
        """Solicita el número de empleado para ver sus detalles."""
        while True:
            try:
                opcion = int(input("\nIngrese el número del empleado para ver detalles (0 para cancelar): "))
                return opcion
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
    
    def mostrar_mensaje(self, mensaje):
        """Muestra un mensaje genérico al usuario."""
        print(mensaje)

    def esperar_enter(self):
        """Espera que el usuario presione Enter para continuar."""
        input("\nPresione Enter para continuar...")
        self._limpiar_pantalla()

    def mostrar_lista_vacia(self):
        """Mensaje específico cuando la lista de empleados está vacía."""
        print("\nNo hay empleados registrados.")
