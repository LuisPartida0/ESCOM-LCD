from models.producto import Producto
from utils.validators import validar_producto
from utils.io import leer_inventario, escribir_reporte

def main():
    print("Iniciando Sistema de Inventario Modular...")
    datos_raw = leer_inventario("data/inventario.csv")
    productos_validos = []

    for item in datos_raw:
        v = item['datos']
        # Validar antes de instanciar (Regla de Robustez)
        es_valido, error = validar_producto(
            v[0] if len(v)>0 else "", v[1] if len(v)>1 else "", 
            v[3] if len(v)>3 else "", v[4] if len(v)>4 else "", 
            v[5] if len(v)>5 else "", len(v)
        )
        
        if es_valido:
            productos_validos.append(Producto(v[0], v[1], v[2], v[3], v[4], v[5]))
        else:
            print(f"Advertencia: Registro ignorado -> {error}")

    # Filtrar y Ordenar Descendente por faltantes
    reorden = [p for p in productos_validos if p.necesita_reorden()]
    reorden.sort(key=lambda x: x.unidades_faltantes(), reverse=True)

    escribir_reporte(reorden, "outputs/reporte_inventario.csv")
    print(f"Proceso completo. Reporte generado con {len(reorden)} productos.")

if __name__ == "__main__":
    main()