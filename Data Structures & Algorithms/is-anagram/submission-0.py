class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset = set()

        for char in s:
            hashset.add(char)
        
        for char in t:
            if char not in hashset:
                return False
        
        return True