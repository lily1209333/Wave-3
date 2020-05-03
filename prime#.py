num = int(input("input an integer (2 or greater): "))
print("The prime factors of", num, "are:")
f = 2
while f <= num:
    if num % f == 0:
        print(f)
        num = num / f
    else:
        f += 1
