class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        max_count = 0
        count = 0
        for num in nums:
            hashset.add(num)
        
        if len(hashset) == 1:
            return 1

        for i in hashset:
            if i - 1 not in hashset:
                count += 1

            if i + 1 in hashset:
                count += 1
                if count >= max_count:
                    max_count = count

            if i + 1 not in hashset:
                count = 0

        return max_count