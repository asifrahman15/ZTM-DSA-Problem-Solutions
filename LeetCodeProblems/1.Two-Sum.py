class Solution:
    def twoSumBruteForce(self, nums: list[int], target: int) -> list[int]:
        """
        The Time Complexity of the code is O(n^2)

        The logic used here was iterating with one fixed value and 
            all other value remain in the list
        """

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        The Time Complexity of the code is O(n)

        The logic used here was generating the hash map for the index with their required value,
            to get the target so with this the upcomming number is present in the key,
            then this was required by some other index, we already have that index map,
            so will return that and the current index
        """

        mapper = {}
        for ind, num in enumerate(nums):
            print(mapper)
            print(f"Checking if {num} exists in mapper: {mapper.get(num)}")
            if mapper.get(num) is not None:
                return [mapper.get(num), ind]
            mapper[target-num] = ind

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(sol.twoSum([3, 2, 4], 6))  # Output: [0, 0]
print(sol.twoSum([3, 3], 6))  # Output: [0,1]
