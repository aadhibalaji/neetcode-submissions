class Solution:
    def countSubstrings(self, s: str) -> int:
        


        res = 0

        for i in range(len(s)):

            index = i

            #odd length
            l, r = index, index

            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                res += 1      
                l -= 1
                r += 1
        
            
            #even length
            l, r = index, index + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
               
                res += 1
                    
                l -= 1
                r += 1
    

        return res
