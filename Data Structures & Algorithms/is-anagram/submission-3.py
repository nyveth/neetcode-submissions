class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts_s = {}
        counts_t = {}

        for char_s in s:
            counts_s[char_s] = counts_s.get(char_s, 0) + 1
        
        for char_t in t:
            counts_t[char_t] = counts_t.get(char_t, 0) + 1

        if counts_s == counts_t:
            return True
        
        return False