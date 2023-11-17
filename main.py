from pico2d import open_canvas, delay, close_canvas
import game_framework

import play_mode as start_mode
import os
os.chdir(os.path.dirname(__file__)) #폴더째로 가져오는 법을 알아서 이제 쓸모 없으나 추가함
open_canvas(1280, 1024)
game_framework.run(start_mode)
close_canvas()

