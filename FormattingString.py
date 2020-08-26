import math

# An expression goes into {} The String is prefixed by f or F
print(f'The value of pi is {math.pi:.1f}')
print(F'The value of pi is {math.pi:.1f}')

# Dictionary Datastructure

table = {'priya': 1234, 'Raleyn': 23343, 'Deblyn': 3453534535}
# the number specified after : is used for line up the columns
for name, number in table.items():
    # print(table.items())
    print(f'{name:100} ==> {number:10}')

animals = "eels"
print(f'The animal is {animals}')
print(f'The animal is !a {animals !a}')
print(f'The animal is !r {animals !r}')
print(f'The animal is !s {animals !s}')

# keyword arguments [kwargs] formatting

print('{food} is {type}!'.format(food='priya',type='cool'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}

print('Sjoerd: {Sjoerd:d} '.format(**table))

for x in range(1,5):
    # 0,1,2 determines the position in format()
    print('{0:d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

if __name__ == "__main__":
    pass
