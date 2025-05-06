# Example: Check if a number is positive, negative or zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(5))
print(n(-3))
print(n(0))

# Example: Perform addition and multiplication in a single line
calc = lambda x, y: (x + y, x * y)

res = calc(3, 4)
print(res)


# Example: Filter even numbers from a list
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x:x % 2 == 0, n)
print(list(even))


# Example: Double each number in a list
a = [6, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))