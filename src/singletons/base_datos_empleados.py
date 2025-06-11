# src/singletons/base_datos_empleados.py
class BaseDeDatosEmpleados:
    """
    Singleton que gestiona la colección de empleados.
    Asegura que solo exista una única instancia de esta clase.
    """
    _instance = None
    _empleados = [] # Lista para almacenar los objetos Empleado

    def __new__(cls):
        """
        Implementa el patrón Singleton, asegurando que solo se cree
        una instancia de BaseDeDatosEmpleados.
        """
        if cls._instance is None:
            cls._instance = super(BaseDeDatosEmpleados, cls).__new__(cls)
        return cls._instance

    def agregar_empleado(self, empleado):
        """Agrega un nuevo empleado a la base de datos."""
        self._empleados.append(empleado)
        print(f"Empleado '{empleado.nombre} {empleado.apellido}' agregado con éxito.")

    def listar_empleados(self):
        """Lista todos los empleados registrados en la base de datos."""
        if not self._empleados:
            print("\nNo hay empleados registrados.")
            return []
        
        print("\n--- Lista de Empleados ---")
        for i, empleado in enumerate(self._empleados):
            print(f"{i+1}. {empleado.nombre} {empleado.apellido} (DNI: {empleado.dni})")
        print("--------------------------")
        return self._empleados # Retorna la lista para facilitar el acceso en otras partes

    def obtener_empleado_por_indice(self, indice):
        """
        Obtiene un empleado de la lista por su índice.
        Retorna el empleado si el índice es válido, de lo contrario None.
        """
        if 0 <= indice < len(self._empleados):
            return self._empleados[indice]
        return None
