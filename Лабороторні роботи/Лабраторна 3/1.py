#1
try:
 print (1, end="")
 print (1 / 0, end="")
 print (2, end="")
except Exception:
 print (3, end="")
except:
 print (4, end="")
else:
 print (5, end="")
finally:
 print (6, end="")

#4
print("\n----------")
try:
 print (1, end="")
 print (1 / 0, end="")
except ZeroDivisionError:
 print (3, end="")
except Exception:
 print (4, end="")
else:
 print (1 / 0, end="")
 print (5, end="")
finally:
 print (6, end="")

  #6
print("\n----------")
try:
 print (1, end="")
except ZeroDivisionError:
 print (2, end="")
except:
 print (3, end="")
else:
 print (4, end="")
finally:
 print (5, end="")

 #7
 print("\n----------")
try:
     print(1, end="")
     print (1 / 0, end="")
except ZeroDivisionError:
     print(3, end="")
except Exception:
 print(4, end="")
else:
 print(5, end="")
finally:
# print(2 / 0, end="")
 print(6, end="")

 #9
 print("\n----------")
try:
    print(1, end="")
    print(1 / 0, end="")
except ZeroDivisionError:
    print(2 / 0, end="")
    print(3, end="")
except Exception:
    print(4, end="")
else:
    print(5, end="")
finally:
    print(6, end="")

def f(x):
     return 1 / x

try:
    print(f(0), end="")
    print(1, end="")
except Exception:
     print(2, end="")
else:
     print(3, end="")
finally:
     print(4, end="")

#13
print("\n----------")
def f(x):
 try:
   print(int(1/x), end="")
 except:
     print (1, end="")
 else:
  print(2, end="")
  raise TypeError
 finally:
    print (3, end="")
 try:
    f(0)
    f(1)
 except:
    print (4, end="")

#17
print("\n----------")
def f(x):
 try:
  return int (1 / x)
 except:
  print (1, end="")
  return 0
 else:
   print (2, end="")
   return 1
 finally:
   print (3, end="")
   return 2
 try:
   print(f(1) and f(0), end="")
   print (3, end="")
 except:
  print (4, end="")