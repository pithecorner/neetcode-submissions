class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = {}

        for n in nums:
            if n in counter_dict:
                counter_dict[n] = counter_dict[n] + 1
            else:
                counter_dict[n] = 1


        
        return sorted(counter_dict, key=counter_dict.get,reverse=True)[:k]