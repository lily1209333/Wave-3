num = int(input("input an integer (2 or greater): "))
count = 0
f = 2
while f <= num:
    if num % f == 0:
        count += 1
        num = num / f
    else:
        f += 1
if count == 1:
    print("True")
else:
    print("False")
