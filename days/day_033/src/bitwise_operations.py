a = 11 #1011
b = 5  #0101
assert a & b == 1  #0001
assert a | b == 15 #1111
assert a ^ b == 14 #XOR 1110
assert ~a == -12 #-(1100)

a = a >> 1 #0101
b = b >> 1 #0010
assert a == 5
assert b == 2

a = a << 1 #1010
b = b << 1 #0100
assert a == 10
