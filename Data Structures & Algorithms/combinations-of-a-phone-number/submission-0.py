class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        table = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        res = []
        combo = []
        def backtrack(i):
            
            if i >= len(digits):

                res.append("".join(combo))
                return

            for c in table[digits[i]]:
                combo.append(c)
                backtrack(i + 1)
                combo.pop()


        if digits:
            backtrack(0)

            
        return res
            