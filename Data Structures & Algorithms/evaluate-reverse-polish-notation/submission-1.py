class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        s = 0

        for token in tokens :
            if token not in "+-*/":
                num.append(int(token))
            else:
                b = num.pop()
                a = num.pop()

                if token == '+':
                    num.append(a+b)
                elif token == '-':
                    num.append(a-b)
                elif token == '*':
                    num.append(a*b)
                elif token == '/':
                    num.append(int(a/b))
        return num[-1]