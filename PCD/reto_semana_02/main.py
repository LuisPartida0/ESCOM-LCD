import sys

def fahrenheit_a_celsius(f):
    """Convierte Fahrenheit a Celsius usando la fórmula estándar."""
    return (f - 32) * 5 / 9

def clasificar_temperatura(celsius):
    """
    Clasifica el clima según los rangos establecidos:
    < 0: Congelante | 0-15: Frio | 16-25: Templado | 26-35: Calido | > 35: Extremo
    """
    if celsius < 0:
        return "Congelante"
    elif celsius <= 15:
        return "Frio"
    elif celsius <= 25:
        return "Templado"
    elif celsius <= 35:
        return "Calido"
    else:
        return "Extremo"

def main():
    """Punto de entrada principal para el procesamiento del CSV."""
    primera_linea = True
    
    # Imprimir encabezado de salida (Regla de Formato)
    print("ciudad,temperatura_celsius,clasificacion")
    
    for linea in sys.stdin:
        linea = linea.strip()
        
        # Saltar el encabezado de entrada
        if primera_linea:
            primera_linea = False
            continue
            
        # Ignorar líneas vacías
        if not linea:
            continue
            
        # Separar campos y validar estructura (Regla 3)
        partes = linea.split(',')
        if len(partes) != 3:
            continue
            
        ciudad = partes[0].strip()
        temp_str = partes[1].strip()
        unidad = partes[2].strip().upper()
        
        # Validar Unidad y Temperatura
        if unidad not in ['C', 'F']:
            continue
            
        try:
            temp_valor = float(temp_str)
        except ValueError:
            continue
            
        # Transformación: Unificar a Celsius (Regla 1)
        if unidad == 'F':
            celsius = fahrenheit_a_celsius(temp_valor)
        else:
            celsius = temp_valor
            
        # Clasificación (Regla 2)
        categoria = clasificar_temperatura(celsius)
        
        # Salida Estándar con 1 decimal (Regla 4)
        print(f"{ciudad},{celsius:.1f},{categoria}")

if __name__ == "__main__":
    main()