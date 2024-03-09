# This is a Collatz Conjecture program;
# No matter the input number it will always become 1.
number = int(input('Enter a number: '))
hops = 0
while number != 1:
    print('-> ', number)
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    hops = hops + 1
print('-> ', number)
print('>> hops: ', hops)