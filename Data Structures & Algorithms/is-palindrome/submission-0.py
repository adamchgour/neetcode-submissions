class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse_s = ""
        clean_s = ""

        for i in range(len(s)):
            if s[len(s)-1-i].isalnum():
                reverse_s += s[len(s)-1-i].lower()
            if s[i].isalnum():
                clean_s += s[i].lower()

        return clean_s == reverse_s