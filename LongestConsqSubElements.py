class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = []
        data = {}
        longest_length = 0
        for n in nums:
            data[n] = n

        for i in range(len(nums)):
            if res[-1] + 1 == nums[i]:
                res.append(n)
                longest_length += 1
            elif res[-1] + 1 in data:
                res.append(data[res[-1] + 1])
                longest_length += 1
            i += 1

        return res
