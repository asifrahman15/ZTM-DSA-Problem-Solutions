class Solution:
    def maxSubArrayBruteForce(self, nums: list[int]) -> int:
        """
        The time complexity of this code O(n^3)
        """
        max_num = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                cur_sum = 0
                for num in nums[i:j]:
                    cur_sum += num
                if cur_sum > max_num:
                    max_num = cur_sum
        return max_num

    def maxSubArrayBetter(self, nums: list[int]) -> int:
        """
        The time complexity of this code O(n^2)
        """
        max_num = 0
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                if cur_sum > max_num:
                    max_num = cur_sum
        return max_num

    def maxSubArray(self, nums: list[int]) -> int:
        """
        The time complexity of this code O(n).

        This is known as Kadane's Algorithm
        """
        if not nums:
            return None
        cur_sum = max_num = nums[0]
        for num in nums[1:]:
            cur_sum += num
            if cur_sum > max_num:
                max_num = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        # This condition was applied, if empty array was considered
        # if max_num < 0:
        #     max_num = 0
        return max_num

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(sol.maxSubArray([1]))  # Output: 1
print(sol.maxSubArray([5,4,-1,7,8]))  # Output: 23
print(sol.maxSubArray([-5,-4,-1]))  # Output: -1
