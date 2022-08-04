class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def rotation_index(l, r):
            if nums[l] < nums[r]:
                return 0
        
            while l <= r:
                mid  = l + (r-l) //2
            
                if nums[mid] > nums[mid+1]:
                        return mid+1
                else:
                    #the pivot index can be in left or right
                    if nums[mid] < nums[l]:
                        r = mid-1
                    else:
                        l = mid+1
    
        def search(l,r):
            while l <= r:
                mid = (l+r) //2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            return -1
        
        n = len(nums)
        
        if n==1:
            return 0 if nums[0] == target else -1
        
        rotate_index = rotation_index(0, n-1)
        
        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index
        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search(0, n - 1)
        if target < nums[0]:
            # search on the right side
            return search(rotate_index, n - 1)
        # search on the left side
        return search(0, rotate_index)

        
        
        
#4 5 6 7 8 9 0 1 2 

#5601234
