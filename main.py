# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 14:32:06 2022

@author: HOME
"""


# secret message

file = open("sunrise.jpeg","a+")

#byte_data=file.read(10)

file.write("GOOD MORNING!!")

file.flush()

file.close()


file = open("sunrise.jpeg",'rb')

file.read()

file.close()


