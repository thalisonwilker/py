#-*- coding:latin1 -*-

import os
def Ex(s):
    try: 
        x = input(s)
        return x
    except:
        pass
        
def Rn():
    os.system("clear")
    import random
    os.system("clear")
    i = random.randint(1,100)
    j = random.randint(1,100)
    k = random.randint(1,100)
    senha = str(i)+str(j)+str(k)
    t = 10
    os.system("clear")
    print '----------001 RANDOM PASSWORD 100---------- '
    print "A senha é composta e divida em três partes"
    print "Tente adivinhar cada parte, e em seguida digite-a para entrar!"
    print "Boa Sorte!"
    
    print "\nParte 1 "
    while 1:
        c = Ex("Chute um numero entre 1 e 100: ")
        if c == i :
            print "\nCorreto! voce ja tem a primeira parte da senha\n" 
            t = 10
            break
        else:
            t -= 1
            print "\nIncorreto\n"
            if c > i:
                print "tente um numero menor"
            elif c < i:
                print "tente um numero maior"
           
    print "\nParte 2 "     
    while 2:
        c = Ex("Chute um numero entre 1 e 100: ")
        if c == j :
            print "\nCorreto! agora voce tem duas partes!\n"
            break
        else:
            print "\nIncorreto\n"
            if c > j:
                print "tente um numero menor"
            elif c < j:
                print "tente um numero maior"
    
    print "\nParte 3 "       
    while 3:
        c = Ex("Chute um numero entre 1 e 100: ")
        if c == k :
            print "\nCorreto!\n"
            en = raw_input("Senha: ")
            if en == senha:
                print "CONGRATULATION!! VOCE E FODA!"
                break            
        else:
            print "Incorreto"
            if c > k:
                print "tente um numero menor"
            elif c < k:
                print "tente um numero maior"       
       
def LevelOne():
    os.system("clear")
    os.system("clear")
    print '---------- MATH LEVEL ONE -> EASY ---------- '
    import random
    x = random.randint(1,1000)
    y = random.randint(1,1000)
    str1 = "%d + %d = " % (x,y)
    z = Ex(str1)
    if z == ( x + y ):
        print "Suceful!"
        x = random.randint(1,1000)
        y = random.randint(1,1000)
        str1 = "%d - %d = " % (x,y)
        z = Ex(str1)
        if z == ( x - y):
            print "Suceful"
            x = random.randint(1,1000)
            y = random.randint(1,1000)
            str1 = "%d * %d = " % (x,y)
            z = Ex(str1)
            if z == ( x * y ):
                print "Suceful"
                x = random.randint(1,1000)
                y = random.randint(1,1000)
                str1 = "%d / %d = " % (x,y)
                z = Ex(str1)
                if z == ( x/y):
                    print "Congratulation! Finish!"
                    print "You is master in math!"
                else:
                    erro(1)
            else:
                erro(1)      	    
        else:
            erro(1)    	
    else:
        erro(1)
 
def erro(level):
    print "errado"
    s = raw_input("Try again ? <Yes> or <No>: ")
    if s == 'Y' or s == 'y' or s == "Yes" or s == "yes":
    	if level == 1:
    	    LevelOne()
    else:
        i = input("Return to menu ? 1--<Y> 2--<N> ")
        if i == 1:
            Menu()
        else:
            pass
    	    
def Mat(level):
    if level == 1:
        LevelOne()
        
def Menu():
    os.system("clear")
    print "---------- MENU ----------"
    print " 1 - RANDOM PASSWORD "
    print " 2 - MATH "
    op = input(">>> ")
    if op == 1:
        Rn()
    elif op == 2:
        op = input("1 - Level One -> Easy\n2 - Level Two -> Medium\n3 - Level Tree -> Hard\n ")
        if op == 1:
            Mat(1)
            
Menu()
