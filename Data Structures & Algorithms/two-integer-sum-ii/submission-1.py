class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1 

        while left < right:
            pointer_sum = numbers[left] + numbers[right]

            if pointer_sum > target:
                right -= 1
            elif pointer_sum < target:
                left +=1
            else:
                return [left + 1, right + 1]
        return []