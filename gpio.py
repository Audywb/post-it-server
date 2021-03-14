import RPi.GPIO as GPIO  

from time import sleep 

GPIO.setwarnings(False)  

GPIO.setmode(GPIO.BOARD)  

GPIO.setup(8, GPIO.IN) #Read output from PIR motion sensor 
people = [] 

while True:  

    input=GPIO.input(8)  
    n = 0
    m = 1

    if input == 0: #When output from motion sensor is LOW 
        print ("No object detected",input) 
        sleep(1) 
    elif input == 1: #When output from motion sensor is HIGH 
        print ("Object detected",input) 
        n = n+m
        people.append(n)
        print(sum(people))
        sleep(1)
    else:
        break
        
print(people)
people = [] 

while True:  

    x = int(input()) 
    n = 0
    m = 1

    if x == 0: #When output from motion sensor is LOW 
        print ("No object detected",input) 
        
    elif x == 1: #When output from motion sensor is HIGH 
        print ("Object detected",input) 
        n = n+m
        people.append(n)
        print(sum(people))

    else:
        break
        
print(people)