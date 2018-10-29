import subprocess
import os

def testudp(hostname = "google.com", count = 4):
    output1 = subprocess.check_output("ping -c {} {}".format(count,hostname), shell=True)

    y = output1.decode("utf-8").split('\n')[-2].split('/')
    min1 = float(y[3].split('=')[-1].replace(' ',''))
    avg  = float(y[4].replace(' ',''))
    max1 = float(y[5].replace(' ',''))

    dicio ={
        'min': min1,
        'avg': avg,
        'max': max1,
    }
    return dicio
