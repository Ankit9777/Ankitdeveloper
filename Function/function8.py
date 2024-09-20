#no return value with argument
# check a number is even or odd
def check(no):
    if no%2==0:
        print("num is an even number")
    else:
        print("num is an odd number")
print("enter the value of num")
no=int(input())
check(no)