# src/controllers/sistema_gestion.py
from src.builders.empleado_builder import EmpleadoBuilder
from src.singletons.base_datos_empleados import BaseDeDatosEmpleados
from src.views.menu_view import MenuView

class SistemaGestionEmpleados:
    """
    Controlador principal del sistema de gestión de empleados.
    Orquesta las interacciones entre la vista, el modelo y el builder.
    """
    def __init__(self):
        self.db = BaseDeDatosEmpleados() # Obtiene la única instancia del Singleton
        self.view = MenuView() # Crea una instancia de la vista para interactuar con el usuario

    def _agregar_empleado(self):
        """Controla el flujo para agregar un nuevo empleado."""
        datos = self.view.solicitar_datos_empleado()

        # Usa el Builder para construir el objeto Empleado
        empleado = EmpleadoBuilder() \
            .con_nombre(datos['nombre']) \
            .con_apellido(datos['apellido']) \
            .con_dni(datos['dni']) \
            .con_cargo(datos['cargo']) \
            .con_salario(datos['salario']) \
            .construir()

        self.db.agregar_empleado(empleado)
        self.view.esperar_enter()

    def _listar_empleados(self):
        """Controla el flujo para listar todos los empleados."""
        self.view._limpiar_pantalla()
        empleados = self.db.listar_empleados()
        if not empleados:
            self.view.mostrar_lista_vacia()
        self.view.esperar_enter()

    def _ver_detalles_empleado(self):
        """Controla el flujo para ver los detalles de un empleado específico."""
        self.view._limpiar_pantalla()
        empleados = self.db.listar_empleados() # Muestra la lista para que el usuario elija
        
        if not empleados:
            self.view.mostrar_lista_vacia()
            self.view.esperar_enter()
            return

        opcion = self.view.solicitar_indice_empleado()
        if opcion == 0:
            self.view._limpiar_pantalla()
            return

        empleado = self.db.obtener_empleado_por_indice(opcion - 1)
        if empleado:
            empleado.mostrar_detalles()
        else:
            self.view.mostrar_mensaje("Número de empleado inválido.")
        self.view.esperar_enter()

    def ejecutar(self):
        """Ejecuta el bucle principal del sistema de gestión."""
        while True:
            self.view.mostrar_menu()
            opcion = self.view.obtener_opcion_menu()

            if opcion == '1':
                self._agregar_empleado()
            elif opcion == '2':
                self._listar_empleados()
            elif opcion == '3':
                self._ver_detalles_empleado()
            elif opcion == '4':
                self.view.mostrar_mensaje("Saliendo del sistema. ¡Hasta luego!")
                break
            else:
                self.view.mostrar_mensaje("Opción inválida. Por favor, intente de nuevo.")
                self.view.esperar_enter()
