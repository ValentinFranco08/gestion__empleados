
# Gestión de Empleados

Este proyecto es un sistema básico de gestión de empleados desarrollado en Python, diseñado para demostrar la implementación de patrones de diseño **Singleton** y **Builder** en un contexto práctico. Es ideal para estudiantes que buscan comprender cómo estos patrones estructuran y mejoran la modularidad del código.

---

## 🚀 Características

* **Agregar Empleados:** Permite registrar nuevos empleados con sus datos básicos (nombre, apellido, DNI, cargo, salario).
* **Listar Empleados:** Muestra un listado de todos los empleados registrados.
* **Ver Detalles:** Permite consultar la información completa de un empleado específico.
* **Menú Interactivo:** Un sistema de menú en consola fácil de usar para navegar por las funcionalidades.

---

## 🛠️ Patrones de Diseño Implementados

### 1. Singleton

* **Clase:** `BaseDeDatosEmpleados`
* **Propósito:** Asegura que solo exista **una única instancia** de la clase que gestiona la colección de empleados. Esto simula una "base de datos" centralizada a la que todas las partes del sistema acceden, garantizando coherencia en los datos.

### 2. Builder

* **Clase:** `EmpleadoBuilder`
* **Propósito:** Facilita la **construcción paso a paso** de objetos `Empleado`. Esto desacopla el proceso de creación de la representación final del objeto, permitiendo un código más legible y flexible, especialmente útil si los objetos `Empleado` tuvieran muchos atributos o diferentes formas de inicialización.

---

## 📂 Estructura del Proyecto

El proyecto sigue una estructura modular dentro de la carpeta `src/` para una mejor organización y separación de responsabilidades.

## ⚙️ Cómo Ejecutar el Proyecto

Sigue estos pasos para poner en marcha el sistema:

1.  **Clonar el Repositorio:**
    ```bash
    git clone git@github.com:ValentinFranco08/gestion__empleados.git
    ```

2.  **Navegar al Directorio del Proyecto:**
    ```bash
    cd gestion__empleados
    ```

3.  **Ejecutar la Aplicación:**
    ```bash
    python main.py
    ```

Una vez ejecutado, el sistema presentará un menú interactivo en la consola.

