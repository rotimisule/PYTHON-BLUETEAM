while True:
    ## this output line wasnt needed but it felt like a unresponsive code without 
    n = int(input('Enter an integer between 1 and 100: '))
#check if n is in range 
    if  (n < 100) and (n > 1):
#check if n is weird , must be odd num or even within the range of 6-20
        if n % 2 != 0  :
            print ("Weird")
            break
        elif n in range(6, 20):
            if n % 2 == 0 :
                print ("Weird")
                break
#check if n is not weird , must be even in range 2-5 or even when greater than 20  
        if n in range(2, 5):
            if n % 2 == 0:
                print("Not Weird")
                break
        elif n > 20:
            if n % 2 == 0:
                print("Not Weird")
                break
    
    
