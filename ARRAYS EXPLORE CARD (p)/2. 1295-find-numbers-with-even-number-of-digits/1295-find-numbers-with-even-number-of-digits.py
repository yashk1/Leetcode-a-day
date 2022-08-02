class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        count = 0
        for num in nums:
            digits = floor(log10(num)) + 1 #this is the formula to find the number of digits in an interger
            
            if digits % 2 == 0:
                count +=1
        return count
        
#time - O(n)
#space - O(1)