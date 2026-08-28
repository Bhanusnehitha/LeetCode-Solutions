class Solution(object):
    def minDays(self, bloomDay, m, k):
       
        if m * k > len(bloomDay):
            return -1

       
        def canMakeBouquets(day):
            bouquets = 0
            flowers = 0
            
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    
                    if flowers == k:
                        bouquets += 1
                        flowers = 0 
                else:
                    flowers = 0  
            
            return bouquets >= m

       
        low, high = min(bloomDay), max(bloomDay)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            
            if canMakeBouquets(mid):
                ans = mid
                high = mid - 1  
            else:
                low = mid + 1   
        return ans