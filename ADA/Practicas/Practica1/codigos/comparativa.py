import time
import random
import math
import sys

# --- Algoritmos de Ordenamiento ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        merge_sort(L); merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]: arr[k] = L[i]; i += 1
            else: arr[k] = R[j]; j += 1
            k += 1
        while i < len(L): arr[k] = L[i]; i += 1; k += 1
        while j < len(R): arr[k] = R[j]; j += 1; k += 1

# --- Algoritmos de Busqueda ---
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x: return i
    return -1

def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x: return m
        elif arr[m] < x: l = m + 1
        else: r = m - 1
    return -1

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n)-1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n: return -1
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n): return -1
    return prev if arr[prev] == x else -1

# --- Ejecucion de Pruebas ---
sizes = [10, 100, 1000, 10000, 100000]

print(f"{'N':<10} | {'Quick':<12} | {'Merge':<12} | {'Bubble':<12} | {'Memoria (MB)':<12}")
print("-" * 65)

for n in sizes:
    data = [random.randint(-10000, 10000) for _ in range(n)]
    mem_mb = sys.getsizeof(data) / (1024 * 1024)
    
    # Test QuickSort
    start = time.time()
    _ = quick_sort(data.copy())
    t_quick = time.time() - start
    
    # Test MergeSort
    start = time.time()
    temp_data = data.copy()
    merge_sort(temp_data)
    t_merge = time.time() - start
    
    # Test BubbleSort (Solo si N <= 5000)
    t_bubble = "N/A"
    if n <= 5000:
        start = time.time()
        bubble_sort(data.copy())
        t_bubble = f"{time.time() - start:.6f}s"
    
    print(f"{n:<10} | {t_quick:.6f}s | {t_merge:.6f}s | {t_bubble:<12} | {mem_mb:.4f}")