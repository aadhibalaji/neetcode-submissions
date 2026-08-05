class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if (len(s1) > len(s2)):
            return False

        s1Map = {}
        s2Map = {}

        for i in range(len(s1)):
            s1Map[s1[i]] = s1Map.get(s1[i], 0) + 1

        l = 0
        r = len(s1) - 1
        tempL = l

        while r <= len(s2) - 1:
            
            while tempL <= r:
                s2Map[s2[tempL]] = s2Map.get(s2[tempL], 0) + 1
                tempL += 1
                
            
            print(s2Map)

            if (s1Map == s2Map):
                return True

            s2Map.clear()

            l += 1
            r += 1
            tempL = l

        return False

        