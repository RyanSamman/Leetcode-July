import re


# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = re.split(r"\s+", s)
        ans.reverse()
        return " ".join(ans).strip()
