def longestCommonPrefix(strs: list[str]) -> str:
#    max = 0
    ans = ""

    sort_strs = sorted(strs)
    first = sort_strs[0]
    last = sort_strs[-1]

#    for x in strs:
#        if len(x) > max:
#            max = len(x)
#    
#    for y in range(max):
#        for z in range(y+1, max):
#            if strs[0][y:z] == strs[1][y:z] == strs[2][y:z] and z - y > len(ans):
#                ans = strs[0][y:z]

    for x in range(min(len(strs), len(last))):
        if(first[x] != last[x]):
            return ans
        ans += first[x]
    return ans
            


print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))