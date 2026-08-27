class Solution(object):
    def lexGreaterPermutation(self, s, target):
        
        # Count frequency of characters in s
        count = [0] * 26
        
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        prefix = []
        
        # Try to match target from left to right
        i = 0
        
        while i < len(target):
            index = ord(target[i]) - ord('a')
            
            if count[index] == 0:
                break
            
            count[index] -= 1
            prefix.append(target[i])
            i += 1
        
        # Go backwards and try to make one character bigger
        for pos in range(i, -1, -1):
            
            # If this position was already matched,
            # put that character back
            if pos < i:
                char_index = ord(target[pos]) - ord('a')
                count[char_index] += 1
                prefix.pop()
            
            # Find the smallest available character
            # greater than target[pos]
            if pos < len(target):
                target_index = ord(target[pos]) - ord('a')
                
                for j in range(target_index + 1, 26):
                    if count[j] > 0:
                        
                        result = prefix + [chr(j + ord('a'))]
                        
                        count[j] -= 1
                        
                        # Add remaining characters
                        # in sorted order
                        for x in range(26):
                            result.extend(
                                [chr(x + ord('a'))] * count[x]
                            )
                        
                        return "".join(result)
        
        return ""