class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        count={}

        for num in arr1:
            count[num]=count.get(num,0)+1

        result=[]

        for num in arr2:
            if num in count:
                result.extend([num]*count[num])

                del count[num]

        remaining=[]

        for num in count:
            remaining.extend([num]*count[num])

        remaining.sort()

        result.extend(remaining)

        return result