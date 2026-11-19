# SPDX-FileCopyrightText: 2026 Shuusuke Inomata
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)


def cb():
    msg = Person()
    msg.name = "猪股柊介"
    msg.age = 21
    pub.publish(msg)


def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)
