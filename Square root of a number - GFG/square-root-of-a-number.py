#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, y): 
        start = 1
        end = y // 2 
        ans = 1
        while start <= end:
            mid = (start+end) //2
        
            if mid * mid <= y:
                start = mid + 1
                ans = mid #this is the case of 5
            else:
                end = mid -1
            
        return ans
    #Your code here
    
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends