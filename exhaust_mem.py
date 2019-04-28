# -*- encoding:utf-8 -*-
# 薛师兄的内存溢出错误注入代码
import threading
import time
import logging
logging.basicConfig(level=logging.INFO)


# 注入 500mb 的内存
def exhaust_mem(num=500, unit='MB', duration=3000):
    if unit == 'MB':
        s = ' ' * (num * 1024 * 1024)
    else:
        s = ' ' * (num * 1024 * 1024 * 1024)
    time.sleep(duration)


# 注入 500mb 的内存泄漏
if __name__ == '__main__':
    try:
        threads = []
        thread_num = 1
        for i in range(0, thread_num):
            thread = threading.Thread(target=exhaust_mem, args=(500, 'MB',))
            threads.append(thread)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    except Exception as e:
        logging.exception(e)
        logging.CRITICAL("Error: unable to start thread")


