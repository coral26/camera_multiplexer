#! /usr/bin/env python

import rospy
#import rosbag
#import datetime
from sensor_msgs.msg import Image


class Camera_Multiplexer:


    def callback_1(self,data):
        self.camera_1 = data
        self.cam1_hasdata = True

    def callback_2(self,data):
        self.camera_2 = data
        self.cam2_hasdata = True

    def callback_3(self,data):
        self.camera_3 = data
        self.cam3_hasdata = True

    def callback_4(self,data):
        self.camera_4 = data
        self.cam4_hasdata = True

    def callback_5(self,data):
        self.camera_5 = data
        self.cam5_hasdata = True

    def publisher(self,camera):
        #print camera.header
        '''self.cam_multi.header = camera.header
        self.cam_multi.height = camera.height
        self.cam_multi.width = camera.width
        self.cam_multi.encoding = camera.encoding
        self.cam_multi.is_bigedian = camera.is_bigedian
        self.cam_multi.step = camera.step
        self.cam_multi.data = camera.data'''

        #rospy.loginfo(camera)
        self.pub.publish(camera)
        self.rate.sleep()

    def camera_multiplexer(self):
        if self.cam1_hasdata:
            self.publisher(self.camera_1)
            #print self.camera_1.header
            self.cam1_hasdata = False

        rospy.sleep(0.01)

        if self.cam2_hasdata:
            self.publisher(self.camera_2)
            #print self.camera_2.header
            self.cam2_hasdata = False

        rospy.sleep(0.01)

        if self.cam3_hasdata:
            self.publisher(self.camera_3)
            #print self.camera_3.header
            self.cam3_hasdata = False

        '''rospy.sleep(0.01)

        if self.cam4_hasdata:
            self.publisher(self.camera_4)
            #print self.camera_4.header
            self.cam4_hasdata = False'''

        rospy.sleep(0.01)

        if self.cam5_hasdata:
            self.publisher(self.camera_5)
            #print self.camera_5.header
            self.cam5_hasdata = False

        rospy.sleep(0.01)
	    
    def __init__(self):
        rospy.init_node('camera_multiplexer', anonymous=False)
        self.camera_1 = Image()
        self.camera_2 = Image()
        self.camera_3 = Image()
        self.camera_4 = Image()
        self.camera_5 = Image()
        self.cam_multi = Image()

        self.cam1_hasdata = False
        self.cam2_hasdata = False
        self.cam3_hasdata = False
        self.cam4_hasdata = False
        self.cam5_hasdata = False

        rospy.Subscriber('/camera_1/image_raw',Image,self.callback_1)
        rospy.Subscriber('/camera_2/image_raw',Image,self.callback_2)
        rospy.Subscriber('/camera_3/image_raw',Image,self.callback_3)
        #rospy.Subscriber('/camera_4/image_raw',Image,self.callback_4) 
        rospy.Subscriber('/camera_5/image_raw',Image,self.callback_5)

        self.pub = rospy.Publisher('camera_multiplex', Image , queue_size=10)

        self.rate = rospy.Rate(5)



if __name__=='__main__':
    cam_mplx = Camera_Multiplexer()
    while not rospy.is_shutdown():
        try:
            cam_mplx.camera_multiplexer()
        except rospy.ROSInterruptException:
            pass


