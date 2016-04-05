#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from regulateur.msg  import reg

def talker():
    rrr= reg()
    rrr.pos0=12
    rrr.pos1=44
    rrr.cap=0
    rrr.obja0=0
    rrr.obja1=0
    rrr.objb0=0
    rrr.objb1 =0
    rrr.deltaMax=0.4
    pub = rospy.Publisher('/inputRegulateur', reg, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % reg.deltaMax
        rospy.loginfo(hello_str)
        pub.publish(rrr)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
