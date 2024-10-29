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
    iv = False

    for letter in s:
        string += letter

    for x in range(len(string), len(string)-1):
        print(string[x:x+1])
        if string[x] + string[x+1] == "IV":
            iv = True
        
    print(iv)

    for x in range(len(string)):
        if iv == True:
            if string[x] == "I":
                int -= roman[string[x]]
            else:
                int += roman[string[x]]
        else:
            int += roman[string[x]]
    

    return(int)

print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("VI"))