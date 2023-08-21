# your code goes here!

import time

def countdown(count): 
    while count > 0:
        print(f'{count} SECOND(S)!')
        
        count -= 1
        
    print('HAPPY NEW YEAR!')
countdown(5)         

def countdown_with_sleep(count):
    while count > 0:
        time.sleep(1)
        print(f'{count} SECOND(S)!')
        
        count -= 1
        
    print('HAPPY NEW YEAR!')
    
countdown_with_sleep(10)    
       