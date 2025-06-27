from math import ceil

class Solution:
    def split(self, elements: list):
        """
        This function splits the list into two halves.
        It returns two lists, one for each half.
        """
        mid = ceil(len(elements) / 2)
        return elements[:mid], elements[mid:]

    def merge(self, left_elements: list, right_elements: list, ascending=True):
        # print("Sorted Left :", left_elements)
        # print("Sorted Right :", right_elements)
        final_arr = []
        left_ind = 0
        right_ind = 0
        while left_ind < len(left_elements) and \
                right_ind < len(right_elements):
            if ((left_elements[left_ind] <= right_elements[right_ind]) and ascending) or \
                    ((left_elements[left_ind] >= right_elements[right_ind]) and (not ascending)):
                final_arr.append(left_elements[left_ind])
                left_ind += 1
            else:
                final_arr.append(right_elements[right_ind])
                right_ind += 1
        final_arr.extend(left_elements[left_ind:])
        final_arr.extend(right_elements[right_ind:])
        # print("Merged :", final_arr)
        # print()
        return final_arr

    def mergeSort(self, elements: list, ascending=True) -> list:
        """
        The time complexity of this code O(n log(n)).
        This is because of the divide and conquer approach.

        But this has the space complexity of O(n) because of the
        additional space used for merging the sorted arrays.

        Note: This is a stable sort, meaning that
            it maintains the relative order of equal elements.
        """
        if len(elements) == 1:
            return elements
        left, right = self.split(elements)
        # print()
        # print("Left :", left)
        # print("Right :", right)

        return self.merge(
            self.mergeSort(left, ascending),
            self.mergeSort(right, ascending),
            ascending
        )

sol = Solution()
print(sol.mergeSort([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.mergeSort([-2,1,-3,4,-1,2,1,-5,4], False))
