def bubble_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                a = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = a


def selection_sort(lst):
    for i in range(len(lst)-1):
        minpos=i
        for j in range(i, len(lst)):
            if lst[j] < lst[minpos]:
                minpos = j

        a = lst[i]
        lst[i] = lst[minpos]
        lst[minpos] = a

