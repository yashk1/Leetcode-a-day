class Solution:
    def numberOfSteps(self, num: int) -> int:
        #return number of steps to take from num to 0
        #even number divide by 2
        #odd number subtract 1
        
        steps = 0
        while num > 0 :
            if num % 2 == 0:
                num = num // 2
                steps += 1
            else:
                num = num - 1
                steps +=1
        return steps
            