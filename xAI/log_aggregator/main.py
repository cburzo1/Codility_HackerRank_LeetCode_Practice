import datetime

def log_aggregator(l_s):
    dict_l = {}

    for i in range(len(l_s), -1, -1):
        for j in range(1, i):
            c1 = l_s[j]
            c2 = l_s[j - 1]
            dt_c1 = datetime.datetime.strptime(c1, "%Y-%m-%d %H:%M:%S " + c1[20:])
            dt_c2 = datetime.datetime.strptime(c2, "%Y-%m-%d %H:%M:%S " + c2[20:])

            if dt_c1 < dt_c2:
                temp = l_s[j]
                l_s[j] = l_s[j - 1]
                l_s[j - 1] = temp

    for i in range(len(l_s), -1, -1):
        for j in range(1, i):
            c1 = l_s[j].split(" ")
            c2 = l_s[j - 1].split(" ")

            if c1[2] < c2[2]:
                temp = l_s[j]
                l_s[j] = l_s[j - 1]
                l_s[j - 1] = temp

    #print(l_s)

    for i in range(0, len(l_s)):
        s = l_s[i].split(" ")
        if s[2] not in dict_l:
            dict_l[s[2]] = [l_s[i]]
        else:
            aa = dict_l.get(s[2])
            aa.append(l_s[i])
            dict_l.update({s[2]: aa})

    return dict_l

print(log_aggregator([
    "2025-08-14 09:12:45 AuthService User login successful",
    "2025-08-14 09:11:05 PaymentService Payment initiated",
    "2025-08-14 09:12:00 AuthService User logout",
    "2025-08-14 09:10:10 PaymentService Payment completed"
]
))

print(log_aggregator([
    "2025-08-14 09:12:45 AuthService Login",
    "2025-08-14 09:12:45 AuthService Logout",
    "2025-08-14 09:12:45 PaymentService Payment1",
    "2025-08-14 09:12:45 PaymentService Payment2"
]
))

print(log_aggregator([
    "2025-08-14 08:00:00 Auth Login",
    "2025-08-14 08:01:00 Auth Logout",
    "2025-08-14 08:02:00 Payment Start",
    "2025-08-14 08:03:00 Payment End"
]
))