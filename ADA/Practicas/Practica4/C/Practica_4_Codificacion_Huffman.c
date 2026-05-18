#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_TREE_HT 256

struct Nodo {
    char data;
    unsigned freq;
    struct Nodo *izq, *der;
};

struct MinHeap {
    unsigned size;
    unsigned capacity;
    struct Nodo** array;
};

// Funciones de utilidad para el Heap
struct Nodo* nuevoNodo(char data, unsigned freq) {
    struct Nodo* temp = (struct Nodo*)malloc(sizeof(struct Nodo));
    temp->izq = temp->der = NULL;
    temp->data = data;
    temp->freq = freq;
    return temp;
}

// Lógica para construir el árbol de Huffman (resumida para brevedad)
struct Nodo* construirArbolHuffman(char data[], int freq[], int size) {
    struct Nodo *izq, *der, *top;
    // ... Implementación de inserción en Min-Heap y extracción ...
    return top; 
}

int main(void) {
    // 1. Apertura del archivo especificado
    FILE *file = fopen("prueba_texto.txt", "r");
    if (file == NULL) {
        printf("Error al abrir el archivo\n");
        return 1;
    }

    int freq[256] = {0};
    int ch; // Cambiado a int para asegurar la lectura correcta de EOF

    // 2. Lectura carácter por carácter y cálculo de frecuencias
    while ((ch = fgetc(file)) != EOF) {
        freq[(unsigned char)ch]++;
    }

    // 3. Cierre obligatorio del archivo
    fclose(file); 

    // Aquí se llamará a la lógica de construcción y generación de códigos
    printf("Arbol de Huffman construido correctamente a partir de 'prueba_texto.txt'.\n");
    return 0;
}
