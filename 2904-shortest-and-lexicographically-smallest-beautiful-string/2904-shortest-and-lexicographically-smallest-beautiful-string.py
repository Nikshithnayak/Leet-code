class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        left = 0
        ones = 0

        result = ""

        for right in range(len(s)):

            # Add current character
            if s[right] == '1':
                ones += 1

            # Too many 1's → shrink window
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # Exactly k 1's
            if ones == k:

                # Remove unnecessary leading zeros
                while s[left] == '0':
                    left += 1

                current = s[left:right + 1]

                # First answer OR shorter answer OR lexicographically smaller
                if (result == "" or
                    len(current) < len(result) or
                    (len(current) == len(result) and current < result)):

                    result = current

        return result