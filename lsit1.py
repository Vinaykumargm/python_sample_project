# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 12:02:03 2023

@author: Admin
"""
abd=[]
li={
        1:["Vinay",18,"M","789654321"],
        2:["Ram",18,"M","789654322"],
        3:["pooja",20,"F","789654323"],
        4:["rakesh",20,"M","789654324"],
        5:["Ananya",19,"F","789654325"],
        6:["SadieSink",18,"F","789654326"],
        7:["MilliBobbyBrown",20,"F","789654327"],
        8:["Hermione",19,"F","789654328"],
        9:["Niranjan",26,"M","789654329"],
        10:["Balaji",22,"M","789654310"],
        11:["Sameer",21,"M","789654311"],
        12:["Bharat",25,"M","789654312"],
        13:["EmmaWhatson",27,"F","789654313"],
        14:["Gibbs",24,"M","789654314"],
        15:["MadMax",30,"F","789654315"],
        16:["Uday",29,"M","789654316"],
        17:["Dinesh",35,"M","789654317"],
        18:["Naveen",20,"M","789654318"],
        19:["Darshan",24,"M","789654319"],
        20:["Dheeraj",22,"M","789654320"]
        }
def acc():
    print("{:<18} {:<10} {:<10} {:<10}".format("Name","age","male","AaadharNo"))
    for x,y in li.items():
        Name,age,male,AaadharNo=y
        print("{:<18} {:<10} {:<10} {:<10}".format(Name,age,male,AaadharNo))
