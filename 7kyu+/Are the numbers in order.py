def in_asc_order(arr):
    p = 0
    for n in arr:
        if n < p:
            return False
        p = n
    return True
