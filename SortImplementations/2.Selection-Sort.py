class Solution:
    def selectionSort(self, elements: list, ascending=True) -> list:
        """
        The time complexity of this code O(n^2).

        This is not an efficient way of Sorting but can be implemented easily.
        """
        for i in range(len(elements)):
            ref = i
            for j in range(i+1, len(elements)):
                # print("List :", elements)
                # print("\tCompared :", elements[ref], elements[j])
                if ((elements[ref] > elements[j]) and ascending) or \
                        ((elements[ref] < elements[j]) and (not ascending)):
                    # print(f"\t\tRefernce Index Updated {ref}, {j}")
                    ref = j
            if ref != i:
                elements[ref], elements[i] = elements[i], elements[ref]
                # print(f"Swapped ({ref}, {i}): ", elements[ref], elements[i])
            # print()

        return elements

sol = Solution()
print(sol.selectionSort([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.selectionSort([-2,1,-3,4,-1,2,1,-5,4], False))
