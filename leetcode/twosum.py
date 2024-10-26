from typing import List
nums=[3,3]
target=6
iteration1=0
iteration2=1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==2:
            for Sum in range(len(nums)):
                for sum in range(len(nums)):
                    if nums[sum] + nums[Sum] == target:
                        x = [sum, Sum]
                        break
            return x
        else:
            for Sum in range(len(nums)):
                for sum in range(len(nums)):
                    if nums[sum] + nums[Sum] == target:
                        if sum == Sum:
                            break
                        else:
                            x = [sum, Sum]
            return x
ret = Solution().twoSum(nums=nums, target=target)
print(ret)


