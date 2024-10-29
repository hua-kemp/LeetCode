def longestCommonPrefix(strs: list[str]) -> str:
    max = 0
    longest = ""

    for x in strs:
        if len(x) > max:
            max = len(x)
    
    for y in range(max):
        for z in range(y+1, max):
            if strs[0][y:z] == strs[1][y:z] == strs[2][y:z] and z - y > len(longest):
                longest = strs[0][y:z]

    return(longest)
            


longestCommonPrefix(["flower","flow","flight"])
longestCommonPrefix(["dog","racecar","car"])