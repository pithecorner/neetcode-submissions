class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            if target - n in dict.keys():
                return [dict[target - n],i]
            else:
                dict[n] = i



"""
create

"""