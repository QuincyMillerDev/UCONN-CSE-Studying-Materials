# Video Quiz Implementation
def is_sorted(L):
    for i in range(len(L) - 1):
        if L[i] > L[i+1]: return False
    return True

def bubble_sort(L): # O(n^2)
    for j in range(len(L) - 1):
        for i in range(len(L) - 1 - j):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]

# Book implementation: Includes a flag to terminate the algorithm early if the list is already sorted
def bubblesort(L):
    keepgoing = True
    while keepgoing:
        keepgoing = False
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                keepgoing = True
        


if __name__ == "__main__":
    import random
    L = [random.randint(0, 10) for i in range(1000)]
    L.append(-1)

    assert(not is_sorted(L))
    bubble_sort(L)
    assert(is_sorted(L))