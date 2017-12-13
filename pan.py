#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import os
import sys
import random

curpath = os.path.abspath('.')
badnamefile = curpath+'/bad_names.txt'
goodnamefile = curpath+'/good_names.txt'
goodwordfile = curpath+'/good_words.txt'
badnames = []
goodnames = []
goodwords = []

def read_file(file):
    tmp = []
    with open(file,'r') as f:
        tmp = f.read()
        tmp = tmp.split(',')
        tmp.pop()
    return tmp

def write_file(file,str):
    with open(file,'a') as f:
        f.write(str)

def pick_name():
    n = 1
    names = []
    goodwords = []
    goodnames = []
    badnames = []
    
    goodwords = read_file(goodwordfile)
    goodnames = read_file(goodnamefile)
    badnames = read_file(badnamefile)
    
    while n < 20:
        n = n + 1
        name = goodwords[random.randint(0,len(goodwords)-1)] + goodwords[random.randint(0,len(goodwords)-1)]
        if len(sys.argv) > 1:
            first = sys.argv[1]
        else:
            first = ""
        if 'j' == first:
            if name not in badnames:
                print("===============")
                print(name)
                print("\n好听y 一般i 难听n")
                judge = input("请输入：")
                print("")
                if judge == 'y':
                    write_file(goodnamefile,name+',')
                elif judge == 'n':
                    write_file(badnamefile,name+',')
                else:
                    pass
                names.append(name) 
        else:
            print(name)


if __name__ == "__main__":
    pick_name()


