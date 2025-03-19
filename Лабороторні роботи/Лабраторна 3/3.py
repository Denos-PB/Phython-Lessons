def f(x):
    try:
        return int(1 / x)
    except TypeError:
        print(1, end="")
    else:
        print(2, end="")
        return 0
    finally:
        print(3, end="")

#a
try:
    print(f(0), end="")
    print(f(1), end="")
except:
    print(4, end="\n")
#b
try:
    print(f(0) or f(1), end="")
    print(3, end="")
except:
    print(4, end="\n")
#в
try:
    print(f(1) or f(0), end="")
    print(3, end="")
except:
    print(4, end="\n")