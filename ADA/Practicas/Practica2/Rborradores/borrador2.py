import json
import os

def clean_transactions(transactions):
    seen_ids = set()
    unique_transactions = []
    
    for i, record in enumerate(transactions):
        # Usamos .get() para evitar que el programa se cierre si falta la llave
        t_id = record.get('transaction_id')
        
        if t_id is None:
            # Si no encuentra 'transaction_id', nos avisa qué llaves sí existen
            print(f"⚠️ Aviso: El registro en la posición {i} no tiene 'transaction_id'.")
            print(f"   Llaves encontradas: {list(record.keys())}")
            continue # Salta este registro y sigue con el siguiente
            
        if t_id not in seen_ids:
            seen_ids.add(t_id)
            unique_transactions.append(record)
            
    return unique_transactions


try:
    base_dir = os.path.dirname(os.path.abspath(__file__)) 
    archivo = os.path.join(base_dir, 'transaction_data.json')

    with open(archivo, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    cleaned_data = clean_transactions(data)
    salida = os.path.join(base_dir, 'transaction_cleaned.json')
    
    with open(salida, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, indent=4, ensure_ascii=False)
    
    print(f"\n✅ Proceso completado.")
    print(f"Registros originales: {len(data)}")
    print(f"Registros únicos: {len(cleaned_data)}")

except Exception as e:
    print(f"❌ Error crítico: {e}")