class Solution:
    def leastInterval(self, tasks, n):

        freq = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        max_freq = max(freq.values())

        count_max = 0

        for count in freq.values():
            if count == max_freq:
                count_max += 1

        formula = (max_freq - 1) * (n + 1) + count_max

        return max(len(tasks), formula)