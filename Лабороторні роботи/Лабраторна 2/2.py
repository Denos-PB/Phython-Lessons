#a
def f1(a, b, c=3):
    pass
f1(1, b=1, c=3)
f1(1, b=2, c=1)
f1(1, b=1)
f1(1, 2)
f1(1, b=1)
f1(1, b=1)
f1(1, b=1)
f1(1, b=1, c=5)

#b
def f2(a, /, b, *, c=3, d=4):
    pass

f2(4, 5, d=5)
f2(4, 3, d=5)
f2(4, b=3, d=5)
f2(1, 2)
f2(1, 2, c=4)
f2(1, 2, d=4, c=5)