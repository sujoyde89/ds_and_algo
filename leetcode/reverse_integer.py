# rem = num % 10
# num = num//10
# sum = sum * 10 + rem

def reverse_integer(x):
    sum = 0
    if x<0:
        is_positive = False
        x = -1 * x
    else:
        is_positive = True
    while x>0:
        rem = x%10
        x = x//10
        sum = sum * 10 + rem
    if is_positive==False:
        sum = -1 * sum
    if sum>-2**31 and sum<(2**31)-1:
        sum = sum
    else:
        sum=0
    return sum

num = 123
num = -123
num = 120
print (reverse_integer(num))