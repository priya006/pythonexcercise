from math import pi
# More on list Example: []


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
countAppleIntheList = fruits.count('apple')
print('countAppleIntheList:', countAppleIntheList)

nextbanna = fruits.index('banana', 4)
print('nextbanna:', nextbanna)

pop = fruits.pop()
print(pop)

stack = [1, 2, 3]
stack.append(6)
print('stackappend:', stack)

# List Comprehensions
cubes = [x ** 3 for x in range(5)]
print('cubes:', cubes)

combs = []  # an empty set
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print('combs',combs)


#Adding if condition to exclude negative results
vec = [-4, -2, 0, 2, 4]
[x for x in vec if x >= 0]
print(abs(x))

i = 6
piValue = str(round(pi,i))
print('piValue', piValue)


if __name__ == "__main__":
    pass
