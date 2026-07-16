class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest_seq_len = 1
        num_set = set(nums)
        for num in nums:
            if num - 1 not in num_set:
                seq_len = 1
                next_no = num + 1
                while next_no in num_set:
                    seq_len += 1
                    next_no += 1
                longest_seq_len = max(longest_seq_len, seq_len)
        return longest_seq_len
