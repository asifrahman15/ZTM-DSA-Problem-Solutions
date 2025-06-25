class Solution:
    def bubbleSort(self, elements: list, ascending=True) -> list:
        """
        The time complexity of this code O(n^2).

        This is not an efficient way of Sorting but can be implemented easily.
        """
        for i in range(1, len(elements)):
            for j in range(len(elements)-i):
                # print("List :", elements)
                # print("\tCompared :", elements[j], elements[j+1])
                if ((elements[j] > elements[j+1]) and ascending) or \
                        ((elements[j] < elements[j+1]) and (not ascending)):
                    elements[j], elements[j+1] = elements[j+1], elements[j]
                    # print(f"\t\tSwapped ({j}, {j+1}): ", elements[j], elements[j+1])
            # print()

        return elements

sol = Solution()
print(sol.bubbleSort([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.bubbleSort([-2,1,-3,4,-1,2,1,-5,4], False))
