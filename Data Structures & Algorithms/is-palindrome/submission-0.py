class Solution:
    def isPalindrome(self, s: str) -> bool:
        text_normalized = "".join([char for char in s if char.isalnum()]).lower()
        
        if text_normalized == text_normalized[::-1]:
            return True
        return False