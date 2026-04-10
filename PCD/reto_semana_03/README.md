# Clasificador de Temperaturas (Reto 03)

## Descripción
Este programa es una herramienta de procesamiento de datos diseñada para consolidar transacciones diarias de una tienda de tecnología. Su función principal es transformar una lista de ventas individuales en un reporte ejecutivo agrupado por producto, permitiendo identificar rápidamente los artículos más rentables mediante el análisis de ingresos y precios promedio.

## Caracterisicas Principales
Agrupamiento Inteligente: Consolida múltiples transacciones del mismo producto en una única entrada de reporte.

Métricas de Negocio: Calcula automáticamente el total de unidades vendidas, el ingreso total generado y el precio promedio de venta por artículo.

Ordenamiento de Rentabilidad: El reporte final se entrega ordenado de mayor a menor ingreso total.

Procesamiento Robusto: Capacidad para ignorar líneas con datos corruptos, precios no numéricos o formatos incompletos sin interrumpir la ejecución.

## Requisitos de Procesamiento
1.Consolidación: Suma de cantidades y cálculo de (cantidad * precio) por cada fila del mismo producto.

2.Promedios: El precio promedio se obtiene dividiendo el ingreso total entre las unidades vendidas.

3.Formato: Los valores monetarios se presentan con exactamente dos decimales.

4.Validación: Se descarta cualquier fila que no cumpla con las 4 columnas requeridas o contenga valores no numéricos en cantidad y precio.

## Instrucciones de Uso
El programa utiliza la entrada estándar (stdin) para leer los datos y la salida estándar (stdout) para entregar el reporte CSV.

Ejecución en Terminal

# Ejecución básica con redirección de archivo
python main.py < tests/entrada1.txt

## Autor:
Luis Fernando Partida Martinez - Estudiante de Ciencia de Datos (ESCOM)


# Guardar el reporte en un nuevo archivo
python main.py < tests/entrada1.txt > reporte_consolidado.csv

## Autor
Luis Fernando Partida Martinez - Estudiante de Ciencia de Datos (ESCOM)
