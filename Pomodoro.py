import time

def countdown(pomo):
    pomo = 15
    while pomo:
            mins = pomo // 60
            secs = pomo % 60
            desplay = "{:02d}:{:02d}".format(mins, secs)
            print(desplay, end="\r")
            time.sleep(1)
            pomo -= 1
    
pomo = (input("Are you ready? "))

countdown(pomo)

def Pomodoro():
    print("Pomodoro start!")
    for i in range(4):
        pomo = 25*60
        while pomo:
            mins = pomo // 60
            secs = pomo % 60
            desplay = "{:02d}:{:02d}".format(mins, secs)
            print(desplay, end="\r")
            time.sleep(1)
            pomo -= 1
        print("5 min Break!")

        pomo = 5 *60
        while pomo:
            mins = pomo // 60
            secs = pomo % 60
            desplay = "{:02d}:{:02d}".format(mins, secs)
            print(desplay, end="\r")
            time.sleep(1)
            pomo -= 1
        print("Work again!")

Pomodoro()