class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subs = []
        one = []
        sub_sum = 0
        for n in nums:
            if n < k and sub_sum < k:
                sub_sum += n
                if sub_sum == k:
                    one.append(n)
                    subs.append(one)
                    sub_sum = n
                elif sub_sum < k:
                    one.append(n)
                else:
                    one = []
            elif n == k:
                one = []
                one = [k]
                subs.append(one)
                one = []
            elif n > k:
                one = []

        return len(subs)