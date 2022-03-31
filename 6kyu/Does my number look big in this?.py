def narcissistic( value ):
    s_value = str(value)
    a = 0
    for n in s_value:
        a+=pow(int(n),len(s_value))
    return a == value
