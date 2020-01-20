# -*- coding: utf-8 -*-
"""
Author : Jeanne Morin

AI Assigment
"""

def logic():
    Stat= []
    Stat.append(("I",[1,2]))
    Stat.append(("Good",[]))
    Stat.append(("Human Being",[3]))
    Stat.append(("Love Graders",[]))
    Stat.append(("Good Graders", [2,5]))
    Stat.append(("Study Well",[]))
    
    print("Does every humans study well ?\n")
    subject = "Human Being"
    link = "Study Well"
    
    for i in range (len(Stat)):
        if Stat[i][0] == subject:
            for j in Stat[i][1]:
                if Stat[j][0]== link:
                    return True
            return False
            break