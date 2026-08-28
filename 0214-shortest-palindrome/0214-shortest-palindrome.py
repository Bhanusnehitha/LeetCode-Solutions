class Solution:
    def shortestPalindrome(self, s: str) -> str:

        if s == "":
            return ""

        for i in range(len(s),0,-1):
            prefix=s[:i]

            if prefix == prefix[::-1]:
                remaining=s[i:]

                return remaining[::-1] + s