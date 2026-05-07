# Perfilador Automático de Datasets (Reto 05)

## Descripción
Esta herramienta automatiza el análisis exploratorio inicial de cualquier archivo CSV. Identifica la estructura del dataset, cuenta valores faltantes por columna y detecta registros duplicados, generando un reporte legible en la carpeta de resultados.

## Funcionamiento
1. Coloca tus archivos CSV en la carpeta `data/`.
2. Ejecuta el programa principal: `python main.py`.
3. Revisa los reportes generados en la carpeta `outputs/`.

## Métricas Analizadas
- **Conteo de Columnas y Filas**: Dimensión total del dataset.
- **Detección de Nulos**: Identifica qué columnas requieren mayor limpieza.
- **Registros Duplicados**: Calcula cuántas filas se repiten exactamente.

## Autor
Luis Fernando Partida Martinez - ESCOM IPN