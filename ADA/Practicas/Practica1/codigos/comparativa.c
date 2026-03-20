#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

/* --- PROTOTIPOS DE FUNCIONES  */
void initialize_data(int arr[], int n);
void print_data(int arr[], int n);
void copy_data(int source[], int dest[], int n);

/* Ordenamientos */
void bubble_sort(int arr[], int n);
void quick_sort(int arr[], int low, int high);
void merge_sort(int arr[], int l, int r);
void merge(int arr[], int l, int m, int r);

/* Busquedas */
int linear_search(int arr[], int n, int x);
int binary_search(int arr[], int n, int x);
int jump_search(int arr[], int n, int x);

int main(void) {
    int n, option, target;
    int *master_arr, *work_arr;
    clock_t start, end;
    double sort_time;

    srand((unsigned int)time(NULL));

    printf("=== LABORATORIO DE ALGORITMOS OPTIMIZADOS ===\n");
    printf("Ingrese el numero de elementos (N): ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Error: Ingrese un numero entero positivo.\n");
        return 1;
    }

    /* Asignacion dinamica para manejar N hasta 1,000,000 */
    master_arr = (int*)malloc(n * sizeof(int));
    work_arr = (int*)malloc(n * sizeof(int));

    if (master_arr == NULL || work_arr == NULL) {
        printf("Error: Memoria insuficiente.\n");
        return 1;
    }

    initialize_data(master_arr, n);

    do {
        printf("\n--- MENU DE ORDENAMIENTO ---\n");
        printf("1. Bubble Sort (Optimizado)\n");
        printf("2. Quick Sort\n");
        printf("3. Merge Sort\n");
        printf("0. Salir\n");
        printf("Opcion: ");
        scanf("%d", &option);

        if (option >= 1 && option <= 3) {
            copy_data(master_arr, work_arr, n);

            if (n < 50) {
                printf("\nDatos desordenados:\n");
                print_data(work_arr, n);
            }

            /* --- EJECUCION Y TIEMPO DE ORDENAMIENTO --- */
            start = clock();
            switch (option) {
                case 1: bubble_sort(work_arr, n); break;
                case 2: quick_sort(work_arr, 0, n - 1); break;
                case 3: merge_sort(work_arr, 0, n - 1); break;
            }
            end = clock();
            sort_time = ((double)(end - start)) / CLOCKS_PER_SEC;

            if (n < 50) {
                printf("Datos ordenados:\n");
                print_data(work_arr, n);
            }
            printf("\n>> Tiempo de ordenamiento: %.6f segundos.\n", sort_time);

            /* --- EJECUCION DE BUSQUEDAS --- */
            /* Buscamos el elemento central para asegurar que el algoritmo trabaje */
            target = work_arr[n / 2]; 
            printf("\n--- COMPARATIVA DE BUSQUEDAS (Valor buscado: %d) ---\n", target);

            /* Lineal */
            start = clock(); linear_search(work_arr, n, target); end = clock();
            printf("Linear Search: %.8f s\n", (double)(end - start) / CLOCKS_PER_SEC);

            /* Binaria */
            start = clock(); binary_search(work_arr, n, target); end = clock();
            printf("Binary Search: %.8f s\n", (double)(end - start) / CLOCKS_PER_SEC);

            /* Saltos */
            start = clock(); jump_search(work_arr, n, target); end = clock();
            printf("Jump Search:   %.8f s\n", (double)(end - start) / CLOCKS_PER_SEC);
            printf("----------------------------------------------------------\n");
        }

    } while (option != 0);

    free(master_arr);
    free(work_arr);
    return 0;
}

/* --- IMPLEMENTACIONES AUXILIARES --- */

void initialize_data(int arr[], int n) {
    int i;
    for (i = 0; i < n; i++) {
        arr[i] = rand() % 20001 - 10000;
    }
}

void print_data(int arr[], int n) {
    int i;
    for (i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
}

void copy_data(int source[], int dest[], int n) {
    int i;
    for (i = 0; i < n; i++) dest[i] = source[i];
}

/* --- ALGORITMOS DE ORDENAMIENTO --- */


void bubble_sort(int arr[], int n) {
    int i, j, temp, swapped;
    for (i = 0; i < n - 1; i++) {
        swapped = 0;
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j]; arr[j] = arr[j + 1]; arr[j + 1] = temp;
                swapped = 1;
            }
        }
        if (swapped == 0) break;
    }
}


void quick_sort(int arr[], int low, int high) {
    int i, j, pivot, temp;
    if (low < high) {
        pivot = arr[high];
        i = low - 1;
        for (j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
            }
        }
        temp = arr[i + 1]; arr[i + 1] = arr[high]; arr[high] = temp;
        quick_sort(arr, low, i);
        quick_sort(arr, i + 2, high);
    }
}


void merge(int arr[], int l, int m, int r) {
    int i, j, k, n1 = m - l + 1, n2 = r - m;
    int *L, *R;
    L = (int*)malloc(n1 * sizeof(int));
    R = (int*)malloc(n2 * sizeof(int));
    for (i = 0; i < n1; i++) L[i] = arr[l + i];
    for (j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
    i = 0; j = 0; k = l;
    while (i < n1 && j < n2) arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
    free(L); free(R);
}

void merge_sort(int arr[], int l, int r) {
    int m;
    if (l < r) {
        m = l + (r - l) / 2;
        merge_sort(arr, l, m);
        merge_sort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

/* --- ALGORITMOS DE BUSQUEDA --- */


int linear_search(int arr[], int n, int x) {
    int i;
    for (i = 0; i < n; i++) if (arr[i] == x) return i;
    return -1;
}

int binary_search(int arr[], int n, int x) {
    int l = 0, r = n - 1, m;
    while (l <= r) {
        m = l + (r - l) / 2;
        if (arr[m] == x) return m;
        if (arr[m] < x) l = m + 1; else r = m - 1;
    }
    return -1;
}

int jump_search(int arr[], int n, int x) {
    int step = (int)sqrt(n), prev = 0, limit;
    while (arr[(step < n ? step : n) - 1] < x) {
        prev = step;
        step += (int)sqrt(n);
        if (prev >= n) return -1;
    }
    limit = (step < n ? step : n);
    while (arr[prev] < x) {
        prev++;
        if (prev == limit) return -1;
    }
    return (arr[prev] == x) ? prev : -1;
}
