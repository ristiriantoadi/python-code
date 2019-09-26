x = "hello world"


def printSomething():
    global x
    x = "hello python"
    print(x)


printSomething()
print(x)
