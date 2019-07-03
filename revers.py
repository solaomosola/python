def reversed_args(f):
    def reverseAction(*args):
        localArgs = []
        for arg in reversed(args):
            localArgs.append(arg)
        return f(*localArgs)
    return reverseAction

first = (i for i in range(10))


def numberGenerator(n):
    for i in range(n):
        yield(i)

for i in numberGenerator(3):
    print(i)