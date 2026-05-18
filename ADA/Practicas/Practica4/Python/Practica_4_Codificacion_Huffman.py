import heapq
from collections import Counter

# -----------------------------
# Nodo del árbol de Huffman
# -----------------------------
class Nodo:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia


# -----------------------------
# Construcción del árbol
# -----------------------------
def construir_arbol(texto):
    frecuencias = Counter(texto)

    heap = []

    for caracter, frecuencia in frecuencias.items():
        heapq.heappush(heap, Nodo(caracter, frecuencia))

    while len(heap) > 1:
        izquierda = heapq.heappop(heap)
        derecha = heapq.heappop(heap)

        nuevo = Nodo(None, izquierda.frecuencia + derecha.frecuencia)
        nuevo.izquierda = izquierda
        nuevo.derecha = derecha

        heapq.heappush(heap, nuevo)

    return heap[0], frecuencias


# -----------------------------
# Generación de códigos
# -----------------------------
def generar_codigos(nodo, codigo_actual="", codigos={}):
    if nodo is None:
        return

    if nodo.caracter is not None:
        codigos[nodo.caracter] = codigo_actual

    generar_codigos(nodo.izquierda, codigo_actual + "0", codigos)
    generar_codigos(nodo.derecha, codigo_actual + "1", codigos)

    return codigos


# -----------------------------
# Codificación
# -----------------------------
def codificar(texto, codigos):
    return ''.join(codigos[c] for c in texto)


# -----------------------------
# Decodificación
# -----------------------------
def decodificar(bits, raiz):
    resultado = ""
    actual = raiz

    for bit in bits:
        if bit == '0':
            actual = actual.izquierda
        else:
            actual = actual.derecha

        if actual.caracter is not None:
            resultado += actual.caracter
            actual = raiz

    return resultado


# -----------------------------
# Programa principal
# -----------------------------
# Nombre fijo del archivo
ruta = r"D:\ESCOM\practica4\python\prueba_texto.txt"

with open(ruta, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

raiz, frecuencias = construir_arbol(texto)

print("\nFrecuencias:")
for c, f in frecuencias.items():
    print(f"'{c}': {f}")

codigos = generar_codigos(raiz)

print("\nCódigos Huffman:")
for c, codigo in codigos.items():
    print(f"'{c}': {codigo}")

texto_codificado = codificar(texto, codigos)

print("\nTexto codificado:")
print(texto_codificado)

texto_decodificado = decodificar(texto_codificado, raiz)

print("\nTexto decodificado:")
print(texto_decodificado)

if texto == texto_decodificado:
    print("\nVerificación EXITOSA: el texto coincide.")
else:
    print("\nError: los textos no coinciden.")