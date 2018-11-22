# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pylab
#import csv
import math

pylab.figure(figsize=(16,8))

"""PARAMETERS"""
total_games = 100000
#koyaku
ko = 9.2 #小役確率
ko_mai = 9 #小役枚数
ko_kaku = 0
#cherry
ch = 47.1
ch_mai = 4
ch_kaku = 0
#su
su = 42.6
su_mai = 12
su_kaku = 0
#bb
bb = 683 #bb prob
bb_mai = 348 #bb coins
bb_kaku = 0 
#rb
rb = 100 #rb
rb_mai = 102
rb_kaku = 0
#rep
rep, rep_kaku = 7.3,0

#we should count bonus
bbs,rbs = 0,0
#hosii nara kikai wari wo irero
wari = 0
#ransu no bunbo
bunbo = 65535
"""KOKOMADE"""

g,c,r = 0,0,0

"""for graph"""
x = np.arange(0,total_games)
y = np.zeros(total_games,"float32")

"""some slot parameters"""
def sazan_C():
    global ko,ko_mai,ch,ch_mai,su,su_mai,bb,bb_mai,rb,rb_mai,rep
    #koyaku
    ko = 9.2 #小役確率
    ko_mai = 9 #小役枚数
    
    #cherry
    ch = 47.1
    ch_mai = 4
    
    #su
    su = 42.6
    su_mai = 12
    
    #bb
    bb = 683 #bb prob
    bb_mai = 348 #bb coins
     
    #rb
    rb = 100 #rb
    rb_mai = 102
    #rep
    rep = 7.3
    
def my3_6():
    global ko,ko_mai,ch,ch_mai,su,su_mai,bb,bb_mai,rb,rb_mai,rep, wari
    #koyaku
    ko = 6.09 #小役確率
    ko_mai = 7 #小役枚数
    
    #cherry
    ch = 33.23
    ch_mai = 2
    
    #piero,bell
    su = 4096
    su_mai = 12
    #kobosi wo kami site koxnna mon yaro
    
    #bb
    bb = 240.9 #bb prob
    bb_mai = 312 #bb coins
     
    #rb
    rb = 240.9 #rb
    rb_mai = 104
    #rep
    rep = 7.3
    
    wari = 1.122

def funky_6():
    global ko,ko_mai,ch,ch_mai,su,su_mai,bb,bb_mai,rb,rb_mai,rep, wari #optional
    #koyaku
    ko = 6.09 #小役確率
    ko_mai = 7 #小役枚数
    
    #cherry
    ch = 33.51
    ch_mai = 2
    
    #piero,bell
    su = 4096
    su_mai = 12
    #kobosi wo kami site koxnna mon yaro
    
    #bb
    bb = 232.4 #bb prob
    bb_mai = 312 #bb coins
     
    #rb
    rb = 275.36 #rb
    rb_mai = 104
    #rep
    rep = 7.3
    
    wari = 1.11
    

"""determine how many random numbers will hits"""
def det_ran():
    global ko_kaku,bb_kaku,rb_kaku,rep_kaku,ch_kaku #mendokusai
    ko_kaku = bunbo // ko
    bb_kaku = math.ceil(bunbo // bb)#koituraha bunboga
    rb_kaku = math.ceil(bunbo // rb)#omoinode kiriage
    rep_kaku = bunbo // rep
    ch_kaku = bunbo //ch
    if su != 0:#koyaku zenbu ni yarubeki yakedo kuso mendokusai
        global su_kaku
        su_kaku = bunbo//su

"""lottery"""
def chusen():
    rd = np.random.randint(bunbo) #THIS GAME'S RNG
    
    if rd >=20000 and rd < 20000+ko_kaku:
        global g
        g +=1
        return ko_mai
    elif rd <bb_kaku:
        global bbs
        bbs += 1
        return bb_mai
    elif rd >=1000 and rd < 1000+rb_kaku:
        global rbs
        rbs += 1
        return rb_mai
    elif rd >= 2000 and rd < 2000 + rep_kaku:
        global r
        r+=1
        return 3
    elif rd >= 50000 and rd < 50000 + ch_kaku:
        global c
        c +=1
        return ch_mai
    elif rd >=40000 and rd < 40000+su_kaku:
        return su_mai
    else:
        return 0

"""kekka happyou"""
def result():
    """sukunai kaiten suu dato 0 de watte simau kara zenbu jouken bunki"""
    if bbs == 0:
        print(bbs)
    else:
        print(bbs,np.round(total_games/bbs,2))       
    if rbs == 0:
        print(rbs)
    else:    
        print(rbs,np.round(total_games/rbs,2))
    if g == 0:
        print(g)
    else:
        print(np.round(total_games/g,2))

    print("差枚",y[total_games-1])
    if wari != 0:
        print("期待値",total_games*3*(wari-1)//1)
""" cherry wo dasitakattara tukae
    if c == 0:
        print(c)
    else:
        print(np.round(total_games/c,2))
"""

"""nandemo kandemo method ni sitai syndrome"""
def kadou():
    for i in range(total_games):
        y[i] = chusen() -3 + y[i-1]

    

funky_6() #use methods required to enter parameters.
det_ran()
kadou()
result()
plt.plot(x,y)





#テンプレ
"""

def something():
    global ko,ko_mai,ch,ch_mai,su,su_mai,bb,bb_mai,rb,rb_mai,rep #, wari #optional
    #koyaku
    ko = 6.48 #小役確率
    ko_mai = 7 #小役枚数
    
    #cherry
    ch = 36.51
    ch_mai = 2
    
    #non_cherry rare yaku. su means suika
    su = 4096
    su_mai = 12
    #piero to bell de kobosi wo kami site koxnna mon yaro
    
    #bb
    bb = 240.9 #bb prob
    bb_mai = 312 #bb coins
     
    #rb
    rb = 240.9 #rb
    rb_mai = 104
    #rep
    rep = 7.3
    
    wari = 1.11
    
"""