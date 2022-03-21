def digital_root(n):
    return digital_root(sum(list(map(int, list(str(n)))))) if len(str(n)) > 1 else int(n)
