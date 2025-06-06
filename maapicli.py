import os
if not os.path.exists("run_cli.py"):
    os.environ["MAAFW_BINARY_PATH"] = os.getcwd()

from assets.custom.action.Fishing import Fishing
from assets.custom.action.ShotTarget import ShotTarget
from assets.custom.action.ScreenShot import ScreenShot
from assets.custom.action.ShotSelf import ShotSelf
from assets.custom.action.StoryRogue import StoryRogue
from assets.custom.action.Count import Count

from maa.toolkit import Toolkit

import sys


print("如无必要，请使用MFW.exe运行")
print("if not necessary, please use MFW.exe to run")

def main():
    # 注册自定义动作
    Toolkit.pi_register_custom_action("Fishing", Fishing())
    Toolkit.pi_register_custom_action("ShotTarget", ShotTarget())
    Toolkit.pi_register_custom_action("ScreenShot", ScreenShot())
    Toolkit.pi_register_custom_action("ShotSelf", ShotSelf())
    Toolkit.pi_register_custom_action("StoryRogue", StoryRogue())
    Toolkit.pi_register_custom_action("Count", Count())

    # 注册自定义识别

    directly = "-d" in sys.argv
    Toolkit.pi_run_cli("./", "./", directly)


if __name__ == "__main__":
    main()
