class Solution:
    def quickSort(self, elements: list, ascending=True) -> list:
        """
        The time complexity of this code averagely O(n log(n)).
            But, at the worst case scenario it can be O(n^2)
        This is because of the divide and conquer approach.

        But this has the space complexity of O(log(n)) because of the
        additional space used for merging the sorted arrays.

        Note: This is a unstable sort, meaning that
            it doesn't maintains the relative order of equal elements.
        """
        if len(elements) < 2:
            return elements

        pivot_position = len(elements) - 1
        pivot_element = elements[pivot_position]
        # print("Elements :", elements, pivot_position, pivot_element)
        i = 0
        while pivot_position > i:
            # print(elements[i], ">", pivot_element, elements[pivot_position - 1], elements[i] > pivot_element)
            if ((elements[i] > pivot_element) and ascending) or \
                    ((elements[i] < pivot_element) and (not ascending)):
                # print(f"Swaps ({elements[pivot_position]} -> {elements[i]}),"
                #       f" ({elements[i]} -> {elements[pivot_position - 1]}),"
                #       f" ({elements[pivot_position - 1]} -> {elements[pivot_position]})")
                elements[pivot_position], elements[i], elements[pivot_position - 1] = \
                    elements[i], elements[pivot_position - 1], elements[pivot_position]
                pivot_position -= 1
            else:
                i += 1
            # print(elements, pivot_position)
            # print()
        return [*self.quickSort(elements[:pivot_position]), pivot_element, *self.quickSort(elements[pivot_position+1:])]

sol = Solution()

print(sol.quickSort([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.quickSort([-2,1,-3,4,-1,2,1,-5,4], False))
