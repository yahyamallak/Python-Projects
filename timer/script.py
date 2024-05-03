import time


def timer(seconds):

    minutes = int(seconds / 60)
    secondsLeft = seconds % 60
    hours = 0

    if minutes > 59 :
        hours = int(minutes / 60)
        minutes = minutes % 60 
    
    time.sleep(1)

    print(f'{hours:02d}:{minutes:02d}:{secondsLeft:02d}')

    minutes += hours * 60
    secondsLeft += minutes * 60
    
    if seconds == 0:
        return
    
    secondsLeft -= 1

    timer(secondsLeft)




timer(8000)