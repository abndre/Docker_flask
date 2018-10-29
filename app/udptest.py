import subprocess
import os
import re
import sys

def testudp(hostname = "google.com", count = 4):
    output1 = subprocess.check_output("ping -c {} {}".format(count,hostname), shell=True)

    y = output1.decode("utf-8").split('\n')[-2].split('/')
    min1 = float(y[3].split('=')[-1].replace(' ',''))
    avg  = float(y[4].replace(' ',''))
    max1 = float(y[5].replace(' ',''))

    s = output1.decode("utf-8").split('\n')[-3]

    listpackets = [float(s) for s in re.findall(r'-?\d+\.?\d*', s)]

    dicio ={
        'min': min1,
        'avg': avg,
        'max': max1,
        'received': listpackets[1],
        'packelost' : listpackets[2],
        'time':listpackets[3],
        'hostname':hostname,
        'count':count
    }
    return dicio
