def func(a,b = []):
    b.append(a)
    return b

print(func(1))
func(2)
print(func(3))

'''
O/P

[1]
[1, 2, 3]

'''

gen = (x**2 for x in range(5) if x % 2 == 0)
for val in gen:
    print(val)

'''
O/P

0
4
16

'''

class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    pass

print(Dog().speak())
print(Cat().speak())


'''

O/P
Woof
...

'''


result = []
for i in range(3):
    result.append(lambda: i)

print([f() for f in result])

print(result)

# for i in range(3):
#     print(i)

'''
O/P

[2, 2, 2]
[<function <lambda> at 0x102f30790>, <function <lambda> at 0x102f309d0>, <function <lambda> at 0x102f30a60>]

'''

class A:
    def hello(self):
        return "A"
    
class B(A):
    def hello(self):
        return "B"

class C(A):
    def hello(self):
        return "C"
    
class D(B,C):
    pass

print(D().hello())
# print(D.__mro__)

'''
O/P

B

'''