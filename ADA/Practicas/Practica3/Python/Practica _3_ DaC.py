import random

def max_cruce(A, izq, mid, der):
    # Suma hacia la izquierda desde el centro
    suma_izq = float('-inf')
    suma_actual = 0
    for i in range(mid, izq - 1, -1):
        suma_actual += A[i]
        if suma_actual > suma_izq:
            suma_izq = suma_actual
            
    # Suma hacia la derecha desde el centro
    suma_der = float('-inf')
    suma_actual = 0
    for i in range(mid + 1, der + 1):
        suma_actual += A[i]
        if suma_actual > suma_der:
            suma_der = suma_actual
            
    return suma_izq + suma_der

def max_subarray_sum(A, izq, der):
    if izq == der:
        return A[izq]
    
    mid = (izq + der) // 2
    
    return max(
        max_subarray_sum(A, izq, mid),
        max_subarray_sum(A, mid + 1, der),
        max_cruce(A, izq, mid, der)
    )

# Casos de Prueba Básicos
casos = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4], # C1: 6
    [-1, -2, -3, -4],               # C2: -1
    [5, 4, -1, 7, 8],               # C3: 23
    [1],                            # C4: 1
    [2, -1, 2, 3, 4, -1]            # C5: 10
]

for i, arr in enumerate(casos, 1):
    print(f"Caso {i}: {max_subarray_sum(arr, 0, len(arr)-1)}")

# Pruebas de Escalabilidad
for n in [10, 100, 1000, 10000]:
    test_large = [random.randint(-10000, 10000) for _ in range(n)]
    res = max_subarray_sum(test_large, 0, n-1)
    print(f"N={n:5} -> Resultado: {res}")