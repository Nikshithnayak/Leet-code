class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        # Find indices of minimum and maximum
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        # left = smaller index
        # right = bigger index
        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # Option 1: Remove both from the front
        front = right + 1

        # Option 2: Remove both from the back
        back = n - left

        # Option 3: Remove one from front and one from back
        both_sides = (left + 1) + (n - right)

        return min(front, back, both_sides)