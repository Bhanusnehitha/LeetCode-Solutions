class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n=len(citations)
        count=0
        for i in range(n):
            if citations[i]>=i+1:
                count+=1
            else:
                break
        return count