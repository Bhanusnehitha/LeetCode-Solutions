class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)

        if n==1:
            return False

        for i in range(1,n):
            part=s[:i]

            if n%i==0:
                if part*(n//i)==s:
                    return True
           
        return False