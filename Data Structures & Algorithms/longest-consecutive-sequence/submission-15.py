class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        max_count = 0
        count = 0
        for num in nums:
            hashset.add(num)

        for i in hashset:
            current_num = i
            if i - 1 in hashset:
                continue

            if i - 1 not in hashset:
                count = 1
            while current_num + 1 in hashset:
                current_num += 1
                count += 1
            
            if count >= max_count:
                max_count = count
            

        return max_count