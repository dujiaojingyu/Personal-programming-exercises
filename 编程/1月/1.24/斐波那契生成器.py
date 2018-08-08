
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n += 1
    return 'lalalalal'

f = fib(10)

while True:
    try:
        x = next(f)
        print(x)
    except StopIteration as e:
        print('Generator return value is %s '%e.value)
        break

# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())