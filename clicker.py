import pyautogui
import time
import os
import pydirectinput
import keyboard

pyautogui.PAUSE = 0

print("Press 's' to start playing.")
print("Once started press 'Ctrl + C' to quit.")
keyboard.wait('s')
tempo = input("Set tome for scan in seconds: ")
tempo = int(tempo)
#tempo = 2
print ("Starting in 2...")
time.sleep(2)


def storm_click():
    board = pyautogui.locateOnScreen('data/storm_click.png')
    board2 = pyautogui.locateOnScreen('data/storm_click_loading.png', confidence = 0.7)
    board3 = pyautogui.locateOnScreen('data/storm_click_loading2.png', confidence = 0.7)

    if board is not None:
        print("Activing Click Storm...")
        time.sleep(1)
        pyautogui.moveTo(board)
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()
    elif board2 or board3 is not None:
        print("Click Storm in loading...")
    else:
        print("Click Storm is not in display...")

def powersurge():
    board = pyautogui.locateOnScreen('data/powersurge.png')
    board2 = pyautogui.locateOnScreen('data/powersurge_loading.png', confidence = 0.7)
    board3 = pyautogui.locateOnScreen('data/powersurge_loading2.png', confidence = 0.7)

    if board is not None:
        print("Activing Powersurge...")
        time.sleep(1)
        pyautogui.moveTo(board)
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()
    elif board2 or board3 is not None:
        print("Powersurge in loading...")
    else:
        print("Powersurge is not in display...")

def lucky_strike():
    board = pyautogui.locateOnScreen('data/lucky_strikes.png')
    board2 = pyautogui.locateOnScreen('data/lucky_strikes_loading.png', confidence = 0.7)
    board3 = pyautogui.locateOnScreen('data/lucky_strikes_loading2.png', confidence = 0.7)

    if board is not None:
        print("Activing Lucky Strike...")
        time.sleep(1)
        pyautogui.moveTo(board)
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()
    elif board2 or board3 is not None:
        print("Lucky Strike in loading...")
    else:
        print("Lucky Strike is not in display...")

def metal_detector():
    board = pyautogui.locateOnScreen('data/metal_detector.png')
    board2 = pyautogui.locateOnScreen('data/metal_detector_loading.png', confidence = 0.7)
    board3 = pyautogui.locateOnScreen('data/metal_detector_loading2.png', confidence = 0.7)

    if board is not None:
        print("Activing Metal Detector...")
        time.sleep(1)
        pyautogui.moveTo(board)
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()
    elif board2 or board3 is not None:
        print("Metal Detector in loading...")
    else:
        print("Metal Detector is not in display...")

def golden_clicks():
    board = pyautogui.locateOnScreen('data/golden_clicks.png')
    board2 = pyautogui.locateOnScreen('data/golden_clicks_loading.png', confidence = 0.7)
    board3 = pyautogui.locateOnScreen('data/golden_clicks_loading2.png', confidence = 0.7)

    if board is not None:
        print("Activing Golden Clicks...")
        time.sleep(1)
        pyautogui.moveTo(board)
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()
    elif board2 or board3 is not None:
        print("Golden Clicks in loading...")
    else:
        print("Golden Clicks is not in display...")

def super_clicks():
    board = pyautogui.locateOnScreen('data/super_clicks.png')
    board2 = pyautogui.locateOnScreen('data/super_clicks_loading.png', confidence = 0.7)
    board3 = pyautogui.locateOnScreen('data/super_clicks_loading2.png', confidence = 0.7)

    if board is not None:
        print("Activing Super Clicks...")
        time.sleep(1)
        pyautogui.moveTo(board)
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()
    elif board2 or board3 is not None:
        print("Super Clicks in loading...")
    else:
        print("Super Clicks is not in display...")


if __name__ == "__main__":
    while True:
        storm_click()
        powersurge()
        lucky_strike()
        metal_detector()
        golden_clicks()
        super_clicks()
        time.sleep(2)
        os.system('cls||clear')
        print("Waiting {} seconds...".format(tempo))
        time.sleep(tempo)

