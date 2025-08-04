def longest_common_prefix(l_s):

    aux = []

    for i in range(0, len(l_s)):
        if len(l_s[i]) > len(aux):
            aux = l_s[i]

    print(aux)

    for i in range(0, len(l_s)):
        s_l = list(l_s[i])
        for j in range(0, len(s_l)):
            if s_l[j] not in au

print(longest_common_prefix(["flower","flow","flight"]))  # → "fl"
#print(longest_common_prefix(["dog","racecar","car"])  )   # → ""
#print(longest_common_prefix(["interspecies", "interstellar", "interstate"]) ) # → "inters"
#print(longest_common_prefix(["a"]) ) # → "a"
#print(longest_common_prefix(["",""]) ) # → ""
