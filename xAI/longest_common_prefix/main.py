def longest_common_prefix(l_s):
    if not l_s:
        return ""

    # Start with the first string as the running prefix
    prefix = list(l_s[0])

    for i in range(1, len(l_s)):
        current = list(l_s[i])
        aux = []

        # Compare the current string with the running prefix
        for j in range(min(len(prefix), len(current))):
            if prefix[j] == current[j]:
                aux.append(prefix[j])
            else:
                break  # As soon as mismatch occurs, break

        # Update the running prefix
        prefix = aux

        # Early exit: no common prefix
        if not prefix:
            return ""

    return "".join(prefix)


print(longest_common_prefix(["flower","flow","flight"]))  # → "fl"
#print(longest_common_prefix(["dog","racecar","car"])  )   # → ""
#print(longest_common_prefix(["interspecies", "interstellar", "interstate"]) ) # → "inters"
#print(longest_common_prefix(["a"]) ) # → "a"
#print(longest_common_prefix(["",""]) ) # → ""
