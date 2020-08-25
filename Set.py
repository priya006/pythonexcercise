# set removes duplicates Example set()

a = set('priya')
b = set('Raelyn')
print(a)
print(a-b) # letters in a but not in b

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

if __name__ == "__main__":
    pass