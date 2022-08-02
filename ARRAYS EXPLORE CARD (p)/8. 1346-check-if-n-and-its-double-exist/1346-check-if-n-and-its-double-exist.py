class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = {}
        
        for i in range(len(arr)):
            if arr[i] /2 in hashmap or arr[i] * 2 in hashmap:
                return True
            else:
                hashmap[arr[i]] = i
        return False