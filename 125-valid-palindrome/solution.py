# https://leetcode.com/problems/valid-palindrome/submissions/

class Solution:
    """A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
    removing all non-alphanumeric characters, it reads the same forward and backward. 
    Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
    """
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1        
        
        while left < right:
            # advance left and right pointers if char is not alpha num
            while left < right and not self.is_alpha_num(s[left]):
                left += 1
            while right > left and not self.is_alpha_num(s[right]):
                right -= 1

            # compare left and right chars... if not equal, then it's not a palindrone
            l = s[left].upper()
            r = s[right].upper()
            if s[left].upper() == s[right].upper():
                print(f'left and right are equal: {left=}({l}) {right=}({r})')
                left += 1
                right -= 1
            else:
                print(f'Returning {False}... {l=} and {r=} are not equal')
                return False

        return True


    def is_alpha_num(self, s):
        if 'a' <= s.lower() <= 'z' or "0" <= s <= "9":
            return True


s = Solution()
s.isPalindrome('racecar')
s.isPalindrome('race a car')
s.isPalindrome('A man a plan a canal Panama')
s.isPalindrome('A man, a plan, a canal: Panama')
s.isPalindrome(' ')