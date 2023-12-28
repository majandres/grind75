# https://leetcode.com/problems/valid-anagram/

class Solution:
    """Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    """
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
    
        # place both s & t into dict with keys being the letter and the count it's value
        d1, d2 = {}, {}

        for i in range(len(s)):
            if d1.get(s[i]):
                d1[s[i]] += 1
            else:
                d1[s[i]] = 1

            if d2.get(t[i]):
                d2[t[i]] += 1
            else:
                d2[t[i]] = 1

        # if val in d2 does not match d1, not an anagram
        for k,v in d1.items():
            if d2.get(k) != v:
                return False
            
        return True


s = Solution()
print(f"anagram and nagaram: {s.isAnagram('anagram','nagaram')}")
print(f"rata and car: {s.isAnagram('rata','car')}")