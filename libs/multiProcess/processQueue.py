# -*- coding:utf-8 -*-
 
import multiprocessing
import time
 
def run(q, number):
    # 判断队列不为空
    while not q.empty():
        print('run_{0}:{1}'.format(number, q.get()))
        time.sleep(number)
 
if __name__ == '__main__':
    start = time.clock()
    # 创建队列
    manager = multiprocessing.Manager()
    q = manager.Queue()
 
    for i in range(100):
        q.put({'{}'.format(i): i})
 
    # 创建进程池
    pool = multiprocessing.Pool(5)
 
    pool.apply_async(run, (q, 0.1))
    pool.apply_async(run, (q, 0.2))
    pool.apply_async(run, (q, 0.3))
    pool.apply_async(run, (q, 0.4))
    pool.apply_async(run, (q, 0.5))
 
    pool.close()
    pool.join()
    end = time.clock()
    print('run_time：{0}'.format(end - start))


