 #!/usr/bin/env python
import rospy
from std_msgs.msg import String
from test_package_2.simp_sub2 import COMP2

class COMP1:
    def __init__(self) -> None:
        self.hello_str = ''
        rospy.init_node('listener1', anonymous=True)
        rospy.Subscriber("chatter1", String, self.callback)

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        self.hello_str = data.data


    def printHello (self):
        rospy.loginfo(self.hello_str + " Function 1")

    def run(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.printHello()
            rate.sleep()

if __name__ == '__main__':
    c = COMP1()
    cp2 = COMP2()
    cp2.run()
    c.run()