a=int(input("give;"))
b=a
c=0
d=a*a
v=len(str(a))

e=d%(10**v)
f=d//(10**v)
c=e+f
    


if b==c:
    print(f"{c} is kaprekar")
else:
    print("not a kaprekar")