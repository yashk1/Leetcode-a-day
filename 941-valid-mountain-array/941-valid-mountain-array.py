class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        
        #base case check
        if arr[0]>arr[1]:
            return False
        
        
        #first loop to find the peak
        peak=0
        index=0
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                peak = arr[i]
                index = i
                break
            if arr[i] == arr[i+1]:
                return False
            
            
        #second loop checks for values are in decreasing order after peak
        for i in range(index+1, len(arr)-1):
            if arr[i] <= arr[i+1] or arr[i]>peak:
                return False
        return True
            
        