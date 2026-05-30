class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        sorted_list = sorted(num_set)
        max_count = 0
        current_count = 0
        previous_int = sorted_list[0]-1

        for i in sorted_list:
            
            if i == previous_int + 1:
                current_count += 1
                if current_count >= max_count:
                    max_count += 1
            else:
                current_count = 0
            
            previous_int = i

        return max_count
