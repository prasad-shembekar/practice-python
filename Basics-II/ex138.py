def test(n):
    return int(bin(n)[::-1][:-2], 2)

n = 13
print("Original number: ", n);
print("Reverse the binary representation of the said integer and convert it into an integer:\n",test(n));
n = 145
print("Original number: ", n);
print("Reverse the binary representation of the said integer and convert it into an integer:\n",test(n));
n = 1342
print("Original number: ", n);
print("Reverse the binary representation of the said integer and convert it into an integer:\n",test(n));
