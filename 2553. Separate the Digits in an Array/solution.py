class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        newArr=[]

        for i in nums:
            temp=[]
            while i>0:
                temp.append(i%10)
                i//=10
            newArr.extend(temp[::-1])
        
        return newArrc