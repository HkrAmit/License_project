from datetime import date

#Main Program
def insvalid():
	#Today Part
	tdy=str(date.today()).split('-')
	t=[]
	for i in tdy:
		t.append(int(i))
	#Data Part
	fl2=open('data.txt', 'r').read().split()[3].split(':')[1].split('-')
	d=[]
	for i in fl2:
		d.append(int(i))
	#Validation Part
	try:
		for i in range(3):
			if t[i]<d[i]:
				out="OK"
				break
			elif t[i]>d[i]:
				out="Expired"
				break
			elif t[i]==d[i]:
				continue
			else:
				out="Expired"
		if out=="OK":
			print("OK")
		else:
			print("Expired")
	except:
		 print("Your Card Will Expire Tomorrow")

#Card Input
card=input()

#User Checker
fl1=open('users.txt', 'r').read().split()
if card in fl1:
	print("Authorized")
	insvalid()
else:
	print("Unauthorized")
