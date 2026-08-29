class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        left = 0
        max_len = 0
        freq = {}

        for right in range(len(fruits)):

            freq[fruits[right]] = freq.get(fruits[right], 0) + 1

            while len(freq) > 2:

                freq[fruits[left]] -= 1

                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]

                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len