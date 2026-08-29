class Solution:
    def partition(self, s):

        result = []

        def isPalindrome(word):
            return word == word[::-1]

        def backtrack(start, path):

            # We have used the complete string
            if start == len(s):
                result.append(path[:])
                return

            # Try every possible ending position
            for end in range(start, len(s)):

                word = s[start:end + 1]

                # Only choose palindrome parts
                if isPalindrome(word):

                    path.append(word)

                    backtrack(end + 1, path)

                    # Backtrack
                    path.pop()

        backtrack(0, [])

        return result
        