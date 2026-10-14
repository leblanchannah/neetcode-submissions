class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums[i:]):
                actual_index_j = i+j
                if (num_i+num_j==target) and (i!=actual_index_j):
                    return [i,actual_index_j]
                
        