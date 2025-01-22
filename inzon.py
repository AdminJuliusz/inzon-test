import time
import random

down = "_"

player_name = input("enter a name: ")
print(f"welcome " + player_name + " to inzon")
player_look = input("enter how your player look")
print("let go " + player_name + player_look)
game_mode = input("muitplayer, singeplaer, storymode, /m/s/sm/")
if game_mode == "m":
    ip = input("enter a ip for the sever: ")
print("joining" + ip)
if game_mode == "s":
    pass
if game_mode == "sm":
    pass
for i in range(10):
    down
    