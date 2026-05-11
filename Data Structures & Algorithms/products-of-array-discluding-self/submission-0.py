class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        running_product = 1
        for i in range(len(nums)):
            res[i] = running_product
            running_product *= nums[i]
        
        running_product = 1
        for i in reversed(range(len(nums))):
            res[i] *= running_product
            running_product *= nums[i]

        return res


"""

1. Input / return?
Input: List[int]
Return: List[int], where output[i] = product of all nums except nums[i].

2. Constraints / complexity?
n <= 1000.
Target is O(n), no division.

3. Simplest brute force?
For each index, multiply every other number.

4. What is wrong with brute force?
It repeats the same left/right products over and over.
O(n²).

5. What pattern does that suggest?
Prefix/suffix accumulation.
Left product * right product.

6. Edge cases?
Zeros, multiple zeros, negatives, length 2.

"""