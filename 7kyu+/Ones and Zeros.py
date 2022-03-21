def binary_array_to_number(arr):
    p = 1
    b = 0
    for n in reversed(arr):
        b+=p*n
        p = p*2
    return b
  
  # I was unaware of the int(base=2) method
