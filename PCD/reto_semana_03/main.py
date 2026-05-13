import sys
import math  

def main():
    productos = {}
    primera_linea = True

    for linea in sys.stdin:
        linea = linea.strip()
        if primera_linea:
            primera_linea = False
            continue
        if not linea:
            continue
        
        partes = linea.split(',')
        if len(partes) != 4:
            continue
            
        producto = partes[1].strip()
        
        try:
            cantidad = int(partes[2])
            precio_unitario = float(partes[3])
            
           
            if not math.isfinite(precio_unitario):
                continue
                
        except ValueError:
            continue 
           
        if producto not in productos:
            productos[producto] = {"unidades": 0, "ingreso": 0.0}
    
        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio_unitario

    reporte_final = []
    for prod, datos in productos.items():
        unidades = datos["unidades"]
        ingreso = datos["ingreso"]
        promedio = ingreso / unidades if unidades > 0 else 0
        
        reporte_final.append({
            "producto": prod,
            "unidades": unidades,
            "ingreso": ingreso,
            "promedio": promedio
        })
    

    reporte_ordenado = sorted(
        reporte_final, 
        key=lambda x: (-x["ingreso"], x["producto"])
    )
    

    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    for item in reporte_ordenado:
        print(f"{item['producto']},{item['unidades']},{item['ingreso']:.2f},{item['promedio']:.2f}")

if __name__ == "__main__":
    main()