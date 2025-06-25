class Solution:
    def insertionSort(self, elements: list, ascending=True) -> list:
        """
        The time complexity of this code O(n^2). This O(n) in almost sorted Array.

        This is not an efficient way of Sorting but can be implemented easily.
        """
        for i in range(1, len(elements)):
            # print(f"List: {elements}, Sorted: {elements[:i]}")
            if (elements[i] == elements[i-1]) or \
                    ((elements[i] > elements[i-1]) and ascending) or \
                    ((elements[i] < elements[i-1]) and (not ascending)):
                # print(f"Already {elements[i]} ({i}) is aligned with Sorted Array")
                continue
            else:
                ref = elements[i]
                # print(f"Taken the Refenrce at {i}: {ref}")
                for j in range(i, -1, -1):
                    # print(f"Compare {elements[j-1]} ({j-1}) and {ref}")
                    # If it reaches 0, then no privious element is there
                    #     to compare and that's also pushed to previous
                    if (j != 0) and (((elements[j-1] > ref) and ascending) or \
                            ((elements[j-1] < ref) and (not ascending))):
                        elements[j] = elements[j-1]
                        # print(f"Pushing elements {elements}")
                    else:
                        elements[j] = ref
                        # print(f"Inserted element at {j+1} {elements}")
                        break
            # print()

        return elements

sol = Solution()
print(sol.insertionSort([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.insertionSort([-2,1,-3,4,-1,2,1,-5,4], False))
