class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):

        n = len(nums)

        # Store (value, original_index)
        pairs = []

        for i in range(n):
            pairs.append((nums[i], i))

        # Sort by value
        pairs.sort()

        result = nums[:]

        start = 0

        while start < n:

            end = start

            # Find all values in the same connected group
            while (end + 1 < n and
                   pairs[end + 1][0] - pairs[end][0] <= limit):
                end += 1

            # Get indices of this group
            indices = []

            for i in range(start, end + 1):
                indices.append(pairs[i][1])

            # Sort indices
            indices.sort()

            # Assign smallest values to smallest indices
            for i in range(len(indices)):
                result[indices[i]] = pairs[start + i][0]

            # Move to next group
            start = end + 1

        return result