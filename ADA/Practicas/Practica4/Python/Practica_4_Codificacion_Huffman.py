import heapq
from collections import Counter

class NodoHuffman:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.izq = None
        self.der = None

    # Definir comparación para el min-heap
    def __lt__(self, otro):
        return self.freq < otro.freq

def construir_arbol(frecuencias):
    heap = [NodoHuffman(char, freq) for char, freq in frecuencias.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        nodo1 = heapq.heappop(heap)
        nodo2 = heapq.heappop(heap)
        fusion = NodoHuffman(None, nodo1.freq + nodo2.freq)
        fusion.izq = nodo1
        fusion.der = nodo2
        heapq.heappush(heap, fusion)
    return heap[0]

def generar_tabla(nodo, codigo_actual, tabla):
    if nodo is None:
        return
    if nodo.char is not None:
        tabla[nodo.char] = codigo_actual
    generar_tabla(nodo.izq, codigo_actual + "0", tabla)
    generar_tabla(nodo.der, codigo_actual + "1", tabla)

def huffman_workflow(ruta_archivo):
    # 1. Leer archivo
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        texto = f.read()

    # 2. Frecuencias
    frecuencias = Counter(texto)
    
    # 3. Árbol y 4. Tabla
    raiz = construir_arbol(frecuencias)
    tabla = {}
    generar_tabla(raiz, "", tabla)
    
    # 5. Codificar
    codificado = "".join(tabla[char] for char in texto)
    
    # 6. Decodificar para verificar
    decodificado = ""
    actual = raiz
    for bit in codificado:
        actual = actual.izq if bit == '0' else actual.der
        if actual.char:
            decodificado += actual.char
            actual = raiz

    print("\n--- RESULTADOS DEL PROCESAMIENTO ---")
    print(f"Texto Original (Muestra):\n{texto[:100]}...\n")
    print(f"Bits de salida (primeros 100):\n{codificado[:100]}\n")
    print(f"Verificación de integridad: {'EXITOSA (El texto coincide al 100%)' if decodificado == texto else 'FALLIDA'}")

# ==========================================
# SECCIÓN DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    # Contenido proporcionado para la prueba
    contenido = """Tres tristes tigres tragaban trigo en un trigal. 
El algoritmo de Huffman es un metodo de compresion de datos sin perdida.
Divide y venceras es un paradigma de diseño de algoritmos muy poderoso.
Estructuras de datos dinamicas como los min-heaps and los arboles binarios 
son fundamentales para la computacion moderna en este 2026."""

    # 1. Creación y escritura del archivo de texto
    with open("prueba_texto.txt", "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

    print("Archivo 'prueba_texto.txt' creado con exito.")

    # 2. Llamada automática al flujo de Huffman con el archivo recién creado
    huffman_workflow('prueba_texto.txt')