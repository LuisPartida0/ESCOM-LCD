import sys

def limpiar_valor(valor):
    """
    Limpia un valor individual:
    - Quita espacios en los extremos.
    - Elimina cualquier carácter que no sea dígito, punto o signo negativo.
    """
    valor = valor.strip()
    caracteres_validos = '0123456789.-'
    # Filtrar solo los caracteres permitidos
    limpio = "".join(char for char in valor if char in caracteres_validos)
    return limpio

def convertir_y_truncar(texto_limpio):
    """
    Convierte el string limpio a número y lo trunca a entero.
    Si el valor está vacío o no es un número válido, retorna 0.
    """
    if not texto_limpio:
        return 0
    try:
        # Primero a float para manejar decimales, luego a int para truncar
        return int(float(texto_limpio))
    except ValueError:
        # En caso de formatos inválidos (ej. "1.2.3" o "--5")
        return 0

def procesar_linea(linea):
    """
    Procesa una línea completa:
    - Maneja líneas vacías.
    - Separa por comas.
    - Limpia, trunca y suma cada elemento.
    """
    linea = linea.strip()
    if not linea:
        return 0
    
    elementos = linea.split(',')
    suma_total = 0
    
    for item in elementos:
        limpio = limpiar_valor(item)
        valor_entero = convertir_y_truncar(limpio)
        suma_total += valor_entero
        
    return suma_total

def main():
    """
    Punto de entrada: lee de stdin línea por línea y muestra el resultado.
    """
    try:
        for linea in sys.stdin:
            # Eliminar solo el salto de línea final para no afectar espacios internos
            linea_procesable = linea.rstrip('\n')
            resultado = procesar_linea(linea_procesable)
            sys.stdout.write(f"{resultado}\n")
    except EOFError:
        pass

if __name__ == "__main__":
    main()
