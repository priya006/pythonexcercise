# kwarg = value

def parrot(voltage, state='Priya'):
    print(voltage, end=' ')

    print(parrot(1000))

    # unpack argument list


def UnpackingArgumentList(*args):
    output = range(*args)
    print(output)
    pass

# * unpacks the list and tuple
listInput = [3, 6,9]
UnpackingArgumentList(*listInput)

# Dictionaries with Keyword arguments with operator **




# not sure why this would fail
if __name__ == "__main__":
    pass
