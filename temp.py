numbers = [10, 20, 30, 40, 50]

# 1. Off-by-one error (ArrayIndexOutOfBoundsException)
for i in range(len(numbers)):
    print(f"Number: {numbers[i]}")

# 2. NullPointerException
text = "hello"
if text:
    print(f"Text length: {len(text)}")

# 3. Infinite loop (logical bug)
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# 4. Division by zero
a = 10
b = 2
if b != 0:
    print(f"Result: {a / b}")

# 5. Wrong string comparison (logical bug)
s1 = "hello"
s2 = "hello"

if s1 == s2:
    print("Strings are equal")
else:
    print("Strings are NOT equal")
