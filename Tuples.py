# Tuples are seperated by commas Example: (x, y)
t = 'hello!',123,234
print(t)
x, y ,z = t
print('assignment x y z', x,y,z)

v = ([1,2,3] , [3,2,1])
print(v)

# tuple must be parenthesized

tuple = [(x,x**2) for x in [1,2,3]]
print('tuple',tuple)
tuple.append((34,0))
print(tuple)



if __name__ == "__main__":
    pass