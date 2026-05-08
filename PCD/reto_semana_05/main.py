import argparse
import csv
import os
from datetime import datetime

def inferir_tipo(valor):
    if not valor: return None
    # Booleano
    if valor.lower() in ['true', 'false', 'yes', 'no', '1', '0']:
        return "booleano"
    # Fecha
    for formato in ['%Y-%m-%d', '%Y-%m-%d %H:%M:%S']:
        try:
            datetime.strptime(valor, formato)
            return "fecha"
        except ValueError: continue
    # Numerico
    try:
        float(valor)
        return "numerico"
    except ValueError:
        return "texto"

def perfilar(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        reader = list(csv.reader(f))
        if not reader: return
        headers = reader[0]
        filas = reader[1:]
        total_filas = len(filas)

    perfil_data = []
    for i, col_name in enumerate(headers):
        valores = [fila[i] for fila in filas if i < len(fila)]
        valores_no_nulos = [v for v in valores if v.strip()]
        
        # Tipo Inferido (basado en el primer valor no nulo)
        ejemplo = valores_no_nulos[0] if valores_no_nulos else ""
        tipo = inferir_tipo(ejemplo) if ejemplo else "texto"
        
        # Métricas
        nulos = total_filas - len(valores_no_nulos)
        unicos = len(set(valores_no_nulos))
        
        perfil_data.append({
            "nombre_columna": col_name,
            "tipo_inferido": tipo,
            "total_registros": total_filas,
            "valores_nulos": nulos,
            "porcentaje_nulos": round((nulos / total_filas) * 100, 2),
            "valores_unicos": unicos,
            "porcentaje_unicos": round((unicos / total_filas) * 100, 2),
            "ejemplo_valor": ejemplo
        })

    # Escritura del Perfil
    output_headers = ["nombre_columna", "tipo_inferido", "total_registros", "valores_nulos", 
                      "porcentaje_nulos", "valores_unicos", "porcentaje_unicos", "ejemplo_valor"]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=output_headers)
        writer.writeheader()
        writer.writerows(perfil_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perfilador de Datasets CSV")
    parser.add_argument("--input", "-i", required=True, help="Ruta al CSV de entrada")
    parser.add_argument("--output", "-o", required=True, help="Ruta al CSV de salida")
    args = parser.parse_args()
    
    perfilar(args.input, args.output)
    print(f"Perfil generado exitosamente en: {args.output}")