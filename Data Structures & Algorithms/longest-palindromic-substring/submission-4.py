class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        resLen = 0

        for i in range(len(s)):

            index = i

            #odd length
            l, r = index, index

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if (r - l + 1 > resLen):
                        resLen = r - l + 1
                        res = s[l:r+1]
                    
                    l -= 1
                    r += 1
                else:
                    break
            
            #even length
            l, r = index, index + 1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if (r - l + 1 > resLen):
                        resLen = r - l + 1
                        res = s[l:r+1]
                    
                    l -= 1
                    r += 1
                else:
                    break

        return res
