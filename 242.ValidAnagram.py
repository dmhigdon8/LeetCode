class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        return count_s == count_t
    
test1 = Solution()

test1.isAnagram("test", "tests")

# scratch below this
s = "test"

t = "tests"

count = {}

for char in s:
    count[char] = count.get(char, 0) + 1

print(count)

count = {}
for char in t:
    count[char] = count.get(char, 0) + 1

print(count)

total = sum(count.values())
print(total)