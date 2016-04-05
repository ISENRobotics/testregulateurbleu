#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from regulateur.msg  import reg

def talker():
    phiNulaGauche = reg()
    phiNulaGauche.pos0=389444
    phiNulaGauche.pos1=5362681
    phiNulaGauche.cap=0
    phiNulaGauche.obja0=389456
    phiNulaGauche.obja1=5362629
    phiNulaGauche.objb0=389456
    phiNulaGauche.objb1=5362723
    phiNulaGauche.deltaMax=0.4

    phiNulaDroite = reg()
    phiNulaDroite.pos0=389464
    phiNulaDroite.pos1=5362685
    phiNulaDroite.cap=0
    phiNulaDroite.obja0=389456
    phiNulaDroite.obja1=5362629
    phiNulaDroite.objb0=389456
    phiNulaDroite.objb1=5362723
    phiNulaDroite.deltaMax=0.4

    phiPi_2aDroite = reg()
    phiPi_2aDroite.pos0=389367
    phiPi_2aDroite.pos1=5362744
    phiPi_2aDroite.cap=0
    phiPi_2aDroite.obja0=389456
    phiPi_2aDroite.obja1=5362723
    phiPi_2aDroite.objb0=389283
    phiPi_2aDroite.objb1=5362723
    phiPi_2aDroite.deltaMax=0.4

    phiPi_2aGauche = reg()
    phiPi_2aGauche.pos0=389364
    phiPi_2aGauche.pos1=5362716
    phiPi_2aGauche.cap=0
    phiPi_2aGauche.obja0=389456
    phiPi_2aGauche.obja1=5362723
    phiPi_2aGauche.objb0=389283
    phiPi_2aGauche.objb1=5362723
    phiPi_2aGauche.deltaMax=0.4

    phiMoinsPiaDroite = reg()
    phiMoinsPiaDroite.pos0=389272
    phiMoinsPiaDroite.pos1=5362688
    phiMoinsPiaDroite.cap=0
    phiMoinsPiaDroite.obja0=389283
    phiMoinsPiaDroite.obja1=5362723
    phiMoinsPiaDroite.objb0=389283
    phiMoinsPiaDroite.objb1=5362629
    phiMoinsPiaDroite.deltaMax=0.4

    phiMoinsPiaGauche = reg()
    phiMoinsPiaGauche.pos0=389292
    phiMoinsPiaGauche.pos1=5362693
    phiMoinsPiaGauche.cap=0
    phiMoinsPiaGauche.obja0=389283
    phiMoinsPiaGauche.obja1=5362723
    phiMoinsPiaGauche.objb0=389283
    phiMoinsPiaGauche.objb1=5362629
    phiMoinsPiaGauche.deltaMax=0.4

    phiMoinsPi_2aDroite = reg()
    phiMoinsPi_2aDroite.pos0=389390
    phiMoinsPi_2aDroite.pos1=5362617
    phiMoinsPi_2aDroite.cap=0
    phiMoinsPi_2aDroite.obja0=389283
    phiMoinsPi_2aDroite.obja1=5362629
    phiMoinsPi_2aDroite.objb0=389456
    phiMoinsPi_2aDroite.objb1=5362629
    phiMoinsPi_2aDroite.deltaMax=0.4

    phiMoinsPi_2aGauche = reg()
    phiMoinsPi_2aGauche.pos0=389387
    phiMoinsPi_2aGauche.pos1=5362643
    phiMoinsPi_2aGauche.cap=0
    phiMoinsPi_2aGauche.obja0=389283
    phiMoinsPi_2aGauche.obja1=5362629
    phiMoinsPi_2aGauche.objb0=389456
    phiMoinsPi_2aGauche.objb1=5362629
    phiMoinsPi_2aGauche.deltaMax=0.4

    pub = rospy.Publisher('/inputRegulateur', reg, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % reg.deltaMax
        rospy.loginfo(hello_str)
        # pub.publish(phiNulaGauche)
        # pub.publish(phiNulaDroite)
        # pub.publish(phiPi_2aGauche)
        # pub.publish(phiPi_2aDroite)
        pub.publish(phiMoinsPiaGauche)
        # pub.publish(phiMoinsPiaDroite)
        # pub.publish(phiMoinsPi_2aGauche)
        # pub.publish(phiMoinsPi_2aDroite)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
