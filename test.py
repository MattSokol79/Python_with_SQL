def longest_time(h, m, s):
    hours_to_mins = h * 60
    s_to_min = s / 60

    if hours_to_mins > m and s_to_min:
        return h
    elif m > hours_to_mins and s_to_min:
        return m
    elif s_to_min > hours_to_mins and m:
        return s

print(longest_time(2, 300, 15000))