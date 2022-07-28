class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #new max = max(old_max, arr[i])
        
        maxx = -1
        
        
        for c in range(len(arr)-1, -1, -1):
            arr[c] , maxx = maxx, max(arr[c], maxx)
            
        return arr