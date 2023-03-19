'''


Date: Mar 19, 2023.


Author :  Name: Sejin Yoon
          uID: u1311019


Source code File name: problem2.py


'''





value = float(input("Enter the Richter magnitude value: "))
if value >= 9.0:
    print('Cause unbelievable damage')
elif value >= 8.0:
    print('Cause major destruction')
elif value >= 7.0:
    print('Cause damage to most buildings')
elif value >= 6.0:
    print('Cause damage to well-built structures')
elif value >= 5.0:
    print('Cause damage to the poorly constructed building')
elif value >= 4.0:
    print('Damage done to weak buildings')
elif value >= 2.0:
    print('Very rarely causes damage')
elif value >= 1.0:
    print('Micro earthquakes not felt or rarely felt')
else:
    print('Wrong Input')
