import sys

def main():
    # Diccionario para agrupar: { "Producto": {"unidades": 0, "ingreso": 0.0} }
    productos = {}
    
    primera_linea = True
    
    # Lectura desde stdin (ETL: Extract)
    for linea in sys.stdin:
        linea = linea.strip()
        
        # Saltar encabezado de entrada (Regla 5)
        if primera_linea:
            primera_linea = False
            continue
        
        if not linea:
            continue
        
        # Parsear y validar (Regla 5)
        partes = linea.split(',')
        if len(partes) != 4:
            continue
            
        producto = partes[1].strip()
        
        try:
            cantidad = int(partes[2])
            precio_unitario = float(partes[3])
        except ValueError:
            continue # Ignorar si cantidad o precio no son numéricos
            
        # Agrupamiento (Regla 1)
        if producto not in productos:
            productos[producto] = {
                "unidades": 0,
                "ingreso": 0.0
            }
        
        # Acumulación de métricas (Regla 2)
        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio_unitario
    
    # Cálculo de métricas finales y preparación para ordenar
    reporte_final = []
    for prod, datos in productos.items():
        unidades = datos["unidades"]
        ingreso = datos["ingreso"]
        
        # Calcular promedio (evitar división por cero)
        promedio = ingreso / unidades if unidades > 0 else 0
        
        reporte_final.append({
            "producto": prod,
            "unidades": unidades,
            "ingreso": ingreso,
            "promedio": promedio
        })
    
    # Ordenar por ingreso total descendente (Regla 3)
    reporte_ordenado = sorted(
        reporte_final, 
        key=lambda x: x["ingreso"], 
        reverse=True
    )
    
    # Salida estándar CSV (Regla 4 y Especificación de Salida)
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    for item in reporte_ordenado:
        print(f"{item['producto']},{item['unidades']},{item['ingreso']:.2f},{item['promedio']:.2f}")

if __name__ == "__main__":
    main()