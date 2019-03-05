def cut_cake(parts):
    try:
        return 1/int(parts)
    except (ZeroDivisionError, TypeError, ValueError):
        return "С ума посходили?"

f = cut_cake(input('число:'))
print(f)
f = cut_cake([1, 2, 3])
print(f)

def do_something(x):
    try:
        print(x)
    except:
        pass

x = 0
while x < 10:
    do_something(x)
    x += 1
