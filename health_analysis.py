import pandas as pd
import numpy as np

num = 1
print (num)

str = 'string'
print(str)

list = [1, 2, 3]
print(list)



dict = {
    'key': 'value',
    'states': ['New York', 'New Jersey', 'Connecticut'], 
    'nest_dict': {'nest1': 1, 'nest2':2}
}


def BP(x,y):
    diastolic = x - 120
    systolic = y - 80
    if diastolic > 0:
        print ('\nYour diastolic pressure is ', x, ' this is high')
    elif diastolic <=0:
        print ('\nYour diastolic pressure is ', x, ' this is good')
    
    if systolic > 0:
        print ('\nYour systolic pressure is ', y, 'this is high')
    elif diastolic <=0:
        print ('\nYour systolic pressure is ', y, 'this is good')

BP(120,80)
BP(160,120)


def BP2(x,y):
    if x >= 121:
        systolic = 'bad'
    else:
        systolic = 'good'

    if y >= 81:
        diastolic = 'bad'
    else:
        diastolic = 'good'
    output = [systolic, diastolic]
    return output 


sys_in = 120
dia_in = 80

bloodpressure = BP2(sys_in, dia_in)

print ('\nsystolic pressure is', sys_in) 
print ('analysis:', bloodpressure[0])
print ('\ndiastolic pressure is', dia_in) 
print ('analysis:', bloodpressure[1])