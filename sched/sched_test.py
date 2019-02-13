import datetime
import time
import sched


def func1(string):
    print('now is: {:5f}'.format(time.time()), ' === ', string, ' (func 1)')

def func2(string):
    print('now is: {:5f}'.format(time.time()), ' === ', string, ' (func 2)')

def func3(string):
    print('now is: {:5f}'.format(time.time()), ' === ', string, ' (func 3)')

def main():

    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(0.04, 1, func1, ('good1', ))
    scheduler.enter(0.08, 2, func1, ('good2', ))
    scheduler.enter(0.12, 3, func2, ('good3', ))
    scheduler.enter(0.16, 4, func3, ('good4', ))
    scheduler.run()

if __name__ == '__main__':
    main()

