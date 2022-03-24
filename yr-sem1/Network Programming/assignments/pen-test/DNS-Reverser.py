import re
import os
import sys
import time
from multiprocessing import Queue
import threading
from subprocess import Popen, PIPE

mutex = threading.Lock()

def ping_scan(ip):
    if os.name == "nt":
        try:
            p=Popen('ping -n 1 ' + ip, stdout=PIPE)
        except:
            sys.exit("[*] Can't ping")
        if p.stdout.read().find("TTL") != -1: return True
    else:
        try:
            p=Popen(['ping','-c 1',ip], stdout=PIPE, stderr=PIPE)
            print("runnning")
        except:
            sys.exit("[*] Can't ping")
        if p.stdout.read().find("1 received") != -1: return True
    return False

def start():
    while not q.empty():
        try:
            ip = q.get(True, 1)
            if ping_scan(ip):
                mutex.acquire()
                print( "[+] %s is up"%(ip))
                mutex.release()
        except:
            pass
        finally:
            q.task_done()

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        sys.exit("[*] Usage: %s IP [-A] [thread]"%(sys.argv[0]))
    try:
        t1 = time.time()
        thread_num = int(sys.argv[-1]) if sys.argv[-1].isdigit() else int(sys.argv[-2]) if sys.argv[-2].isdigit() else 200

        ip = sys.argv[1]
        if len(ip.split(".")) != 4: sys.exit("[*] Usage: %s IP [-A] [thread]"%(sys.argv[0]))
        for i in ip.split("."):
            if int(i) < 0 or int(i) > 255:
                sys.exit("[*] Usage: %s IP [-A] [thread]"%(sys.argv[0]))

        if sys.argv[-1] == "-A" or sys.argv[-2] == "-A":
            ip_start = ip.split(".")[0]
            ip_list1 = ["%s.%d.%d.1"%(ip_start, i, j) for i in range(256) for j in range(256)]
            ip_list2 = ["%s.%d.%d.254"%(ip_start, i, j) for i in range(256) for j in range(256)]
            ip_list = list(set(ip_list1+ip_list2))
            print( "[*] scan %s.0.0.0/8 with %d threads"%(ip_start, thread_num))
        else:
            ip_start = ".".join([ip.split(".")[0], ip.split(".")[1]])
            ip_list1 = ["%s.%d.1"%(ip_start, i) for i in range(256)]
            ip_list2 = ["%s.%d.254"%(ip_start, i) for i in range(256)]
            ip_list = list(set(ip_list1+ip_list2))
            print( "[*] scan %s.0.0/16 with %d threads"%(ip_start, thread_num))
        
        q = Queue.Queue()
        map(lambda x: q.put(x), ip_list)
        map(lambda x: x.start(), [threading.Thread(target=start) for i in range(thread_num)])
        q.join()
        sys.exit("[*] scan over in %ss"%(time.time() - t1))
    except Exception as e:
        sys.exit(e)