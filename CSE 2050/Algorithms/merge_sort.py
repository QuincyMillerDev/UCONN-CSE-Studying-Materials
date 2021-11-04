# Video Quiz Implementation

def merge_sort(L): # O(nlogn)
    # 1) Divide into subproblems
    # 2) Solve our subproblems
    # 3) Combine sub-solutions into main solution

    # Base Case: list with 1 or fewer items
    if len(L) <= 1: return L
    
    median = len(L) // 2
    left = L[:median]
    right = L[median:]

    left = merge_sort(left)
    right = merge_sort(right)

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[i+j] = left[i]
            i += 1
        else:
            L[i+j] = right[j]
            j += 1
    
    L[i+j:] = left[i:] + right[j:]
    return L

# Book Implementation

def mergesort(L):
    if len(L) < 2:
        return
    
    mid = len(L) // 2
    A = L[:mid]
    B = L[mid:]

    mergesort(A)
    mergesort(B)

    merge(A, B, L)

def merge(A, B, L):
    i = 0 # index into A
    j = 0 # index into B
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[i+j] = A[i]
            i = i + 1
        else:
            L[i+j] = B[j]
            j = j + 11
    # Add any remaining elements once one list is empty
    L[i+j:] = A[i:] + B[j:]