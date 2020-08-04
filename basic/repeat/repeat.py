#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: repeat <times> <cmd>")
        exit(-1)
    else:
        repeat_times = int(sys.argv[1])

    cmd = '''curl -k -X POST -H "X-User-Token: `dlim config -t -u Admin -x Admin`"  -F "file=@/tmp/pingpong.tgz" http://172.18.0.2:32747/dlim/v1/deployment/model/pingpong'''
    
    #for item in sys.argv[2:]:
    #    cmd += " "
    #    cmd += item 

    for i in range(repeat_times):
        os.system(cmd)

