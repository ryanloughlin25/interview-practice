def find_median(array1, array2):
    if not array1 and not array2:
        return None
    if len(array1) == 1 and len(array2) == 1:
        return (array1[0] + array2[0]) / 2
    if not array1:
        return find_median_single_array(array2)
    if not array2:
        return find_median_single_array(array1)
    array1_len = len(array1)
    array2_len = len(array2)
    array1_middle = array1[array1_len // 2]
    array2_middle = array2[array2_len // 2]
    if array1_middle > array2_middle:
        new_array1 = array1[:array1_len // 2]
        new_array2 = array2[array2_len // 2:]
        return find_median(new_array1, new_array2)
    else:
        new_array1 = array1[array1_len // 2:]
        new_array2 = array2[:array2_len // 2]
        return find_median(new_array1, new_array2)

def find_median_single_array(array):
    if len(array) % 2 == 0:
        middle = len(array) // 2
        return ((array[middle - 1] + array[middle]) / 2)
    else:
        middle = len(array) // 2
        return array[middle]
