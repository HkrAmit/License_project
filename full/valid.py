from datetime import date
import requests
# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)
# RELAIS_1_GPIO = 17
# GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)

#Main Program
car_no = 'agfrd'
base_url = 'http://localhost:8000/check/'
def check(scanned):
	url = base_url + scanned + '/' + car_no
	respns = requests.get(url).json()
	if respns['status'] == 'No':
		return "OFF"
	else:
		return "Start"
	# 	#Today Part
	# 	tdy=str(date.today()).split('-')

	# 	#print(tdy)
	# 	t=[]
	# 	for i in tdy:
	# 		t.append(int(i))

	# 	#Data Part
	# 	fl2=open('data.txt', 'r').read().split()[3].split(':')[1].split('-')

	# 	#print(fl2)
	# 	d=[]
	# 	for i in fl2:
	# 		d.append(int(i))

	# 	#Validation Part
	# 	try:
	# 		for i in range(3):
	# 			if t[i]<d[i]:
	# 				out="OK"
	# 				break
	# 			elif t[i]>d[i]:
	# 				out="Expired"
	# 				break
	# 			elif t[i]==d[i]:
	# 				continue
	# 			else:
	# 				out="Expired"
	# 		if out=="OK":
	# 			print("OK")
	# 			#GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
	# 		else:
	# 			print("Expired")
	# 			#GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
	# 	except:
	# 		 print("Your Card Will Expire Tomorrow")


	# #User Checker
	# fl1=open('users.txt', 'r').read().split()
	# if scanned in fl1:
	# 	print("Authorized")
	# 	insvalid()
	# else:
	# 	print("Unauthorized")


if __name__=="__main__":
	check()
