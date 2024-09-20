# no return value with argument
# find the factorial
def factno(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
print("enter a number ")
no=int(input())
res=factno(no)
print("factorial=",res)