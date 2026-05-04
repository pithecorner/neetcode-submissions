class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False


"""
If both strings contain the EXACT same characters, return true, else false

Contstraints, s and t consist of lowercase english letters. No need to manipulate in order to get the same case



"""