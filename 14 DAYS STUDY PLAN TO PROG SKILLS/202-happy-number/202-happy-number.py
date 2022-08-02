class Solution:
    def isHappy(self, n: int) -> bool:
        
        #get next digit
        #create a haset to detect cycle
        
        #to get digits one by one we use divmod 
        #eg. n= 199 -> n,digit =  divmod( 199(n) , 10 )
        #return n = 19 digit =9
        #to get 1 and 9, run this in while loop until remainder becomes zero
        def get_next(n): 
            next = 0
            
            while n >0:
                n, digit = divmod(n, 10)
                next += digit ** 2 #this is what ques asked to do 
            return next 
    
    #detecting cycle using Floyd's cycle finding algo #fast and slow pointer
        
        sp = n
        fp = get_next(n)
        
        while fp !=1 and sp!= fp:
            sp = get_next(sp)
            fp = get_next(get_next(fp))
            
        return fp == 1
        
    
        
        