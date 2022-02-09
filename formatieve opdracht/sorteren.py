def binary_index(sorted_lst, item, mini, maxi):
    """
    takes a sorted list and an item as input. returns the index on which the item should be inserted.
    args:
        :param sorted_lst: (list) a sorted list
        :param item: item you are searching the index for in the sorted list.
        :param mini: (int) minimum index the target can be found at in the list
        :param maxi: (int) maximum index the target can be found at in the list
    returns:
        :return: (int) index on which the item should be inserted when the list is ordered.
    """
    if mini > maxi:
        return maxi + 1
    midi = mini + ((maxi - mini) // 2)
    if item == sorted_lst[midi]:
        return midi
    elif item < sorted_lst[midi]:
        return binary_index(sorted_lst, item, mini, midi - 1)
    return binary_index(sorted_lst, item, midi + 1, maxi)


def my_sort(lst):
    """
    takes an unsorted list as input. binary sorts a copy of the list. returns this copy.
    args:
        :param lst: (list) an unsorted list.
    returns:
        :return: (list) a sorted copy of the input list
    """
    sorted_lst = [lst[0]]
    for item in lst[1:]:
        sorted_lst.insert(binary_index(sorted_lst, item, 0, (len(sorted_lst) - 1)), item)
    return sorted_lst


a_lst = [8, 6, 4, 2, 6, 5, 3, 5, 7, 8, 3, 2, 4, 6]
sorted_a_lst = my_sort(a_lst)
print(len(a_lst), sorted_a_lst, len(sorted_a_lst))
