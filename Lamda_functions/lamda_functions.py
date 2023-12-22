def appl(fx,value):
    return 6+fx(value)

double=lambda x:x*2
cube=lambda x:x*x*x
avg=lambda x,y,z:(x+y+z)/3


print(double(5))
print(cube(2))
print(avg(3,5,10))
print(appl(cube,2))
print(appl(lambda x:x*x,2))
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))