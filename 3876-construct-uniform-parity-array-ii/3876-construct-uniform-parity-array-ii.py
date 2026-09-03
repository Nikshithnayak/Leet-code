class Solution(object):
    def uniformArray(self, nums1):
        minimum = min(nums1)

        # If the smallest number is odd,
        # we can make every element odd.
        if minimum % 2 == 1:
            return True

        # Smallest number is even.
        # Then all numbers must already be even.
        for num in nums1:
            if num % 2 == 1:
                return False

        return True