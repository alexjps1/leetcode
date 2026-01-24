from typing import List


# first solution with three passes
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        pre[0] = nums[0]
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i]

        post = [0] * len(nums)
        post[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i]

        output = [0] * len(nums)
        output[0] = post[1]
        output[-1] = pre[-2]
        for i in range(1, len(nums) - 1):
            output[i] = pre[i - 1] * post[i + 1]

        return output


# with help, second solution with two passes
# uses only one answer array instead of three arrays
# here, the prefix and postfix excludes the number itself (i.e. prefix at index i product of all numbers before index i)
# whereas in my previous solution, prefix at index i was product of all numbers up to and including index i
class OptimalSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        prefix = 1
        for i in range(0, len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans
