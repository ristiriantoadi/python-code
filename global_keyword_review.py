x = "halo dunia"


def hello_world():
    global x
    x = "hello world"
    print(x)


hello_world()
print(x)
