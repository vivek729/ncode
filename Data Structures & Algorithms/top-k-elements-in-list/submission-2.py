class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        freqs = Counter(nums)
        if len(freqs) <= k:
            return [num for num in freqs]

        topk = []
        # max freq for any num can be len(nums)
        # store num(s) in appropriate index in freq_to_nums depending on their counts
        freq_to_nums = [[] for _ in range(len(nums))]
        for num, count in  freqs.items():
            freq_to_nums[count].append(num)
        
        for i in range(len(freq_to_nums) - 1, -1, -1):
            if freq_to_nums[i] and len(topk) < k:
                topk.extend(freq_to_nums[i])

        return topk
