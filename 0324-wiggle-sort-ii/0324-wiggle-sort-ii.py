class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res=[]
        nums.sort()
        n=len(nums)

        left=(n-1)//2
        right=n-1

        for i in range(0,n):
            if (i%2==0):
                res.append(nums[left])
                left=left-1
            else:
                res.append(nums[right])
                right=right-1
        
        for i in range(n):
            nums[i]=res[i]



