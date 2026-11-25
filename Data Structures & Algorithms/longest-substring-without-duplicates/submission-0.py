class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_set = set()
        max_lenght = 0
        for r in range(len(s)):
            if s[r] not in char_set:
                char_set.add(s[r])
                len_set = len(char_set)
                if max_lenght < len_set:
                    max_lenght = len_set
                
            else:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1
            char_set.add(s[r])
            len_set = len(char_set)
            if max_lenght < len_set:
                max_lenght = len_set      
        return max_lenght
