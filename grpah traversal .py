# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:17:59 2022

@author: 91838
"""
def all_paths(start,end,path=[]):
    print("yy")
    path=path+[start]
    if start==end:
        return path
    for i in graph[start]:
        if i  not in path:
            new_path=all_paths(i,end,path)
            for j in new_path:
                new_path.append(j)
        
    return new_path



