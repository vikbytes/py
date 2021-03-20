import math

def partition(lst, start, end):
    mid = int(math.floor((start + end+1) / 2))
    print(mid)
    pivot = median_of_three(lst, start, mid, end)
    swap(lst[start], lst[pivot])
    j = pivot

    for i in range(start, end):
        if lst[i] <= lst[start]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return j

def median_of_three(lst, a, b, c):
    if lst[a] <= lst[b] <= lst[c] or lst[c] <= lst[b] <= lst[a]:
        return b
    elif lst[b] <= lst[a] <= lst[c] or lst[c] <= lst[a] <= lst[b]:
        return a
    elif lst[a] <= lst[c] <= lst[b] or lst[b] <= lst[c] <= lst[a]:
        return c

def swap(a, b):
    a, b = b, a

def quick_sort(lst, start, end):
    if start >= end:
        return

    j = partition(lst, start, end)
    quick_sort(lst, start, j - 1)
    quick_sort(lst, j + 1, end)

lst = [1, 3, 5, 1, 2, 7, 3, 3, 4, 9]
quick_sort(lst, 0, len(lst)-1)
print(lst)
