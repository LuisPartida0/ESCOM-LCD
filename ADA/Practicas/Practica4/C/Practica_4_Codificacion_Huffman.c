#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CHAR 256
#define MAX_TEXT 10000

// ======================================
// ESTRUCTURA DEL NODO HUFFMAN
// ======================================

typedef struct Nodo {
    char caracter;
    int frecuencia;
    struct Nodo *izq;
    struct Nodo *der;
} Nodo;

// ======================================
// ESTRUCTURA DEL MIN HEAP
// ======================================

typedef struct {
    int size;
    Nodo* data[MAX_CHAR];
} MinHeap;

// ======================================
// CREAR NODO
// ======================================

Nodo* crearNodo(char caracter, int frecuencia) {

    Nodo* nuevo = (Nodo*) malloc(sizeof(Nodo));

    nuevo->caracter = caracter;
    nuevo->frecuencia = frecuencia;
    nuevo->izq = NULL;
    nuevo->der = NULL;

    return nuevo;
}

// ======================================
// INTERCAMBIAR NODOS
// ======================================

void swap(Nodo** a, Nodo** b) {

    Nodo* temp = *a;
    *a = *b;
    *b = temp;
}

// ======================================
// HEAPIFY
// ======================================

void heapify(MinHeap* heap, int i) {

    int menor = i;
    int izquierda = 2 * i + 1;
    int derecha = 2 * i + 2;

    if (izquierda < heap->size &&
        heap->data[izquierda]->frecuencia <
        heap->data[menor]->frecuencia) {

        menor = izquierda;
    }

    if (derecha < heap->size &&
        heap->data[derecha]->frecuencia <
        heap->data[menor]->frecuencia) {

        menor = derecha;
    }

    if (menor != i) {

        swap(&heap->data[i], &heap->data[menor]);

        heapify(heap, menor);
    }
}

// ======================================
// INSERTAR EN HEAP
// ======================================

void insertarHeap(MinHeap* heap, Nodo* nodo) {

    int i = heap->size;

    heap->size++;

    while (i > 0 &&
           nodo->frecuencia <
           heap->data[(i - 1) / 2]->frecuencia) {

        heap->data[i] = heap->data[(i - 1) / 2];

        i = (i - 1) / 2;
    }

    heap->data[i] = nodo;
}

// ======================================
// EXTRAER MINIMO
// ======================================

Nodo* extraerMin(MinHeap* heap) {

    Nodo* minimo = heap->data[0];

    heap->data[0] = heap->data[heap->size - 1];

    heap->size--;

    heapify(heap, 0);

    return minimo;
}

// ======================================
// CONSTRUIR ARBOL HUFFMAN
// ======================================

Nodo* construirHuffman(int frecuencias[]) {

    MinHeap heap;

    heap.size = 0;

    // Insertar caracteres con frecuencia
    for (int i = 0; i < MAX_CHAR; i++) {

        if (frecuencias[i] > 0) {

            insertarHeap(
                &heap,
                crearNodo((char)i, frecuencias[i])
            );
        }
    }

    // Caso especial: solo un caracter
    if (heap.size == 1) {

        Nodo* unico = extraerMin(&heap);

        Nodo* raiz = crearNodo('\0', unico->frecuencia);

        raiz->izq = unico;

        return raiz;
    }

    // Construccion del arbol
    while (heap.size > 1) {

        Nodo* izquierda = extraerMin(&heap);
        Nodo* derecha = extraerMin(&heap);

        Nodo* nuevo = crearNodo(
            '\0',
            izquierda->frecuencia + derecha->frecuencia
        );

        nuevo->izq = izquierda;
        nuevo->der = derecha;

        insertarHeap(&heap, nuevo);
    }

    return extraerMin(&heap);
}

// ======================================
// DUPLICAR CADENA (C99)
// ======================================

char* duplicarCadena(const char* str) {

    char* copia = (char*) malloc(strlen(str) + 1);

    if (copia != NULL) {
        strcpy(copia, str);
    }

    return copia;
}

// ======================================
// GENERAR CODIGOS
// ======================================

void generarCodigos(
    Nodo* raiz,
    char codigo[],
    int top,
    char* tabla[]
) {

    if (raiz->izq != NULL) {

        codigo[top] = '0';

        generarCodigos(
            raiz->izq,
            codigo,
            top + 1,
            tabla
        );
    }

    if (raiz->der != NULL) {

        codigo[top] = '1';

        generarCodigos(
            raiz->der,
            codigo,
            top + 1,
            tabla
        );
    }

    // Nodo hoja
    if (raiz->izq == NULL &&
        raiz->der == NULL) {

        codigo[top] = '\0';

        tabla[(unsigned char)raiz->caracter] =
            duplicarCadena(codigo);

        if (raiz->caracter == '\n') {
            printf("'\\n' : %s\n", codigo);
        }
        else if (raiz->caracter == ' ') {
            printf("'ESPACIO' : %s\n", codigo);
        }
        else {
            printf("'%c' : %s\n",
                   raiz->caracter,
                   codigo);
        }
    }
}

