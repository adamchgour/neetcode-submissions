class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(opened,closed,path):
            if opened == closed == n :
                result.append(path[:])
                return

            if opened < n:
                backtrack(opened + 1, closed, path + "(")

            if closed < opened:
                backtrack(opened,closed + 1,path + ")")

        backtrack(0,0,"")
        return result