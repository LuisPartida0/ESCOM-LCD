import os
import csv

def perfilar_archivo(ruta_entrada, ruta_salida):
    """Analiza un CSV y genera un reporte de calidad en formato de texto."""
    try:
        with open(ruta_entrada, 'r', encoding='utf-8') as f:
            # Usar Sniffer para detectar el dialecto (comas, puntos y comas, etc.)
            dialecto = csv.Sniffer().sniff(f.read(2048))
            f.seek(0)
            lector = csv.reader(f, dialecto)
            
            encabezados = next(lector)
            filas = list(lector)
            
        num_columnas = len(encabezados)
        num_filas = len(filas)
        
        # Contadores de nulos
        nulos_por_columna = [0] * num_columnas
        # Para detectar duplicados (usamos tuplas ya que son hashables)
        registros_unicos = set()
        duplicados = 0
        
        for fila in filas:
            # Validar integridad de la fila
            if len(fila) != num_columnas:
                continue
                
            # Contar nulos
            for i in range(num_columnas):
                if not fila[i].strip():
                    nulos_por_columna[i] += 1
            
            # Contar duplicados
            registro = tuple(fila)
            if registro in registros_unicos:
                duplicados += 1
            else:
                registros_unicos.add(registro)

        # Escribir el reporte de salida
        with open(ruta_salida, 'w', encoding='utf-8') as f_out:
            f_out.write(f"REPORTE DE PERFILAMIENTO: {os.path.basename(ruta_entrada)}\n")
            f_out.write("=" * 50 + "\n")
            f_out.write(f"Total de Registros: {num_filas}\n")
            f_out.write(f"Total de Columnas: {num_columnas}\n")
            f_out.write(f"Registros Duplicados: {duplicados}\n\n")
            f_out.write(f"{'Columna':<20} | {'Nulos':<10}\n")
            f_out.write("-" * 35 + "\n")
            
            for i in range(num_columnas):
                f_out.write(f"{encabezados[i]:<20} | {nulos_por_columna[i]:<10}\n")
                
        return True
    except Exception as e:
        print(f"Error procesando {ruta_entrada}: {e}")
        return False

def main():
    directorio_data = "data"
    directorio_out = "outputs"
    
    # Crear carpeta de salida si no existe
    if not os.path.exists(directorio_out):
        os.makedirs(directorio_out)
        
    print("Iniciando perfilador automático...")
    
    archivos = [f for f in os.listdir(directorio_data) if f.endswith('.csv')]
    
    if not archivos:
        print("No se encontraron archivos CSV en la carpeta /data")
        return

    for archivo in archivos:
        entrada = os.path.join(directorio_data, archivo)
        salida = os.path.join(directorio_out, f"perfil_{archivo.replace('.csv', '.txt')}")
        
        if perfilar_archivo(entrada, salida):
            print(f"✅ Reporte generado: {salida}")

if __name__ == "__main__":
    main()