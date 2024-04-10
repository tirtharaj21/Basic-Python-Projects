from playsound import playsound  
import time

new_var = "\033[2J"
CLEAR = new_var 
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed=0
    print(CLEAR)
    while time_elapsed <seconds:
        time.sleep(1)
        time_elapsed +=1

        time_left = seconds - time_elapsed
        minl=time_left//60
        secl=time_left % 60
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minl:02d}:{secl:02d}")
    playsound("Py_projectss/alarm.mp3")   

minutes=int(input("How many minutes to wait :"))
seconds=int(input("How many seconds to wait :"))
ts=minutes*60 +seconds
alarm(ts)