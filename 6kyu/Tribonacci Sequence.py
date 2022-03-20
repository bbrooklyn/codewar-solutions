def tribonacci(l, n):
    i = 0
    while i < n:
        l = l+[sum(l[i:])]
        i += 1
    return l[:-3]
