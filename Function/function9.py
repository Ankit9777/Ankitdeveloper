# no return value with argument
def factno(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	print("factorial=",f)
print("enter a number ")
no=int(input())
factno(no)