# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 22:10:43 2023

@author: Admin
"""


sep = {
    "Naveen": "7.9",
    "Ram": "9.0",
    "Rakesh": "9.9",
    "Nayana": "7.8",
    "Rajesh": "7.4",
    "Niranjan": "9.0",
    "Dheeraj": "8.9",
    "Darshan": "8.0",
    "Rakshit": "8.8",
}
teac = {
    "Sreeku": "65%",
    "Raghavendra": "70%",
    "Rajshekar": "30%",
    "Anirudh": "90%",
    "Raju": "98%",
    "Praveen": "82%",
    "Niranjan": "100%"
}
pr1 = {
    'Vinay': {"Academic": 0.0, "Sports": 0.0, "Infrastructure": 0.0},
    'Rakesh': {"Academic": 0.0, "Sports": 0.0, "Infrastructure": 0.0},
    'Vasudendra': {"Academic": 0.0, "Sports": 0.0, "Infrastructure": 0.0},
    'Dinesh': {"Academic": 0.0, "Sports": 0.0, "Infrastructure": 0.0}
}

cour = {
    "CSE": ["JAVA", "PYTHON", "WEBDEVELOPING"],
    "ECE": ["NETWORK THEORY", "MICROCONTROLLER", "ADC"],
    "EEE": ["POWER ELECTRONIC", "NETWORK THEORY", "ECA"],
    "ME": ["FLUID MECHANICS", "THERMODYNAMICS", "COMPUTER GRAPHICS"]
}
sel = {}


def pr():
    print("{:<10} {:<10}".format("Name", "cgpa"))
    for x, y in sep.items():
        print("{:<10} {:<10}".format(x, y))


def tr():
    print("----Faculties Success rate---- ")
    print("{:<10} {:<10}".format("Name", "Pass percentage"))
    for x, y in sep.items():
        print("{:<10} {:<10}".format(x, y))


def cr():
    print("----College Courses---- ")
    print("{:<17} {:<17} {:<17} {:<17} ".format("courses", "S1", "S2", "S3"))
    for k, v in cour.items():
        S1, S2, S3 = v
        print("{:<17} {:<17} {:<17} {:<17} ".format(k, S1, S2, S3))
        
        
