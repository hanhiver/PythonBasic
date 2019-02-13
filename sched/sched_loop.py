import datetime
import time
import sched

frame_index = 0

def func(scheduler, sched_time):
    global frame_index
    if frame_index < 99:
        scheduler.enter(0.04, 1, func, (scheduler, time.time(), ))
    frame_index += 1

    print('now is: {:5f}'.format(time.time() - sched_time), ' === ', frame_index, ' (func 1)')
    time.sleep(0.02)

    
def main():
    global frame_index
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(0.04, 1, func, (scheduler, time.time(), ))
    scheduler.run()

if __name__ == '__main__':
    main()

