class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        dictionary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        for i, c in enumerate(s):
            if i == 0:
                num += dictionary[c]
            elif dictionary[s[i]] >  dictionary[s[i - 1]]:
                num -= 2 * dictionary[s[i-1]]
                num += dictionary[c]
            else:
                num += dictionary[c]
                
        return num
    
solution_instance = Solution()
result = solution_instance.romanToInt("MCM")
print(result)

        