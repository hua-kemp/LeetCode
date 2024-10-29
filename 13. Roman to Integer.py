def romanToInt(s: str) -> int:
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    string = []
    int = 0
    str_len = len(s)

    for letter in s:
        string += letter

    for x in range(str_len):
        if x != str_len-1:
            if string[x] + string[x+1] == "IV" or string[x] + string[x+1] == "IX":
                int -= roman[string[x]]
            elif string[x] + string[x+1] == "XL" or string[x] + string[x+1] == "XC":
                int -= roman[string[x]]
            elif string[x] + string[x+1] == "CD" or string[x] + string[x+1] == "CM":
                int -= roman[string[x]]
            else:
                int += roman[string[x]]
        else:
            int += roman[string[x]]

    return(int)

def romanToIntImp(s: str) -> int:
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    int = 0

    for x in range(len(s)):
        if x < len(s) - 1 and roman[s[x]] < roman[s[x+1]]:
            int -= roman[s[x]]
        else:
            int += roman[s[x]]

    return(int)

print(romanToIntImp("III"))
print(romanToIntImp("LVIII"))
print(romanToIntImp("MCMXCIV"))