def longest_substring_without_repeating(string):
    count = {}
    longest_ = ''
    temp = ''
    for s in string:
        if s not in count:
            count[s] = 1
            temp += s
        else:
            temp += s
            print(longest_, temp)
            if len(temp) >= len(longest_):
                longest_ += temp
                temp = ''
    if len(temp) > len(longest_):
        longest_ = temp
    return (longest_, len(longest_))


print(longest_substring_without_repeating('pwwkewlabor'))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]

            index = chars[ord(r)]
            if index != None and index >= left and index < right:
                left = index + 1

            res = max(res, right - left + 1)

            chars[ord(r)] = right
            right += 1
        return res

sol = Solution()
# print(sol.lengthOfLongestSubstring    ('pwwkewlabor'))