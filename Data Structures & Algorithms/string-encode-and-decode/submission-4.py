class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded =''
        for i in range(len(strs)) :
            encoded += strs[i] + '<'
        return encoded

    def decode(self, s: str) -> List[str]:
        L = []
        temp =''
        for char in s : 
            if char != '<':
                temp += char
            if char == '<':
                L.append(temp)
                temp = ''
        return L