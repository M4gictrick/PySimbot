#!/usr/bin/python3

import os, platform
if platform.system() == "Linux" or platform.system() == "Darwin":
    os.environ["KIVY_VIDEO"] = "ffpyplayer"

from pysimbotlib.core import PySimbotApp
from kivy.config import Config

# Force the program to show user's log only for "debug" level or more. The info log will be disabled.
Config.set('kivy', 'log_level', 'debug')

if __name__ == '__main__':
    app = PySimbotApp(enable_wasd_control=True)
    app.run()