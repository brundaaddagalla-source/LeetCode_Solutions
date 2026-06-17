class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[i.lower() for i in s if i.lower() in "qwertyuiopasdfghjklzxcvbnm0123456789"]
        if s==s[::-1]:
            return True
        else:
            return False