
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)]
        top_k = []
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for num, freq in counter.items():
            buckets[freq].append(num)

        top_k = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k

