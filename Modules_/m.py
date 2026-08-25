# what is modules ? it is python files (.py) that contain s function , var , and classes , which can be resued in another program  by importing modules 
# note : single py files 
# user define modules and built in modules :
# 1. user define modules : we can create our own modules by writing code in a py file and then importing it in another py file
# 2. built in modules : python provides a lot of built in modules that we can use in our programs like math , random , datetime etc
# user define module 

import my_module
my_module.my_function()

# imprt specific part of code from modeule:

from my_module import person
print(person["name"])
print(person["age"])
print(person["city"])

import my_m as m 
stu1 = m.student(90, 80 ,95)
print(stu1.percentage)



# built inn modules :
import math 
print(math.sqrt(125))

import calendar
print(calendar.month(2024, 6))
print(calendar.isleap(2024))


import math
print(math.sqrt(16))
print(math.pi)

# Use:

# Scientific calculation

# ML formulas

# Statistics basics

import statistics
data = [1,2,3,4]
print(statistics.mean(data))


# Use:

# Basic data analysis

# Small dataset summary

import random
print(random.randint(1,10))
print(random.choice(["apple", "banana", "cherry"]))  # use : genrate random number and random elements etc 





import os
print(os.getcwd()) #  intract with operating system like files handing , dir handing  etc .


 # use like this :
# File path manage karna
# Folder banana
# Environment variable read karna
# Data science me dataset path handle karna


import sys
print(sys.version) #  intract with python interpreter in run time like command line arguments , python version etc .


# Use:

# Command line arguments
# sys.path check
# Exit program

import platform
print(platform.system())   # intract wiht system info . like OS name , version etc .

# import shutil
# shutil.copy("a.txt", "b.txt") #  intract with file handling like copy , move , delete files etc .


from datetime import datetime
print(datetime.now())


import time
time.sleep(2)



import json
data = {"name": "Ramesh"} # intract with json data \
print(json.dumps(data))

# Use:

# API response

# Config files

# ML model metadata

import csv # data handling like read and write csv files
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age"])
    writer.writerow(["Ramesh", 30])


import time  
print(dir (time ))



# https://docs.python.org/3/library/


# pakage : collection of modules /py files  + __init__.py file (empty file )  + sub pakage (optional )

# Library:   collection of pakage and modules that provide specific functionality like numpy , pandas , matplotlib etc
# inbuilt lib :
import math 
a=50
print(math.sqrt(a))

# import specific part of code from module :
from math import sqrt
b= 32 
print(sqrt(b))

from math import factorial
c= 20 
print(factorial(c))
    