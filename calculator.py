def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
def power(a,b):
    c=a**b
    return c
print("""Enter your choice:
1.Add
2.Sub
3.Multiply
4.Divide
5.Power
""")
ch=int(input("Enter your choice:"))
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
if(ch==1):
    print(add(a,b))
elif(ch==2):
    print(sub(a,b))
elif(ch==3):
    print(mul(a,b))
elif(ch==4):
    print(div(a,b))
elif(ch==5):
    print(power(a,b))
else:
    print("Enter your correct choice")
