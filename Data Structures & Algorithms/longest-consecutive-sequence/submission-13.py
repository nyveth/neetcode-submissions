class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_count = 0

        for i in hashset:
            current_num = i
            count = 1
            while current_num + 1 in hashset:
                current_num += 1
                count += 1
                if count >= max_count:
                    max_count = count

        return max_count