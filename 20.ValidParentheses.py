class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for char in s:
            if char not in brackets and char not in brackets.values():
                return False  
            if char in brackets:
                stack.append(char)  
            elif char in brackets.values():
                if not stack or brackets[stack.pop()] != char:
                    return False  
        return len(stack) == 0


test1 = Solution()
print(test1.isValid("a)([()]"))  # Example usage
print(test1.isValid(")([()]"))
print(test1.isValid("([()]"))
print(test1.isValid("([()])"))
print(test1.isValid("()"))
print(test1.isValid("([)]"))
print(is_valid_parentheses("a)([()]"))  # Example usage
print(is_valid_parentheses(")([()]")) 
print(is_valid_parentheses("([()]"))
print(is_valid_parentheses("([()])"))
print(is_valid_parentheses("()"))   
        

#scratch below here
def is_valid_parentheses(s):

    brackets = ['()', '[]', '{}','(', ')', '[', ']', '{', '}']
    open_brackets = ['(', '[', '{']
    closed_brackets = [')', ']', '}']        
    bracket_type = {'{':'curly', '[':'square', '(': 'round',
                    '}':'curly', ']':'square', ')': 'round'}
    bracket_function = {'{': 'open', '[': 'open', '(': 'open',
                    '}': 'close', ']': 'close', ')': 'close'}


    #s = "a)([()]"

    round_count = 0
    curly_count = 0
    square_count = 0

    for char in s:
        if char not in brackets:
            return False

        if char in open_brackets and bracket_type[char] == 'round':
            round_count += 1
        elif char in closed_brackets and bracket_type[char] == 'round':
            round_count -= 1
        elif char in open_brackets and bracket_type[char] == 'curly':
            curly_count += 1
        elif char in closed_brackets and bracket_type[char] == 'curly':
            curly_count -= 1    
        elif char in open_brackets and bracket_type[char] == 'square':
            square_count += 1
        elif char in closed_brackets and bracket_type[char] == 'square':
            square_count -= 1   
        
        if round_count < 0 or curly_count < 0 or square_count < 0:
            return False
        
    return round_count == 0 and curly_count == 0 and square_count == 0



print(is_valid_parentheses("a)([()]"))  # Example usage
print(is_valid_parentheses(")([()]")) 
print(is_valid_parentheses("([()]"))
print(is_valid_parentheses("([()])"))
print(is_valid_parentheses("()"))   

