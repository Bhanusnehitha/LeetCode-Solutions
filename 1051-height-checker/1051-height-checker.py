class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        y=sorted(heights)

        for i in range(0,len(heights)):
            if heights[i]!=y[i]:
                count=count+1

        return count


