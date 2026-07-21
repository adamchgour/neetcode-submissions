class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        r = True

        for elt in s:
            if elt == '(' or elt == '[' or elt == '{' :
                stack.append(elt)
                
            elif len(stack) == 0:
                return False

            elif elt == ')' and stack[-1] != '(' :
                return False
            elif elt == ']' and stack[-1] != '[' :
                return False
            elif elt == '}' and stack[-1] != '{' :
                return False
            
            else :
                stack.pop()

        if stack != [] :
            return False
        
        return r
