
# Search Algorithm
# Implementasi Linear Search dan Binary Search

def linear_search(data, target):
    """
    Mencari data satu per satu dari awal.
    """
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data, target):
    """
    Mencari data dengan membagi area pencarian menjadi dua.
    Data harus sudah terurut.
    """
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
