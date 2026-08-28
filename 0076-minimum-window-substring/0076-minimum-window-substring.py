class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        left = 0
        have = 0
        need_count = len(need)

        result = ""
        result_len = float("inf")

        for right in range(len(s)):

            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_count:

                if right - left + 1 < result_len:
                    result_len = right - left + 1
                    result = s[left:right + 1]

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                left += 1

        return result