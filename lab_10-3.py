# Auhtor: CMOB 3/1/2022

from email.encoders import encode_noop
import enum


lst = ["end","yay",10,'weeeeee',250,22.68,'maybe','this should be the start']
n_lst = []
for index, value in enumerate(lst):
    n_lst.insert(0,value)

print(n_lst)