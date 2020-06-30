import md5
import sys

while True:
	r=open("test.txt", "a")
	a=raw_input("password: ")
	w=md5.new(a)
	r.write(w.hexdigest()+'\n')
	r.close()
	
	if a=='exit':
		sys.exit()
