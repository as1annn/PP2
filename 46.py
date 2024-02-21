#Python Generator 
#Ex1
def squares_maker(n):
    for i in range(1, n + 1):
        yield i ** 2
n = int(input)
squares = squares_maker(n)
for square in squares:
    print(square)

    #Ex2
def even_numbers_string(n):
    return ','.join(str(i) for i in range(0, n + 1, 2))
n = int(input)
print(even_numbers_string(n))

#Ex3
def divisible_by_three_and_four(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            n = int(input)
divisible_numbers = divisible_by_three_and_four(n)
print(list(divisible_numbers))

#Ex4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = int(input)
b = int(input)
for square in squares(a, b):
    print(square)

#Ex 5
def down(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input)
for number in down(n):
    print(number)






