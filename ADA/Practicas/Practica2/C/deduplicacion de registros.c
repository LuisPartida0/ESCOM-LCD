#include <stdio.h>
#include <stdlib.h>
#include "cJSON.h" /* Necesitarás descargar cJSON.h y cJSON.c */

void procesar_transacciones(const char *filename) {
    FILE *file;
    char *buffer;
    long length;
    cJSON *json_root, *item;
    int i, n;

    /* 1. Leer el archivo JSON */
    file = fopen(filename, "rb");
    fseek(file, 0, SEEK_END);
    length = ftell(file);
    fseek(file, 0, SEEK_SET);
    buffer = malloc(length + 1);
    fread(buffer, 1, length, file);
    fclose(file);
    buffer[length] = '\0';

    /* 2. Convertir a objeto JSON */
    json_root = cJSON_Parse(buffer);
    n = cJSON_GetArraySize(json_root);

    /* 3. Desplegar Lista Original */
    printf("=== LISTA ORIGINAL DE REGISTROS ===\n");
    for (i = 0; i < n; i++) {
        item = cJSON_GetArrayItem(json_root, i);
        printf("ID: %s, Amount: %d\n", 
               cJSON_GetObjectItem(item, "transaction_id")->valuestring,
               cJSON_GetObjectItem(item, "amount")->valueint);
    }

    /* 4. Lógica de Deduplicación (Manteniendo primera aparición) */
    printf("\n=== LISTA DE REGISTROS NO DUPLICADOS ===\n");
    /* Aquí llamarías a una función similar a is_duplicate que 
       vimos antes para filtrar mientras imprimes */
    
    /* ... (Lógica de filtrado) ... */

    free(buffer);
    cJSON_Delete(json_root);
}
