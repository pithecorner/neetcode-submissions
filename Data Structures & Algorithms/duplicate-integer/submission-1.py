class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for n in nums:
            if n in dict:
                return dict[n]
            else:
                dict[n] = True

        return False



# if any number appears > 1 time return true, else false

"""

Create empty dictionary

For each value in array

Check if value is in dictionary
if true
    output true
else
    insert value into dictionary.

return false
"""

    
