# https://leetcode.com/problems/valid-parentheses/

class Solution:
    """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.
    Input: s = "()[]{}"
    Output: true
    
    Input: s = "(]"
    Output: false
    """
    def isValid(self, s: str) -> bool:
        # handle constraints first
        if len(s) <= 1 or len(s) > 10000:
            print(f"Length of input cannot be <=1 or > 10^4")
            return False

        if len(s) % 2 != 0:
            print(f'Unbalanced number of chars received: {len(s)}')
            return False

        mapa = {
            "}": "{",
            "]": "[",
            ")": "(",
            ">": "<"
        }

        stack = []

        for c in s:
            # c is a closing paranthesis
            if c in mapa:
                if stack and stack[-1] == mapa[c]:
                    stack.pop()
                else:
                    return False
            else: # it's an opening paranthesis
                stack.append(c)

        return True if not stack else False

s = Solution()

print(s.isValid("()[]"))  # true
print(s.isValid("()[]<>"))  # true
print(s.isValid("[((<{}>))]"))  # true
print(s.isValid("(]"))  # false
print(s.isValid("("))  # invalid
print(s.isValid("]"))  # invalid
print(s.isValid("()[]<"))  # invalid