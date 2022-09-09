class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        # K1:L2
        result = []
        for i in range( ord(s[0]) , ord(s[3]) +1 ):
            rs=""
            for j in range( int(s[1]) , int(s[4])+1 ):
                rs = chr(i) + str(j)
                result.append(rs)
        return result 

'''
ord(character) gives ascii value of that character
chr(ascii) converts ascii value back to character

example:
ord("a")=97
chr(97)= a

ord("A")=65
chr(65)=A

fun fact: Difference between ascii values of lowercase character and its uppercase is 32
'''