import json


def clean_transactions(data):
    """Remove duplicate transactions based on all fields."""
    seen = set()
    cleaned = []
    for transaction in data:
        transaction_tuple = tuple(sorted(transaction.items()))
        if transaction_tuple not in seen:
            seen.add(transaction_tuple)
            cleaned.append(transaction)
    return cleaned


try:
    with open('transaction_data.json', 'r') as f:
        data = json.load(f)
    
    print(f"Cargando {len(data)} registros...")
    cleaned_data = clean_transactions(data)
    
    print(f"\n✅ Proceso completado.")
    print(f"Registros originales: {len(data)}")
    print(f"Registros únicos: {len(cleaned_data)}")
    
    with open('transaction_cleaned.json', 'w') as f:
        json.dump(cleaned_data, f, indent=4)

except Exception as e:
    print(f"❌ Error crítico: {e}")