# Video Quiz Version:
def insertion_sort(L): # O(n^2)
    n = len(L)
    for j in range(n):
        for i in range(n - 1 - j, n - 1):
            if L[i] > L[i + 1]:
                L[i], L[i+1] = L[i+1], L[i]
            else:
                break