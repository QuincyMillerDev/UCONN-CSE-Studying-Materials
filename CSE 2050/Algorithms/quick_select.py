# Video Quiz Implementation
def quick_select(L, left=0, right=None): # O(n) or # O(n^2) with bad pivot
    if right is None: right = len(L)

    pivot = right - 1
    i, j = left, pivot - 1

    while i<j:
        while L[i] < L[pivot]:
            i += 1
        while L[j] >= L[pivot] and i<j: 
            j-= 1

        if L[i] > L[j]: L[i], L[j] = L[j], L[i]

    if L[i] >= L[pivot]:
        L[i], L[pivot] = L[pivot], L[i]
        pivot = i

    if pivot == len(L) // 2: return L[pivot]
    elif pivot > len(L) // 2: return quick_select(L, left, pivot)
    elif pivot < len(L) // 2: return quick_select(L, pivot+1, right)

    