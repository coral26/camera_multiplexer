#! /usr/bin/env python

import rospy
#import rosbag
#import datetime
from sensor_msgs.msg import Image

def callback (data):
    print data.header


def cam_multi_subscriber():
    rospy.init_node('cam_multi_subscriber', anonymous=False)
    rospy.Subscriber('/camera_multiplex', Image , callback)
    rospy.spin()

if __name__=='__main__':
    try:
        cam_multi_subscriber()
    except rospy.ROSInterruptException:
        pass
