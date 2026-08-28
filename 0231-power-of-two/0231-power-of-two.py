class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n <= 0:
            return False

        if n % 2==0:
            if n & (n-1)==0:
                return True
            else:
                return False
        else:
            return False
   
            