from lib.mBot import *
import NN
from sys import stdout

if __name__ == '__main__':

    def onDistance_1(dist1):
        #print("distance 1:",dist1)
        dist_1.append(dist1)

    def onDistance_2(dist2):
        #print("distance 2:",dist2)
        dist_2.append(dist2)	
    
    bot = mBot()
    bot.startWithSerial("COM15") or bot.startWithHID()
    
    classifier = NN.main()
    for count in range(10): # Initializing
        # first 10 times are filling the lists
        # to choose them correctly later.
        dist_1 = []
        dist_2 = []
        bot.requestUltrasonicSensor(1,1,onDistance_1)
        sleep(0.5)
        bot.requestUltrasonicSensor(2,3,onDistance_2)
        sleep(0.5)

    while(1):

        bot.requestUltrasonicSensor(1,1,onDistance_1)
        sleep(0.5)
        bot.requestUltrasonicSensor(2,3,onDistance_2)
        sleep(0.5)
        
        x1 = int(dist_1[0])
        x2 = int(dist_2[len(dist_2)-1])
        print("Distance 1: ", x1,)
        print("Distance 2: ", x2,)

        m1, m2 = NN.return_predicted(x1, x2, classifier)

        if x1 < 8: # too close
            m1 = 100
            m2 = 0
            bot.doMove(m1, m2)
        elif x2 < 8:
            m1 = 0
            m2 = 100
            bot.doMove(m1, m2)
        else:
            bot.doMove(m1, m2)
        try:
            pass
        except Exception,ex:
            print str(ex)
        #sleep(0.2)




