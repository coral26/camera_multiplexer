#! /usr/bin/env python

import rospy
#import rosbag
#import datetime
from sensor_msgs.msg import Image

def callback(data):
	print data.header
	#print
	#bag.write('/darknet_ros/bounding_boxes',data)

def camera_multiplexer():
	rospy.init_node('camera_multiplexer', anonymous=False)
	#global bag

	#timestamp = datetime.datetime.utcfromtimestamp(rospy.Time.now().to_time()).isoformat()
	#bag = rosbag.Bag('nodes/darknet_ros_'+('-'.join(timestamp.split(':')))+'.bag', 'w')

	rospy.Subscriber('/camera_1/image_raw',Image,callback)
	#cam_pub=rospy.Publisher('/camera_test', Image , queue_size=10)

        rospy.spin()

	#bag.close()




if __name__=='__main__':
	try:
		camera_multiplexer()
	except rospy.ROSInterruptException:
		pass


