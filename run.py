#!/usr/bin/python3

import os, platform
if platform.system() == "Linux" or platform.system() == "Darwin":
    os.environ["KIVY_VIDEO"] = "ffpyplayer"
    
from pysimbotlib.core import PySimbotApp, Robot
from kivy.logger import Logger
from kivy.config import Config
# Force the program to show user's log only for "info" level or more. The info log will be disabled.
Config.set('kivy', 'log_level', 'info')

import random

# update robot every 0.5 seconds (2 frames per sec)
REFRESH_INTERVAL = 1/2


class RandomWalkRobot(Robot):
    
    def update(self):
        self.turn(self.smell())
        while True:
            IR = self.distance()
            print(IR[0])
            if IR[0] <= 20:
                IR = self.distance()
                self.turn(-2)
            elif IR[1] <= 20:
                IR = self.distance()
                self.turn(-2)
            elif IR[7] <= 20:
                IR = self.distance()
                self.turn(2)
            else:
                self.move(2)
                break


if __name__ == '__main__':
    app = PySimbotApp(robot_cls=RandomWalkRobot, num_robots=1,interval=REFRESH_INTERVAL)
    app.run()