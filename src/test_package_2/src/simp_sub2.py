 #!/usr/bin/env python
import rospy
from std_msgs.msg import String

class COMP2:
    def __init__(self) -> None:
        self.hello_str = ''
        rospy.init_node('listener2', anonymous=True)
        rospy.Subscriber("chatter2", String, self.callback1)
        rospy.Subscriber("chatter_f", String, self.callback2)

    def callback1(self, data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        self.hello_str = data.data

    def callback2(self, data):
        rospy.loginfo(rospy.get_caller_id() + "I heard f: %s", data.data)
        self.hello_str = data.data

    def printHello (self):
        rospy.loginfo(self.hello_str + " Function 2")

    def run(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.printHello()
            rate.sleep()

if __name__ == '__main__':
    c = COMP2()
    c.run()