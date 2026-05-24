import time 

class CounterdownTimer:
    def __init__(self,seconds):
        self.seconds = seconds 

    def start(self):
        while self.seconds > 0:
            seconds = self.seconds % 60
            minutes = self.seconds // 60
            print(f"{minutes:02d}:{seconds:02d}")
            time.sleep(1)
            self.seconds -= 1
        print("hell yeahhhhh")          

try :
    num = int(input("Enter number: "))
except ValueError:
    print("that wasn't a valid number")
countertimer = CounterdownTimer(num)
countertimer.start()

        