import pyautogui as pya
import os

def screen_shot(dir = r"/home/abdulmajed/Pictures/Screenshots") -> None:
    NAME = "screenshot{}.png"
    
    os.chdir(dir)
    ls = sorted([img for img in os.listdir(dir)
          if img.startswith("screenshot") and img.endswith(".png")])
    last_shot = len(ls)

    for (shot, index) in zip(ls, range(1, last_shot+1)):
        shot_num = shot.split("screenshot")[-1].split(".png")[0]

        if shot_num != index:
            print("Before:\n",ls,sep='')
            print(f"shot:{shot}, shot_num={shot_num}\tindex={index}")
            os.rename(shot, NAME.format(index))
            print("After:\n",ls,sep='')

    shot = pya.screenshot()
    name = NAME.format(last_shot + 1)
    print(f"name:{name}")
    shot.save(rf"{dir}/{name}")

screen_shot()
