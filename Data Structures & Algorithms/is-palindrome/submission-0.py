class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS=re.sub(r'[^a-zA-Z0-9]','',s)
        stripS=cleanS.replace(" ","")
        stripS=stripS.lower()
        if stripS==stripS[::-1]:
            return True
        return False