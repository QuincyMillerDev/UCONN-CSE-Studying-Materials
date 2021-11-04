from math import pi
from random import randrange

# Video Quiz Implementaion
def quick_sort(L, left = 0, right = None):
    if right is None: right = len(L)

    if right - left <= 1: return None

    # Partition around a pivot
    pivot = right - 1
    i, j = left, right - 2 # Or pivot - 1

    # Pivot
    while i < j:
        # Find first item bigger than pivot
        while L[i] < L[pivot]:
            i += 1

        while L[j] >= L[pivot] and i < j:
            j -= 1

        if i < j:
            L[i], L[j] = L[j], L[i]

    if L[i] >= L[pivot]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i

    quick_sort(L, left, pivot)
    quick_sort(L, pivot + 1, right)

# Book Implementation
def quicksort(L):
    _quicksort(L, 0, len(L))

def _quicksort(L, left, right):
    if right - left > 1:
        mid = partition(L, left, right)
        _quicksort(L, left, mid)
        _quicksort(L, mid+1, right)

def partition(L, left, right):
    pivot = randrange(left, right)
    L[pivot], L[right - 1] = L[right - 1], L[pivot]
    i, j, pivot = left, right - 2, right - 1
    while i < j:
        while L[i] < L[pivot]:
            i += 1
        while L[j] >= L[pivot]:
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    if L[i] >= L[pivot]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    return pivot