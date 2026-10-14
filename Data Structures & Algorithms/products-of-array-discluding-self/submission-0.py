from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_side = [1] * n
        right_side = [1] * n
        answer = [1] * n

        for i in range(1, n):
            left_side[i] = left_side[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right_side[i] = right_side[i + 1] * nums[i + 1]

        for i in range(n):
            answer[i] = left_side[i] * right_side[i]

        return answer


