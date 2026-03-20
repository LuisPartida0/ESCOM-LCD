#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    char transaction_id[10];
    int amount;
} Transaction;

/* Función para verificar si el ID ya fue procesado */
int is_duplicate(char *id, Transaction *unique_list, int count) {
    int i;
    for (i = 0; i < count; i++) {
        if (strcmp(id, unique_list[i].transaction_id) == 0) return 1;
    }
    return 0;
}

int main() {
    Transaction input[] = {
        {"T1", 100}, {"T2", 200}, {"T1", 100}, {"T3", 300}, {"T2", 999}, {"T2", 999}, {"T2", 999}
    };
    int n = sizeof(input) / sizeof(input[0]);
    Transaction *unique_list = (Transaction*)malloc(n * sizeof(Transaction));
    int unique_count = 0;
    int i;

    for (i = 0; i < n; i++) {
        if (!is_duplicate(input[i].transaction_id, unique_list, unique_count)) {
            unique_list[unique_count] = input[i];
            unique_count++;
        }
    }

    printf("Lista Limpia:\n");
    for (i = 0; i < unique_count; i++) {
        printf("ID: %s, Amount: %d\n", unique_list[i].transaction_id, unique_list[i].amount);
    }

    free(unique_list);
    return 0;
}
