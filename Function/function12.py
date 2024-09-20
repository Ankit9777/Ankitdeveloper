# return value with no argument
# find the factorial
def checkfact():
    print("enter a number")
    no=int(input())
    f=1
    while no>0:
        f=f*no
        no=no-1
    return f
res=checkfact()  # res is a variable
print("factorial=",res)
