#!/usr/bin/python3
import os, platform
if platform.system() == "Linux" or platform.system() == "Darwin":
    os.environ["KIVY_VIDEO"] = "ffpyplayer"
    
from pysimbotlib.core import PySimbotApp, Robot
from kivy.logger import Logger
from kivy.config import Config

# Force the program to show user's log only for "info" level or more. The info log will be disabled.
Config.set('kivy', 'log_level', 'info')

# update robot every 0.5 seconds (2 frames per sec)
REFRESH_INTERVAL = 1/100

class SmartRobot(Robot):

    def update(self):
        if self.distance()[0] <= 15:
            if abs(self.distance()[1] - self.distance()[7]) < 5 :
                print("turning")
                print(self.smell_nearest())
                self.move(2)
                self.turn(-1)
            elif self.distance()[1] < self.distance()[7]:
                print("right1")
                print(self.smell_nearest())
                self.turn(-2)
            elif self.distance()[1] > self.distance()[7]:
                print("left1")
                print(self.smell_nearest())
                self.turn(2)
            else:
                if -1 <= self.smell() <= 1:
                    self.move(2)
                elif self.smell() < -1:
                    self.turn(-2)
                elif self.smell() > 1:
                    self.turn(2)
        elif abs(self.distance()[1] - self.distance()[7]) <5 and self.distance()[7] <= 20 and self.distance()[1] <= 20:
            self.turn(2)
            print("back")
            print(self.smell_nearest())
        elif self.distance()[7] <= 15:
            self.turn(2)
            print("left")
            print(self.smell_nearest())
        elif self.distance()[1] <= 15:
            self.turn(-2)
            print("right")
            print(self.smell_nearest())
        elif self.distance()[0] > 30 and self.distance()[7] > 30 and self.distance()[1] > 30 and self.distance()[6] > 30 and self.distance()[2] > 30:
            print("smell")
            if -1 <= self.smell() <= 1:
                    self.move(2)
            elif self.smell() < -1:
                    self.turn(-2)
            elif self.smell() > 1:
                    self.turn(2)    
        else:
            self.move(2)
            print(self.smell_nearest())

if __name__ == '__main__':
    app = PySimbotApp(robot_cls=SmartRobot, num_robots=1,interval=REFRESH_INTERVAL)
    app.run()