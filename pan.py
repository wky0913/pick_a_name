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

def generate_names():
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
        print(name)

def filter_names():
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
        if name not in badnames:
            print("*******************")
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

def pick_name():
    while True:
        print("\n========================")
        print("请选择模式：")
        print("    a-列出所有好听的名字")
        print("    b-列出所有不好听的名字")
        print("    c-随机生成名字")
        print("    d-筛选名字")
        print("    q-退出")
        mode = input("\n请选择：")
        if mode == "a":
            goodnames = read_file(goodnamefile)
            for name in goodnames:
                print(name)
        elif mode == "b":
            badnames = read_file(badnamefile)
            for name in badnames:
                print(name)
        elif mode == "c":
            generate_names()
        elif mode == "d":
            filter_names()
        elif mode == "q":
            break
        else:
            pass

if __name__ == "__main__":
    pick_name()


