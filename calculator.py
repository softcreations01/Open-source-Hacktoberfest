

import math
print('''1) cube,
2)sphere,
3)cylinder, 
4)cone, 
5)cuboid  ''')
pi=math.pi
check =True 
#definging functions to find volume
#the input is  taken is by default considered as  string format so type conversion to int for using in further mathematical operation
def vol_cube():
    s = int(input('enter side  '))
    int(s)
    v_c = (s ** 3)
    return (v_c)
def vol_sphere():
    r_s = int(input('enter radius'))
    v_s = ((pi * 4 * r_s ** 3) / 3)
    return (v_s)
 
def vol_cylinder():
    r_cy = int(input('radius'))
    h_cy = int(input('height'))
    v_cy = (pi * r_cy ** 2 * h_cy)
    return (v_cy)
def vol_cone():
    r_co = int(input('radius  '))
    h_co = int(input('perpendicular height'))
    v_co = (pi * r_co ** 2 * h_co) / 3
    return (v_co)
def vol_cuboid():
    l = int(input('length'))
    b = int(input('breadthh'))
    h = int(input('length'))
    v_r = (l * b * h)
    return (v_r)
 
#function for printing the required volume as per users choice
def find():
    n=int(input('enter no. for finding the required volume'))
    if(n==1):
 
        print('volume is  '+str(vol_cube()))
    elif(n==2):
 
        print('volume is  '+str(vol_sphere()))
    elif(n==3):
 
        print('volume is  '+str(vol_cylinder()))
    elif(n==4):
 
        print('volume is  '+str(vol_cone()))
    elif(n==5):
 
        print('volume is  ' + str(vol_cuboid()))
    else:
        print("enter valid no.")
 
find()#function called once for 1st calculation
 
 
while( check==True):
    ask = input('do you want to continue?ans in yes or no')
    if (ask == "yes" or ask == "YES" ):#conditional for recalculation.
        find()
        check = True
 
    else:
        print('thanks for usimg tvical')
        check = False