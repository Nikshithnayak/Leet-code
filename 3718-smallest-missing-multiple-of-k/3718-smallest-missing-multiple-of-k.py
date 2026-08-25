class Solution(object):
    def missingMultiple(self, nums, k):
        numbers = set(nums)

        multiple = k

        while multiple in numbers:
            multiple += k

        return multiple