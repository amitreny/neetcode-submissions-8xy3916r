class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet={}
        left=0
        maxLength=0
        for right,char in enumerate(s):
            if char in charSet and charSet[char] >= left:
                left = charSet[char] + 1
            
            charSet[char]=right
            maxLength=max(maxLength,(right-left)+1)
        return maxLength