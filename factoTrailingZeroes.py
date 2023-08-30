
def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n-1)
    

def trailingFacto(num):
    str_num = str(num)
    zeroes = 0

    for i in str_num[::-1]:
        if i == "0":
            zeroes = zeroes + 1
        elif i != "0":
            break

    return zeroes


def trailingZeroes(number):
    count = 0
    i = 5

    while number//i != 0:
        count = count + int(number/i)
        i = i * 5
    return count


num = facto(10)
# print(num)
print(trailingFacto(num))
print(trailingZeroes(1000))
