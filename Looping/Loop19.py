#wap count no of odd and even digit
no=125
oc,ec=0,0
while no!=0:
	r=no%10
	if r%2==0:
		ec=ec+1
	else:
		oc=oc+1
	no=no//10
print("no of odd digit=",oc)
print("no of even digit=",ec)
print("the need for having amoung various stake holders of castel security was pointed out")