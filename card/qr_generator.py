import pyqrcode
import sys

def qrcode():
	q = pyqrcode.create('123456')
	q.png('m.png',scale=6)
	print('generated')

if __name__=='__main__':
	qrcode()
