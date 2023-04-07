
import time as t
from ctypes import *
import random
import time
dd_dll = windll.LoadLibrary('./DD94687.64.dll')
st = dd_dll.DD_btn(0) #classdd 초기설정


for i in range(1,22200):
    dd_dll.DD_key(501,1)
    time.sleep(0.04+random.random()*0.07)
    dd_dll.DD_key(502,1)
    time.sleep(0.12+random.random()*0.38)
    dd_dll.DD_key(502,2)
    time.sleep(0.04+random.random()*0.07)
    dd_dll.DD_key(501,1)    
