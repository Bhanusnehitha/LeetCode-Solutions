class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numbers=[]

        for num in nums:
            numbers.append(str(num))

        for i in range(len(numbers)):

            for j in range(i+1,len(nums)):
                a=numbers[i]
                b=numbers[j]

                if a+b < b+a:
                    numbers[i]=b
                    numbers[j]=a

        if numbers[0]=="0":
            return "0"
            
        answer=""

        for num in numbers:
            answer=answer+num
                
        return answer

        