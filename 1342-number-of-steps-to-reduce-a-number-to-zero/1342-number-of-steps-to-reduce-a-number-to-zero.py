class Solution:
    def numberOfSteps(self, num: int) -> int:
        #return number of steps to take from num to 0
        #even number divide by 2
        #odd number subtract 1
        
        #using counting bits
        
        steps = 0
        
        binary = bin(num)[2:] #removing 0b from the binary 
        
        for bit in binary:
            if bit == '1':
                steps += 2
            else:
                steps +=1
        return steps - 1