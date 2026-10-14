class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        seen = Counter()
        for num in nums:
            seen[num] += 1
            if seen[num]>1:
                return True
        return False


        