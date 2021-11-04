# Book Implementation of Binary Search
def bs(L, item):
    left, right = 0, len(L)
    while right - left > 1:
        median = (right + left) // 2
        if item < L[median]:
            right = median
        else:
            left = median
    return right > left and L[left] == item

# Video Quiz Prof Jake Implementation
def bs2(L, item, left = 0, right = None): # O(logn)
    if right is None: right = len(L) - 1

    median = (left + right) // 2

    if L[median] == item: return True

    if (right - left) <= 1: return L[right] == item

    if item < L[median]: return bs(L, item, left, median)
    elif item > L[median]: return bs(L, item, median, right)