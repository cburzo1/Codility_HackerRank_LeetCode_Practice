import re

def valid_ip(s):
    s2 = re.findall(r'[.]', s)

    print(s2)

    if len(s2) == 3:
        s3 = s.split(".")
        print(s3)
        for i in range(0, len(s3)):
            if s3[i] != "":
                if s3[i][0] == '0':
                    return "Neither"

                s4 = re.search(r'[a-zA-Z]', s3[i])
                if s4:
                    return "Neither"

                s3_i = int(s3[i])
                if s3_i < 0 or s3_i > 255:
                    return "Neither"
            else:
                return "Neither"

        return "ipv4"
    else:
        return "Neither"


print(valid_ip("100.1.2.255"))