def fibonacci(x):
    if x <= 1:
        if x == 1:
            return 1
        if x == 0:
            return 0
    else:
        y = fibonacci(x-1)
        z = fibonacci(x-2)
        print(str(x), str(x-1))
        print(str(x), str(x-2))
        print('-------------------')
        return (y + z)

numero=8
print("The fibonacci of", numero, "is", fibonacci(numero))
