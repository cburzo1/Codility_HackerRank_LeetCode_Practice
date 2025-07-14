'''
SET 1
🧩 1. First Unique Character in a String
Problem Statement:

Given a string s, return the index of the first non-repeating character in it. If there is no such character, return -1.

Constraints:

1 <= s.length <= 10^5

s consists of only lowercase English letters.
'''

def first_unique_character_in_a_string(s):
    dict_s = {}
    s_l = list(s)

    for i in range(0, len(s_l)):
        if s_l[i] not in dict_s:
            dict_s[s_l[i]] = 1
        else:
            dict_s.update({s_l[i]: dict_s.get(s_l[i]) + 1})

    for i in range(0, len(s_l)):
        if s_l[i] in dict_s and dict_s.get(s_l[i]) == 1:
            return i

    return -1

print(first_unique_character_in_a_string("loveleetcode"))
print(first_unique_character_in_a_string("leetcode"))
print(first_unique_character_in_a_string("aabb"))

'''
Main Take Aways: 
- Python concept: "if in" performs a linear search with "break" or return statement for lists, but
"if in" for sets and dicts, it runs a hash style look up, ex: hash[s[i]] == "x"

- understand dictionaries, their JSON-like structure, and their CRUD functionalities: .get(<key>), 
.update({<key>:<value>}), .pop(<key>), <dict>[<key>] = <value>, for <obj> in <obj_list>: <key_set> = <dict>.keys(), 
<key_values> = <dict>.values()

- Dictionaries Preserve Insertion Order (Python 3.7+)
for k in dict: iterates in insertion order — helpful for logic relying on order (e.g. “first unique character”).

But don't depend on this for sorting — it’s insertion, not value-based.

- Avoid Modifying Dicts While Iterating Over Them
Doing so can cause runtime errors or unexpected behavior.

'''