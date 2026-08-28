class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        n = len(s)
        
        # Step 1: Count character frequencies
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1
            
        odd_count = 0
        mid_char = ""
        for i in range(26):
            if counts[i] % 2 != 0:
                odd_count += 1
                mid_char = chr(i + ord('a'))
                
        # Validate if a palindrome can be formed
        if (n % 2 == 1 and odd_count != 1) or (n % 2 == 0 and odd_count != 0):
            return ""
            
        # Characters available for constructing the first half
        H_avail = [counts[i] // 2 for i in range(26)]
        m = n // 2
        
        # Step 2: Phase 1 - Try Exact match of the first half
        H = target[:m]
        temp_avail = list(H_avail)
        possible = True
        
        for char in H:
            idx = ord(char) - ord('a')
            if temp_avail[idx] == 0:
                possible = False
                break
            temp_avail[idx] -= 1
            
        if possible:
            P = H + mid_char + H[::-1]
            if P > target:
                return P
                
        # Step 3: Phase 2 - Find the optimal divergence point
        for i in range(m - 1, -1, -1):
            temp_avail = list(H_avail)
            possible = True
            
            # Consume characters to match the prefix up to i-1
            for j in range(i):
                idx = ord(target[j]) - ord('a')
                if temp_avail[idx] == 0:
                    possible = False
                    break
                temp_avail[idx] -= 1
                
            if not possible:
                continue
                
            t_char_idx = ord(target[i]) - ord('a')
            
            # Find the smallest available character strictly greater than target[i]
            found_c_idx = -1
            for k in range(t_char_idx + 1, 26):
                if temp_avail[k] > 0:
                    found_c_idx = k
                    break
                    
            if found_c_idx != -1:
                # Build the first half up to the divergence point
                temp_avail[found_c_idx] -= 1
                H_list = list(target[:i])
                H_list.append(chr(found_c_idx + ord('a')))
                
                # Fill the rest of the first half with the smallest available characters
                for k in range(26):
                    while temp_avail[k] > 0:
                        H_list.append(chr(k + ord('a')))
                        temp_avail[k] -= 1
                        
                H_str = "".join(H_list)
                
                # Assemble and return the full mirrored palindrome
                return H_str + mid_char + H_str[::-1]
                
        return ""