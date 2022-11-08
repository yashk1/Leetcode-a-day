#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
	    maxx = 0
	    rowindex = -1
		for i in range(len(arr)):
		    curr_max  = 0
		    for j in arr[i]:
		        if j == 1:
		            curr_max +=1
		        if curr_max > maxx:
		            maxx = max(curr_max, maxx)
		            rowindex = i
		return rowindex
		        
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends