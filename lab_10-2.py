# Author: CMOB 3/1/2022

lst = [1,5,10,22,25,50,100,150,345,700,15]


for index, value in enumerate(lst):
    if value > 500:
        break
    elif value <= 500:
        if value % 5 == 0 and value <= 150:
            print(value)
