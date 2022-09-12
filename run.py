import os, platform
if platform.system() == "Linux" or platform.system() == "Darwin":
    os.environ["KIVY_VIDEO"] = "ffpyplayer"

from pysimbotlib.core import PySimbotApp, Robot
from kivy.logger import Logger
from kivy.config import Config

from abc import ABC, abstractmethod

# Force the program to show user's log only for "info" level or more. The info log will be disabled.
Config.set('kivy', 'log_level', 'info')

# update robot every 0.5 seconds (2 frames per sec)
REFRESH_INTERVAL = 1/200


class RunRobot(Robot):
    def update(self):
        IR = self.distance()
        if IR[0] <= 15:
            self.move(-1)
            self.turn(-1)
            print("front obstacle")
            print(self.smell_nearest())
        elif IR[1] <= 15:
            print("left")
            self.turn(-1)
            print(self.smell_nearest())
        elif IR[7] <= 15:
            self.turn(1)
            print("right")
            print(self.smell_nearest())
        elif IR[0] >= 20 and IR[1] >= 20 and IR[7] >= 20 and IR[6] >= 20 and IR[2] >= 20:
            if -1 <= self.smell_nearest() <= 1:
                print("smell")
                self.move(3)
            elif self.smell_nearest() < -1:
                print("smell 1")
                self.turn(-2)
                print(self.smell_nearest())
            elif self.smell_nearest() > 1:
                print("smell 2")
                self.turn(2)
                print(self.smell_nearest())
        else:
            self.move(1)
            print(self.smell_nearest())
            print("walk")
        




if __name__ == '__main__':
    app = PySimbotApp(robot_cls=RunRobot, num_robots=1,interval=REFRESH_INTERVAL)
    app.run()