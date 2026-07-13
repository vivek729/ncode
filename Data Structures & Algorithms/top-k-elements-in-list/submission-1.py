from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)

        # only <=k distinct elements, return the distinct elements
        if len(freqs) <= k:
            return [num for num in freqs]

        min_heap = []
        for num, count in freqs.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (count, num))
            elif count > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (count, num))

        return [num for count, num in min_heap]
