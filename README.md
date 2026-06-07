Sistema de Gestión de Inventario: STOCK-GAMER

¡Bienvenido al Sistema de Gestión de Inventario para Pro-Gamer Logistics! Este es un programa interactivo desarrollado en Python para la terminal que permite administrar de punta a punta un catálogo de productos informáticos orientados al ecosistema gaming.
El sistema cuenta con un robusto bloque de validaciones nativas (sin librerías externas) para asegurar la integridad de los datos ingresados en el inventario.

🚀 Características Principales
Altas, Bajas y Modificaciones (ABM):
Alta: Registro de nuevos productos con generación de ID automático único basado en su categoría. Permite seleccionar nombres y marcas desde un catálogo precargado o ingresar datos 100% personalizados.
Baja con reglas de negocio: No se permite eliminar un producto si todavía tiene existencias físicas disponibles en stock.
Modificaciones precisas: Control individual para sumar, restar o establecer el stock exacto (buscando por nombre), y opción para actualizar precios (buscando por ID).
Informe General Avanzado: Muestra todo el inventario estructurado visualmente en forma de tabla alineada por consola. El listado se ordena mediante el algoritmo de ordenamiento de burbuja, priorizando el stock de forma descendente y usando el nombre alfabéticamente como criterio de desempate.
Validaciones Nativas Rigurosas: Control estricto carácter por carácter para asegurar que los precios sean decimales positivos, el stock sea un entero mayor a cero, las marcas cumplan con longitudes mínimas y los nombres de productos comiencen formalmente con letras.


🛠️ Estructura del Código
El archivo principal (TPO segundo parcial Version Final.py) se divide de manera modular en las siguientes secciones:

Bloque / Sección,Descripción
Variables Globales,"Bases de datos locales en listas (categorías, marcas y strings predefinidos para agilizar la carga de productos)."

Bloque 1: Validaciones de Texto,"Algoritmos para verificar IDs duplicados, descripciones válidas, marcas y formateo estricto de categorías (.capitalize())."

Bloque 2: Validaciones Numéricas,Funciones que recorren los strings carácter por carácter para certificar si son números enteros o decimales legítimos (gestionando signos negativos y puntos flotantes).

Lógica de Negocio y Utilidades,"Generación de IDs (ej: MON503 para un Monitor), búsquedas indexadas y ordenamiento de arrays."

Funciones del Sistema (Módulos),"Funciones principales expuestas al usuario: agregar_producto, eliminar_producto, modificar_stock, modificar_precio e informe_general."

Menú e Interfaz,El bucle principal (main()) que mantiene el programa corriendo y procesa la navegación del usuario.
