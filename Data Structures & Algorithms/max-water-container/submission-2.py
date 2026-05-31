class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        left_pointer = 0
        right_pointer = len(heights) - 1
        max_area = 0

        while left_pointer < right_pointer:
            total_area = (right_pointer - left_pointer) * min(heights[left_pointer], heights[right_pointer])

            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

            if total_area > max_area:
                max_area = total_area

        return max_area