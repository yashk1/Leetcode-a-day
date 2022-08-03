class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        #ex - 25
        l = 2    #l =2 # 5
        r = x//2  #r = 12
        
        while l <= r: #2<12
            mid = l + (r-l) //2 #mid=7 #2+6//2 = 4 #8
            num = mid * mid  #num = 49 #16
            
            if num > x: #49 > 25 #16 !>25
                r = mid - 1 # 6
                
            elif num < x:  
                l = mid + 1 #l = 5
                 
            else:
                return mid
        return r
            
'''

for 25.

2 7 12

mid**2 = 49

updating r, mid-1

2 4 6

mid**2 = 16 

16 < x25

updating l, mid+1

5 5 6

mid**2 = 25

return mid
'''         
        