// ======================================
// CODIFICAR TEXTO
// ======================================

void codificarTexto(
    char texto[],
    char* tabla[],
    char salida[]
) {

    salida[0] = '\0';

    for (int i = 0; texto[i] != '\0'; i++) {

        strcat(
            salida,
            tabla[(unsigned char)texto[i]]
        );
    }
}

// ======================================
// DECODIFICAR TEXTO
// ======================================

void decodificarTexto(
    char bits[],
    Nodo* raiz,
    char resultado[]
) {

    int indice = 0;

    Nodo* actual = raiz;

    for (int i = 0; bits[i] != '\0'; i++) {

        if (bits[i] == '0') {
            actual = actual->izq;
        }
        else {
            actual = actual->der;
        }

        // Nodo hoja
        if (actual->izq == NULL &&
            actual->der == NULL) {

            resultado[indice++] =
                actual->caracter;

            actual = raiz;
        }
    }

    resultado[indice] = '\0';
}

// ======================================
// LEER ARCHIVO
// ======================================

void leerArchivo(
    const char* ruta,
    char texto[]
) {

    FILE* archivo = fopen(ruta, "r");

    if (archivo == NULL) {

        printf("Error al abrir el archivo.\n");

        exit(1);
    }

    int i = 0;
    char c;

    while ((c = fgetc(archivo)) != EOF &&
           i < MAX_TEXT - 1) {

        texto[i++] = c;
    }

    texto[i] = '\0';

    fclose(archivo);
}

// ======================================
// LIBERAR MEMORIA
// ======================================

void liberarArbol(Nodo* raiz) {

    if (raiz == NULL) {
        return;
    }

    liberarArbol(raiz->izq);
    liberarArbol(raiz->der);

    free(raiz);
}

// ======================================
// MAIN
// ======================================

int main() {

    char ruta[200];

    char texto[MAX_TEXT];

    char textoCodificado[MAX_TEXT * 20];

    char textoDecodificado[MAX_TEXT];

    int frecuencias[MAX_CHAR] = {0};

    char* tablaCodigos[MAX_CHAR] = {0};

    char codigoTemporal[MAX_CHAR];

    // ==================================
    // INGRESAR RUTA
    // ==================================

    printf("Ingrese la ruta del archivo: ");

    scanf("%199s", ruta);

    // ==================================
    // LEER ARCHIVO
    // ==================================

    leerArchivo(ruta, texto);

    printf("\nTexto original:\n%s\n", texto);

    // ==================================
    // CALCULAR FRECUENCIAS
    // ==================================

    for (int i = 0; texto[i] != '\0'; i++) {

        frecuencias[
            (unsigned char) texto[i]
        ]++;
    }

    printf("\nFrecuencias:\n");

    for (int i = 0; i < MAX_CHAR; i++) {

        if (frecuencias[i] > 0) {

            if (i == '\n') {
                printf("'\\n' : %d\n",
                       frecuencias[i]);
            }
            else if (i == ' ') {
                printf("'ESPACIO' : %d\n",
                       frecuencias[i]);
            }
            else {
                printf("'%c' : %d\n",
                       i,
                       frecuencias[i]);
            }
        }
    }

    // ==================================
    // CONSTRUIR ARBOL
    // ==================================

    Nodo* raiz =
        construirHuffman(frecuencias);

    // ==================================
    // GENERAR CODIGOS
    // ==================================

    printf("\nCodigos Huffman:\n");

    generarCodigos(
        raiz,
        codigoTemporal,
        0,
        tablaCodigos
    );

    // ==================================
    // CODIFICAR
    // ==================================

    codificarTexto(
        texto,
        tablaCodigos,
        textoCodificado
    );

    printf("\nTexto codificado:\n");

    printf("%s\n", textoCodificado);

    // ==================================
    // DECODIFICAR
    // ==================================

    decodificarTexto(
        textoCodificado,
        raiz,
        textoDecodificado
    );

    printf("\nTexto decodificado:\n");

    printf("%s\n", textoDecodificado);

    // ==================================
    // VERIFICACION
    // ==================================

    if (strcmp(texto, textoDecodificado) == 0) {

        printf("\nVERIFICACION EXITOSA:\n");
        printf("El texto coincide.\n");
    }
    else {

        printf("\nERROR:\n");
        printf("El texto NO coincide.\n");
    }

    // ==================================
    // LIBERAR MEMORIA
    // ==================================

    for (int i = 0; i < MAX_CHAR; i++) {

        if (tablaCodigos[i] != NULL) {

            free(tablaCodigos[i]);
        }
    }

    liberarArbol(raiz);

    return 0;
}
