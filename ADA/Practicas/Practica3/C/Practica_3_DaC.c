#include <stdio.h>
#include <limits.h>

/* Usamos inline para optimizar el rendimiento en C99, 
   evitando la sobrecarga de la llamada a la funcion */
static inline int max(int a, int b, int c) {
    int m = a;
    if (b > m) m = b;
    if (c > m) m = c;
    return m;
}

/* Funcion auxiliar: Calcula la suma maxima que cruza el punto medio */
int max_cruce(const int *__restrict A, int izq, int mid, int der)
 {
    int suma_izq = INT_MIN;
    int suma_der = INT_MIN;
    int suma_actual = 0;
    int i; /* Declaracion fuera del for para compatibilidad estricta */

    /* Parte izquierda del cruce */
    for (i = mid; i >= izq; i--) {
        suma_actual += A[i];
        if (suma_actual > suma_izq) {
            suma_izq = suma_actual;
        }
    }

    /* Parte derecha del cruce */
    suma_actual = 0;
    for (i = mid + 1; i <= der; i++) {
        suma_actual += A[i];
        if (suma_actual > suma_der) {
            suma_der = suma_actual;
        }
    }

    return suma_izq + suma_der;
}

/* Funcion principal recursiva Divide y Venceras */
int max_subarray_sum(const int *__restrict A, int izq, int der) {
    int mid;
    int izq_max, der_max, cruce_max;

    /* Caso base: solo un elemento */
    if (izq == der) {
        return A[izq];
    }

    mid = (izq + der) / 2;

    /* Llamadas recursivas (Sin ciclos en la parte principal) */
    izq_max = max_subarray_sum(A, izq, mid);
    der_max = max_subarray_sum(A, mid + 1, der);
    cruce_max = max_cruce(A, izq, mid, der);

    return max(izq_max, der_max, cruce_max);
}

int main(void) {
    int A[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int n = sizeof(A) / sizeof(A[0]);

    printf("Resultado Caso 1: %d\n", max_subarray_sum(A, 0, n - 1));

    return 0;
}
