#!/usr/bin/python3
from __future__ import annotations
import os, platform
if platform.system() == "Linux" or platform.system() == "Darwin":
    os.environ["KIVY_VIDEO"] = "ffpyplayer"
    
from pysimbotlib.core import PySimbotApp, Robot
from kivy.logger import Logger
from kivy.config import Config

from abc import ABC, abstractmethod

# Force the program to show user's log only for "info" level or more. The info log will be disabled.
Config.set('kivy', 'log_level', 'info')

import random

# update robot every 0.5 seconds (2 frames per sec)
REFRESH_INTERVAL = 1/10

class SmartRobot(Robot):

    _state = None

    def __init__(self, state: State) -> None:
        self.setSmartRobot(state)

    # method to change the state of the object
    def setSmartRobot(self, state: State):

        self._state = state
        self._state.robot = self

    def presentState(self):
        print(f"Robot is in {type(self._state).__name__}")

    # the methods for executing the elevator functionality. These depends on the current state of the object.
    def moving(self):
        self._state.moving()

    def passing(self):
        self._state.passing()

    def update(self):
        if 0 <= self.smell_nearest() <= 40:
            if self.distance()[0] <= 20:
                print("turning")
                if self.distance()[1] <= 15:
                    self.turn(-2)
                elif self.distance()[7] <= 15:
                    self.turn(2)
            elif self.distance()[1] <= 10:
                print(self.distance()[1])
                self.turn(-2)
                print("right")
                print(self.distance()[1])
            elif self.distance()[7] <= 10:
                print(self.distance()[7])
                self.turn(2)
                print("left")
                print(self.distance()[7])
            else:
                self.move(2)
                print(self.smell_nearest())
        elif self.smell_nearest() < 0 and self.distance()[1] > 15 and self.distance()[7] > 15:
            self.turn(-2)
            print(self.smell_nearest())
        elif self.smell_nearest() > 40 and self.distance()[1] > 15 and self.distance()[7] > 15:
            self.turn(2)
            print(self.smell_nearest())
        else:
            self.move(2)
            print(self.smell_nearest())

class State(ABC):
    @property
    def robot(self) -> SmartRobot:
        return self._robot

    @robot.setter
    def robot(self, robot: SmartRobot) -> None:
        self._robot = robot

    @abstractmethod
    def moving(self) -> None:
        pass

    @abstractmethod
    def passing(self) -> None:
        pass


if __name__ == '__main__':
    app = PySimbotApp(robot_cls=SmartRobot, num_robots=1,interval=REFRESH_INTERVAL)
    app.run()