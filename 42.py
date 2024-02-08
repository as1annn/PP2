#task1
def replace_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
#task2
def Fahrenheit(f):
    f -= 32
    c = (5 / 9) * f
    return c

#task3
def solve(numheads, numlegs):
    x = numheads * 2
    x -= numlegs
    x /= -2
    numheads -= x
    return numheads, x

#task4
def prime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return n

#task 5
from itertools import permutations

def permutations():
    text = input("Enter text: ")
    perms = permutations(text)
    for perm in perms:
        print(''.join(perm))

#task 6
def reversed(text):
    words = text.split()
    i = len(words) - 1
    while i >= 0:
        print(words[i], end=' ')
        i -= 1

#task 7
def has_33(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == 3:
            if nums[i+1] == 3:
                return True
        i += 1
    return False

#task 8
def spy(numbs):
    s = ''
    for i in numbs:
        s += i
    if '007' in s:
        return True
    return False

#task9
def radius(radius):
    sphere = 4/3*3.14*radius**3
    return sphere    

#task10
def unique(l):
    new_list = []
    i = 0
    while i < len(l):
        t_or_f = True
        j = 0
        while j < i:
            if l[i] == l[j]:
                t_or_f = False
            j += 1
        if t_or_f:
            new_list.append(l[i])
        i += 1
    return new_list


#task 11
def palindrome(text):
    i = 0
    j = len(text)-1
    while i < len(text)/2:
        if text[i] != text[j]:
            return 'No palindrome'
        i+=1
        j-=1

#task 12
def histogram(gist):
    i = 0
    while i < len(gist):
        j = 0
        while j < gist[i]:
            print('*', end='')
            j += 1
        print()
        i += 1

#task 13
def find_num_random(rand_num, count):
    count += 1
    num = int(input('Take a guess.\n'))
    if num == rand_num:
        print(f'Good job, KBTU! You guessed my number in {count} guesses!')
        return
    print('\nYour guess is too low.')
    return find_num_random(rand_num, count)


#Classes
#Ex1
class StringInputAndOutput:
    def __init__(self, str):
        self.str = str;

    def getString(self):
        return self.str;

    def printString(self):
        print(self.getString().upperCase());

#Ex2
class Shape:
    def __init__(self, length=0):
        self.length = length
        
    def area(self):
        return self.length

class Square(Shape):
    def __init__(self, length=0):
        super().__init__(length)

    def area(self):
        return self.length * self.length

shape = Shape(5)
print("shape:", shape.area())

square = Square(4)
print("square:", square.area())

#Ex 3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length
    
rectangl = Rectangle(4, 5)
print('rectangle: ', rectangl.area())

#Ex 4
import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'x={self.x}  y={self.y}')

    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def dist(self, other_point):
        return math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)
    

p1 = Point(2, 4)
p2 = Point(6, 8)

p1.show()
p2.show()

p1.move(3, 6)
p1.show()

print(f'dist: {p1.dist(p2)}')


#task5
class Bank:
    def __init__(self, money):
        self.balanc = money

    def balance(self):
        print(f'balance: {self.balanc}')

    def deposit(self, dep):
        self.balanc += dep
        print(f'deposit of {dep} successfully made. New balance: {self.balanc}')

    def withdraw(self, wit):
        if self.balanc < wit:
            print('insufficient funds!')
        
        else:
            self.balanc -= wit
            print(f'withdrawal of {wit} successfully made. New balance: {self.balanc}')


user = Bank(1000)

user.balance()
user.deposit(100)
user.balance()
user.withdraw(1200)
user.withdraw(1000)

        
#task6
class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, n):
        if n < 2:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    def filter_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_filter = PrimeFilter(numbers)
prime_numbers = prime_filter.filter_primes()

print("Prime numbers:", prime_numbers)

