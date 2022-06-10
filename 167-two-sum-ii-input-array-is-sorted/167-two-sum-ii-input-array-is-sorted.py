class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for index, value in enumerate(numbers):
            
            complement = target - value #7 #2
            
            if complement in hashmap: #is 7 in hashmap? NO #2in hashmap?Yes
                return [hashmap[complement]+1,index+1]
            else:
                hashmap[value] = index
                