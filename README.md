"Pro Gamer Logistics" , Sistema de Gestión de Suministros para Gaming Houses.
Conformado por: Manuel Dos Ramos(1239249), Esteban Jumilla (1234464), Juan Cruz Gallo (1235624) y Lautaro Cordoba (1235670).


Este programa fue desarrollado como trabajo practico obligatorio para la materia Pensamiento computacional,algoritmica y programacion. El objetivo fue construir un sistema de gestion de inventario para la empresar "UADETech Corp.", aplicando los conceptos vistos en clase.
Esta completamente modularizado en funciones con responsabilidades claras, implementa los algoritmos manualmente y separa las validaciones del flujo principal del programa. Cada integrante del equipo tuvo un rol definido y el codigo refleja esa division de trabajo.

Bloque  Validaciones:
        Bloque 1 Validaciones de texto: contiene las funciones que verifican que los datos ingresados por el usuario sean    correctos, como el identificador, la descripcion, la categoria y la marca.
Tambien incluye las funciones de busqueda por ID y por nombre.
 
        Bloque 2 - Validaciones numericas: verifica que el precio sea un decimal positivo y que el stock sea un entero mayor o igual a 1. Incluye tambien la generacion de IDs unicos y funciones auxiliares de soporte.
Mostrar inventario: imprime el inventario en formato de tablaalineada. Incluye el ordenamiento por burbuja de mayor a menor stock, con desempate alfabetico por nombre.
 
Agregar producto: registra un nuevo producto llamando a todas las validaciones antes de guardarlo en el inventario.
 
Eliminar producto: permite dar de baja un producto unicamente si su stock es igual a cero, solicitando confirmacion previa.
 
Modificar stock: busca el producto por nombre y permite sumar, restar o establecer el stock exacto.
 
Modificar precio: busca el producto por ID y actualiza su precio validando que sea un decimal positivo.
 
Buscar producto: permite buscar por nombre, categoria o marca mostrando los resultados encontrados.
 
Menu principal: coordina el flujo general del programa mostrando las opciones al usuario y derivando a cada funcion segun la
opcion seleccionada.

La metodologia de trabajo consistio en dividir el desarrollo en roles claros desde el inicio. Las validaciones se separaron en dos partes: un bloque de texto y uno numerico, cada uno con funciones especificas y probadas de forma independiente antes de integrarse al sistema. El resto del codigo, menu y stock, siguio la misma logica modular. Una vez que cada parte estuvo lista y probada, se realizo el merge integrando los bloques y verificando que funcionaran en conjunto. Este enfoque permitio detectar errores de forma aislada y facilito la comprension de cada parte del codigo durante la defensa.
