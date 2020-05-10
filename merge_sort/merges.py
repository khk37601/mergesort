""" merge sort algorithm

O(n log n)


Usage:

array = []            # creates an empty list
merge_sort(iterables, version=None) # selected merge sort method
merge(iterables)     # split the array
_sort(left, right)   # sort in ascending order

"""


def merge_sort(iterables, version=None):
    return list(map(int, sorted(iterables))) if version is None else merge(iterables)


def merge(iterables):
    """split iterables """
    length = len(iterables)
    if length <= 1:
        return iterables
    mid = length // 2

    left = merge(iterables[:mid])
    right = merge(iterables[mid:])

    return _sort(left, right)


def _sort(left, right):
    """sort item into array"""
    array = []

    left_len = len(left)
    right_len = len(right)

    right_index = left_index = 0

    while right_index < right_len and left_index < left_len:

        if left[left_index] < right[right_index]:
            array.append(left[left_index])
            left_index += 1
        else:
            array.append(right[right_index])
            right_index += 1

    if left_index < left_len:
        array = array + left[left_index:]

    if right_index < right_len:
        array = array + right[right_index:]

    return array
