class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = "".join(char.lower() for char in s if char.isalnum())
        
        i = 0
        j = len(s) - 1

        print(s)

        while (i < j):
            if (s[i] != s[j]):
                return False
            i += 1
            j -= 1
        
        return True