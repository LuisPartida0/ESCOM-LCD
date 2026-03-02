# Calculadora de Sumas Robustas (Reto 01)

## Descripción
Este programa procesa archivos de texto con datos de ventas "sucios" (caracteres extra, espacios, decimales) y calcula el total entero por día, truncando los valores decimales antes de sumarlos.

## Instrucciones de Uso
El programa lee datos desde la entrada estándar (`stdin`).

### En Linux / Mac / PowerShell:
```bash
python main.py < tests/entrada1.txt

###Ejemplo de entrada
1.9, 2.1, 3.7
1a2, 3b, 4

###Ejemplo de salida
6
19

