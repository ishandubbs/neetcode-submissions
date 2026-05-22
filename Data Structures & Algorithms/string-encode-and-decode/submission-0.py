class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s 
            #returns length of string as str + a # sign
            #[neet, code, you] -> "4#neet4#code3#you"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while i < len(s):
            j = i #j = 0
            while s[j] != "#":
                j += 1 
                #if s[j] is not a #, we keep iterating until we get one:
                #in this case, j = 1
            length = int(s[i:j]) #length = int(s[0:1]) = int(s[0]) = 4
            i = j + 1 #i = 1 + 1 = 2
            j = i + length #j = 2 + 4 = 6
            decoded_string.append(s[i:j]) #s[2:6] = neet
            i = j #i = 6, and does the whole thing again
        return decoded_string
