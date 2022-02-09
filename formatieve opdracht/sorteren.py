def binary_index(sorted_lst, item, mini, maxi):
    """Takes a sorted list and an item as input. Returns the index on which the item should be inserted."""
    if mini > maxi:
        return maxi + 1
    midi = mini + ((maxi - mini) // 2)
    if item == sorted_lst[midi]:
        return midi
    if item < sorted_lst[midi]:
        return binary_index(sorted_lst, item, mini, midi - 1)
    # only option left is:  item > sorted_lst[midi]
    return binary_index(sorted_lst, item, midi + 1, maxi)


def my_sort(lst):
    """Takes an unsorted list as input. Binary sorts a copy of the list. Returns this copy."""
    sorted_lst = [lst[0]]
    for item in lst[1:]:
        sorted_lst.insert(binary_index(sorted_lst, item, 0, (len(sorted_lst) - 1)), item)
    return sorted_lst


a_lst = [8, 6, 4, 2, 6, 5, 3, 5, 7, 8, 3, 2, 4, 6]
sorted_a_lst = my_sort(a_lst)
print(len(a_lst), sorted_a_lst, len(sorted_a_lst))
