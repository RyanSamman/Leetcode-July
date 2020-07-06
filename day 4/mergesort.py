import math

array = [12, 11, 13, 5, 6, 7, 8]


def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr) // 2

        L = arr[:m]
        R = arr[m:]

        mergeSort(L)
        mergeSort(R)

        print(L, R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                k += 1
                i += 1
            else:
                arr[k] = R[j]
                k += 1
                j += 1

        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1

        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1


mergeSort(array)
print(array)
#  print('~~~~~~~~~')
#  mergeSort2(0, len(array))
