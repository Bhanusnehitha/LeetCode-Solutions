class Solution:
    def longestDupSubstring(self, s):
        n = len(s)

        def check(length):
            seen = set()
            base = 26
            mod = 2**63 - 1

            h = 0
            power = 1

            for i in range(length):
                h = (h * base + ord(s[i])) % mod
                power = (power * base) % mod

            seen.add(h)

            for i in range(length, n):
                h = (h * base + ord(s[i])) % mod
                h = (h - ord(s[i - length]) * power) % mod

                if h in seen:
                    return s[i - length + 1:i + 1]

                seen.add(h)

            return ""

        left = 1
        right = n - 1
        answer = ""

        while left <= right:
            mid = (left + right) // 2
            duplicate = check(mid)

            if duplicate:
                answer = duplicate
                left = mid + 1
            else:
                right = mid - 1

        return answer