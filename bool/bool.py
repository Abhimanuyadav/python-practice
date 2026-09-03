# 25
num = int(input("Enter a number: "))

if num > 10 and num < 50:
    print("True")
else:
    print("False")

    # 26
num = int(input("Enter a number: "))

if num < 10 or num > 100:
    print("True")
else:
    print("False")


    # 27
num = 20

print(num > 10)
print(not (num > 10))

# 28
values = [0, 1, -5, "", "Python", False, True, None]

for value in values:
    print(repr(value), bool(value))


    # 29
print(bool(0))
print(bool(10))
print(bool(""))
print(bool("Hello"))
print(bool(None))


# 30
values = [0, 1, "", "Python", False, None]

for value in values:
    print("Value:", repr(value))
    print("Data type:", type(value))
    print("Boolean:", bool(value))
    print()
