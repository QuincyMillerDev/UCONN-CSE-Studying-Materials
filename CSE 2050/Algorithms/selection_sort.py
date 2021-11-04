# Video Quiz implementation

def selection_sort(L): # O(n^2)
    # Find the next biggest item
    # Swap that item to the correct spot
    
    for j in range(len(L) - 1):
        biggest_index = 0
        for i in range(1, len(L) - j):
            if L[i] > L[biggest_index]:
                biggest_index = i
    
    L[biggest_index], L[len(L) - 1] = L[len(L) - 1], L[biggest_index]