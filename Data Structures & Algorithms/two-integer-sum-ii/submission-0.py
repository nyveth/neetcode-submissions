class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            curr_summ = numbers[l] + numbers[r]

            if curr_summ == target:
                return [l+1, r+1]
            elif curr_summ > target:
                r -= 1
            else:
                l += 1
        
        return [-1, -1]
            