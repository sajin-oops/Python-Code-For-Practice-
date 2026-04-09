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
