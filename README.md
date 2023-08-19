# health-analytics
this assignment as a primer for 504/507.

# the variable num is equal to the integer 1
num = 1 

# the variable str is equal to the string 'string'
str = 'string'

# 'list' is a list that contains the numbers 1, 2, and 3
list = [1, 2, 3]

# this is a dictionary that contains one key:value pair, a list, and a nested dictionary
dict = {
    'key': 'value',
    'states': ['New York', 'New Jersey', 'Connecticut'], 
    'nest_dict': {'nest1': 1, 'nest2':2}
}


# this function BP accepts two parameters and subtracts 120 and 80 from them respectively. 
# Depending on the difference, the function will print out a statement that states the blood pressure and if it is good or bad
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




# this function accepts two parameters. If the first parameter is greater than or equal to 121 the funciton will set systolic equal to bad, anything else will
# systolic equal to good. If the second parameter is greater than or equal to 81 the funciton will set systolic equal to bad, anything else will
# systolic equal to good. The function will then create a list 'output' with the values systolic and diastolic and return the values.

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


# this will return the value of the systolic and diastolic and analyze the values. 

bloodpressure = BP2(sys_in, dia_in)

print ('\nsystolic pressure is', sys_in) 
print ('analysis:', bloodpressure[0])
print ('\ndiastolic pressure is', dia_in) 
print ('analysis:', bloodpressure[1])
