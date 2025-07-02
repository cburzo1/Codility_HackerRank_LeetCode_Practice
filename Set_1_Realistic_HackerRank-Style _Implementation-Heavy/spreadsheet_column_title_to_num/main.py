ch_dict = {
    "A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,
    "K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,
    "T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26
}

st = "ZZ"
st_r = st[::-1]

tot = 0

for i in range(len(st_r)):
    ch = st_r[i]
    if ch not in ch_dict:
        print("Character not in dict:", ch)
        break
    tot += ch_dict[ch] * (26 ** i)

print(tot)

'''
Main Take Aways: 
- Remember how to perform base n conversion to decimal and decimal to base. In this case its base 26 
  01 
("AB")sub(26) = (1 * 26^0) + (2 * 26^1), Where 1 is A and B is 2

- The trick to calculating this correctly is to reverse the string. If you dont, then for example: 
2 * 26^1 is calculated for 'B' in "AB" where it should be 2 * 26^0
'''