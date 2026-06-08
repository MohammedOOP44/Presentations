import time 

class CountDouwnTime:
    def __init__(self,minutes,seconds):
        self.total_seconds = minutes * 60 + seconds

    def start(self):
        while self.total_seconds > 0 :
            min = self.total_seconds // 60
            sec = self.total_seconds % 60
            print(f"Time letf: {min:02d}:{sec:02d}")
            time.sleep(1)
            self.total_seconds -= 1
        print("Countdown finished!!") 

try :
    minn = int(input("enter the minutes: "))
    secc = int(input("enter the seconds: "))
    t = CountDouwnTime(minn,secc)
    t.start()

except ValueError:
    print("Invalid Input")









