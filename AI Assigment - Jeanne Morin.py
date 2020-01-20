# -*- coding: utf-8 -*-
"""
Author : Jeanne Morin

AI Assigment
"""

# simple DFS with adjacency lists for representing graph
def __dfs(S, x, M, link):
    M[x] = True    
    for y in S[x][1]:
        if not M[y]:
           if S[y][0]== link:
               print("Yes\n")     
               return True
               
           else:
            __dfs(S, y, M, link) 
            
    return False 

# Build the knowledge representation, here a graph
def graph_construct(Stat):
    Stat.append(("I",[1,2]))
    Stat.append(("Good",[]))
    Stat.append(("Human Being",[3]))
    Stat.append(("Love Graders",[]))
    Stat.append(("Good Graders", [2,5]))
    Stat.append(("Study Well",[]))
 
#Answer the query "Does every human study well?" with the statements known
def logic():
    Stat= []
    graph_construct(Stat)  
    print("Does every human study well ?\n")
    subject = "Human Being"
    link = "Study Well"
    
    M = [False]*6
        
    for i in range (len(Stat)):
        if Stat[i][0] == subject:
            is_true= __dfs(Stat, i, M, link)
            
            if(is_true):
                print("Yes\n")
            else:
                print("No\n")
            break
            
            

         
