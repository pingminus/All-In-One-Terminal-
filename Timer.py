#Timer.py

import time
class Timer:

    def runTimer(self):
        self.user_timer = int(input("Enter time in seconds"))
        for i in range(self.user_timer):
            print(i)
            time.sleep(1)
        print("Times up")



