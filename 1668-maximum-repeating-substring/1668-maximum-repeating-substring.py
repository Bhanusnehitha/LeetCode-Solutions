class Solution:
    def maxRepeating(self, sequence, word):
        count = 0
        current = word

        while current in sequence:
            count += 1
            current += word

        return count