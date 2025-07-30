def get_unique_string(id_l, un):
    i = 0
    tot = 0
    un_l = list(un)

    while i < len(un_l):
        tot += ord(un_l[i])
        i+= 1

    tot_s = str(tot)

    for i in range(0, len(id_l)):
        if tot_s == id_l[i]:
            if id_l[i][-2] == "-":
                inc = int(id_l[i][-1]) + 1
                inc_s = str(inc)
                strip_tot = tot_s[:-2]
                tot_s = strip_tot + "-" + inc_s
            else:
                tot_s = tot_s + "-1"

    return tot_s

#print(get_unique_string(["448", "448-1", "512"],"test"))
#print(get_unique_string(["100", "120"],"Hi"))
#print(get_unique_string(["177", "177-1", "177-2"], "Hi"))
#print(get_unique_string(["177"], "Hi"))
#print(get_unique_string([], "Hi"))
print(get_unique_string(["288", "288-1", "288-2"], "Hio")) # "296-3"
#print(get_unique_string(["320-9"], "Hik"))                # "320"
#print(get_unique_string(["320"], "Hik"))                  # "320-1"