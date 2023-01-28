#!/usr/bin/env python

import sys
import time


def run():
    
    
    USERINPUT_ERROR = False
    INTERNAL_ERROR = False
    INTERNAL_ERROR_COUNTER = 0
    ex1=0
    ex2=0
    n1,n2,USERINPUT_ERROR=userInput()
    
    if USERINPUT_ERROR:
        sys.exit("Too many wrong inputs")
    elif not USERINPUT_ERROR:
        try:
            sum =computerSummation(n1,n2)
            print("Using for loop:= Sum from ",n1," to ",n2,"is:",sum)
        except Exception as e:
            time.sleep(0.01)
            INTERNAL_ERROR = True
            INTERNAL_ERROR_COUNTER+=1
            ex1 = e
        try:
            
            sum  = mathSummation(n1,n2)
            print("Using math equations:= Sum from ",n1," to ",n2,"is:",sum)
        except Exception as e:
            time.sleep(0.01)
            INTERNAL_ERROR = True
            INTERNAL_ERROR_COUNTER+=1
            ex2 = e
    if INTERNAL_ERROR:
        print("Program finished with ",INTERNAL_ERROR_COUNTER," error(s).")
        print(ex1,"\n",ex2)
    elif not INTERNAL_ERROR:
        print("See you ;)")
    

def ValidateInput(chars):
    try:
        number_check = int(chars)
        return True,number_check
    except:
        return False,0

def checkInput(n1:int,n2:int):
    if n2 > n1:
        return True
    elif n1 > n2:
        return False
    else:
        return False
 
def userInput():
    
    ERROR_COUNTER = 0
    IS_VALID_NUMBER = False
    ERROR_FLAG = False
    IS_VALID_INPUT = False
    ERROR_COUNTER2 = 0
    
    while(not IS_VALID_INPUT and ERROR_COUNTER2 < 2 ):
        while(not IS_VALID_NUMBER and ERROR_COUNTER < 2):
            print("Start position ?")
            n1 = input()
            
            IS_VALID_NUMBER,n1 = ValidateInput(n1)
            
            if not IS_VALID_NUMBER:
                print("Not a valid numbr")
            ERROR_COUNTER += 1
            
        if(not IS_VALID_NUMBER):
            ERROR_FLAG = True
            return 0,0,ERROR_FLAG
            
        ERROR_COUNTER = 0
        IS_VALID_NUMBER = False
        
        while((not IS_VALID_NUMBER) and ERROR_COUNTER < 2):
            print("Last position ?")
            n2 = input()
            IS_VALID_NUMBER,n2 = ValidateInput(n2)
            if not IS_VALID_NUMBER:
                print("Not a valid number")
            ERROR_COUNTER += 1  
                
        if(not IS_VALID_NUMBER):
            ERROR_FLAG = True
            return 0,0,ERROR_FLAG
        ERROR_COUNTER = 0
        IS_VALID_NUMBER = False
#ERROR_FLAG = False
#return n1,n2,ERROR_FLAG

        if checkInput(n1,n2):
            IS_VALID_INPUT = True
            ERROR_FLAG=False
            return n1,n2,ERROR_FLAG
        elif not checkInput(n1,n2):
            IS_VALID_INPUT = False
            IS_VALID_NUMBER = False
            ERROR_FLAG = True
            ERROR_COUNTER2+=1
            print("First position bigger than last position?")
    if not IS_VALID_INPUT:
        return 0,0,ERROR_FLAG
            
            
    

    
def computerSummation(n1:int,n2:int):
    sum=0
    if n1 > n2:
        raise Exception("start position > end position")
    
    try:
        
        if n1 > 9999999 or n2 > 9999999:
            raise BaseException()
        for i in range(n1,n2+1):
            sum+=i
    except:
        raise Exception("Summation error")
    return sum



def mathSummation(n1:int,n2:int):
    if n1 > n2:
        raise Exception("start position > end position")
    try:
        
        n =(n2 - n1)+1
        sum  = int((n/2)*(n1+n2))
    except:
        raise Exception("Math error")
    return sum



if __name__ == "__main__":
    #global n1,n2
    n1=0
    n2=0
    print("Sum of consecutive number")
    try:
        run()
    except BaseException as e:
        print(e)
        sys.exit()