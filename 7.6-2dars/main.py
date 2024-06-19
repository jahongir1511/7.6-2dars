def digitize(n):
    return [int(digit) for digit in str(n)]

print(digitize(123))
print(digitize(1))
print(digitize(8675309))
