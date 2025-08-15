# scratch below this

s = ["h","e","l","l","o"]

t = []
t[:] = s[::-1]  
print(t)

#print(s[-1:-len(s)-1:-1])

#print(-len(s)-1)

#print(s[-1:-5])

#print(-len(s))

s = s[-1:-len(s)-1:-1]
print(s)

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]  

