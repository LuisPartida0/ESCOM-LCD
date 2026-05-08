import csv
import random
from datetime import datetime, timedelta

def generar_datasets():
    # 1. ventas.csv (fecha,producto,cantidad,precio,vendedor)
    productos = ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Audifonos']
    vendedores = ['Alice', 'Bob', 'Charlie', 'Diana']
    with open('data/ventas.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['fecha', 'producto', 'cantidad', 'precio', 'vendedor'])
        for i in range(160):
            fecha = (datetime(2026, 1, 1) + timedelta(days=random.randint(0, 200))).strftime('%Y-%m-%d')
            # Introducir algunos nulos aleatorios (5%)
            prod = random.choice(productos) if random.random() > 0.05 else ""
            writer.writerow([fecha, prod, random.randint(1, 10), round(random.uniform(200, 20000), 2), random.choice(vendedores)])

    # 2. empleados.csv (id,nombre,email,departamento,salario,activo)
    deps = ['RRHH', 'Sistemas', 'Ventas', 'Finanzas']
    with open('data/empleados.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'nombre', 'email', 'departamento', 'salario', 'activo'])
        for i in range(1, 161):
            nom = f"Empleado {i}"
            email = f"emp{i}@empresa.com"
            writer.writerow([i, nom, email, random.choice(deps), round(random.uniform(30000, 80000), 2), random.choice(['yes', 'no'])])

    # 3. sensores.csv (timestamp,sensor_id,temperatura,humedad,bateria)
    with open('data/sensores.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'sensor_id', 'temperatura', 'humedad', 'bateria'])
        for i in range(160):
            ts = (datetime(2026, 6, 1) + timedelta(minutes=i*15)).strftime('%Y-%m-%d %H:%M:%S')
            # Sensores suelen tener fallos (nulos)
            temp = round(random.uniform(15, 30), 2) if random.random() > 0.1 else ""
            hum = random.randint(30, 70) if random.random() > 0.1 else ""
            writer.writerow([ts, f"S{random.randint(1,5):03}", temp, hum, random.randint(0, 100)])

if __name__ == "__main__":
    generar_datasets()