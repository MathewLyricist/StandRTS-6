from fnmatch import fnmatch

def find_numbers(mask, n):
    sp1 = []
    for num in range(1, 10**9 + 1):
        str_num = str(num)
        if fnmatch(str_num, mask):
            if num % n == 0:
                sp1.append(num // n)
    return sp1

mask = "5?0*4?4"
n = 789
sp1 = find_numbers(mask, n)
print(sp1)