#include <stdio.h>
#include <limits.h>

int max(int a, int b, int c) {
    if (a >= b && a >= c) return a;
    if (b >= a && b >= c) return b;
    return c;
}

int max_cruce(int A[], int izq, int mid, int der) {
    int suma_izq = INT_MIN;
    int suma_actual = 0;
    for (int i = mid; i >= izq; i--) {
        suma_actual += A[i];
        if (suma_actual > suma_izq) suma_izq = suma_actual;
    }

    int suma_der = INT_MIN;
    suma_actual = 0;
    for (int i = mid + 1; i <= der; i++) {
        suma_actual += A[i];
        if (suma_actual > suma_der) suma_der = suma_actual;
    }
    return suma_izq + suma_der;
}

int max_subarray_sum(int A[], int izq, int der) {
    if (izq == der) return A[izq];

    int mid = (izq + der) / 2;

    return max(
        max_subarray_sum(A, izq, mid),
        max_subarray_sum(A, mid + 1, der),
        max_cruce(A, izq, mid, der)
    );
}

int main() {
    int A[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int n = sizeof(A) / sizeof(A[0]);
    printf("Resultado Caso 1: %d\n", max_subarray_sum(A, 0, n - 1));
    return 0;
}