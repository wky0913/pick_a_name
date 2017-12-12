#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import random

n=1
names=[]
words=['柯','梳','禾','卉','婉','苗','棠','君','哲','琪','竹','美']
while n<30:
    n=n+1
    name=words[random.randint(0,len(words)-1)]+words[random.randint(0,len(words)-1)]
    names.append(name)
    print(name)
