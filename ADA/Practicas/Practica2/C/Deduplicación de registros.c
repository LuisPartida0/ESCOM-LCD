#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cJSON.h" /* Librería necesaria para procesar JSON */

/* Estructura para almacenar IDs únicos temporalmente */
typedef struct {
    char id[20];
} SeenID;

int main() {
    FILE *file;
    char *buffer;
    long length;
    cJSON *json_root, *item;
    int i, j, n, is_dup;
    
    /* Arreglo para rastrear IDs ya procesados */
    SeenID *seen_list;
    int seen_count = 0;

    /* 1. Cargar el archivo .json */
    file = fopen("transaction.json", "rb");
    if (!file) return 1;
    fseek(file, 0, SEEK_END);
    length = ftell(file);
    fseek(file, 0, SEEK_SET);
    buffer = malloc(length + 1);
    fread(buffer, 1, length, file);
    fclose(file);
    buffer[length] = '\0';

    /* 2. Parsear el contenido JSON */
    json_root = cJSON_Parse(buffer);
    n = cJSON_GetArraySize(json_root);
    seen_list = (SeenID*)malloc(n * sizeof(SeenID));

    /* 3. DESPLEGAR LISTA ORIGINAL */
    printf("=== LISTA ORIGINAL DE REGISTROS ===\n");
    for (i = 0; i < n; i++) {
        item = cJSON_GetArrayItem(json_root, i);
        printf("ID: %-5s | Amount: %d\n", 
               cJSON_GetObjectItem(item, "transaction_id")->valuestring,
               cJSON_GetObjectItem(item, "amount")->valueint);
    }

    /* 4. FILTRAR Y DESPLEGAR LISTA SIN DUPLICADOS */
    printf("\n=== LISTA SIN DUPLICADOS (Primera Aparicion) ===\n");
    for (i = 0; i < n; i++) {
        item = cJSON_GetArrayItem(json_root, i);
        char *current_id = cJSON_GetObjectItem(item, "transaction_id")->valuestring;
        int current_amount = cJSON_GetObjectItem(item, "amount")->valueint;

        /* Comprobar si el ID ya fue visto */
        is_dup = 0;
        for (j = 0; j < seen_count; j++) {
            if (strcmp(current_id, seen_list[j].id) == 0) {
                is_dup = 1;
                break;
            }
        }

        /* Si no es duplicado, lo mostramos y lo agregamos a 'vistos' */
        if (!is_dup) {
            printf("ID: %-5s | Amount: %d\n", current_id, current_amount);
            strcpy(seen_list[seen_count].id, current_id);
            seen_count++;
        }
    }

    /* Limpieza de memoria */
    free(buffer);
    free(seen_list);
    cJSON_Delete(json_root);
    return 0;
}
