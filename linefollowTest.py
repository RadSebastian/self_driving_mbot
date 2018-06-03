from lib.mBot import *

def onLineFollower(value):
	print "status = ",value
	
if __name__ == '__main__':
	bot = mBot()
	#bot.startWithSerial("COM15")
	bot.startWithHID()
	while(1):
		bot.requestLineFollower(1,2,onLineFollower)
		sleep(0.5)