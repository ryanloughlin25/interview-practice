class Solution:
    def findMedianSortedArrays(self, array1, array2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not array1 and not array2:
            return None
        if len(array1) == 1 and len(array2) == 1:
            return (array1[0] + array2[0]) / 2.0
        if len(array1) + len(array2) < 5:
            new_array = self.merge_sorted_arrays(array1, array2)
            return find_median_single_array(new_array)
        if not array1:
            return self.find_median_single_array(array2)
        if not array2:
            return self.find_median_single_array(array1)
        array1_len = len(array1)
        array2_len = len(array2)
        array1_median = self.find_median_single_array(array1)
        array2_median = self.find_median_single_array(array2)
        if array1_median > array2_median:
            new_array1 = array1[:(array1_len // 2)]
            new_array2 = array2[array2_len // 2:]
            return self.findMedianSortedArrays(new_array1, new_array2)
        elif array2_median > array1_median:
            new_array1 = array1[array1_len // 2:]
            new_array2 = array2[:(array2_len // 2)]
            return self.findMedianSortedArrays(new_array1, new_array2)
        elif array2_median == array1_median:
            return array1_median

    def find_median_single_array(self, array):
        if len(array) % 2 == 0:
            middle = len(array) // 2
            return ((array[middle - 1] + array[middle]) / 2.0)
        else:
            middle = len(array) // 2
            return array[middle]

    def merge_sorted_arrays(self, array1, array2):
        i = j = 0
        new_array = []
        while i < len(array1)-1 or j < len(array2)-1:
            if array1[i] > array2[j]:
                new_array.append(array1[i])
                if i < (len(array1) - 1): i += 1
            else:
                new_array.append(array2[j])
                if j < (len(array2) - 1): j += 1
        return new_array
