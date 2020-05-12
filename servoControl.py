from motors import Servo
from motors import OmegaPwm
import time

def logic(operator, a, b):
    if(operator == 1):
        return a & b #AND
    elif(operator == 2):
        return a | b #OR
    elif(operator == 3):
        return ~(a & b) + 2 #NAND
    elif(operator == 4):
        return ~(a | b) + 2 #NOR
    elif(operator == 5):
        return a ^ b #XOR
    elif(operator == 6):
        return ~(a ^ b) + 2 #XNOR
    else:
        print ("incorrect logical operator")

def servoCTRL(servo, channel, minPulse, maxPulse):
    servo = Servo(channel, minPulse, maxPulse)
    servo.setAngle(180.0)
    time.sleep(0.1)
    servo.setAngle(90.0)

def main():
    # instantiate objects for all servos
    servoA  = Servo(0, 500, 2400)
    servoB  = Servo(1, 500, 2400)
    servoQa = Servo(2, 500, 2400)
    servoA1 = Servo(3, 500, 2400)
    servoB1 = Servo(4, 500, 2400)
    servoQb = Servo(5, 500, 2400)
    servoQ  = Servo(6, 500, 2400)
    
    # set all servos to the neutral position
    servoA.setAngle(90.0)
    servoB.setAngle(90.0)
    servoQa.setAngle(90.0)
    servoA1.setAngle(90.0)
    servoB1.setAngle(90.0)
    servoQb.setAngle(90.0)
    servoQ.setAngle(90.0)
    
    
    print('Enter Input 1 (0 or 1):')
    a = int(input())
    print('Enter Input 2 (0 or 1):')
    b = int(input())
    print('Enter Input 3 (0 or 1):')
    a1 = int(input())
    print('Enter Input 4 (0 or 1):')
    b1 = int(input())

    
    
    #standard setup: 1 AND, 2 OR, 3 NAND
    operator1 = int(1)
    operator2 = int(2)
    operator3 = int(3)

    #logic gate Qa evaluate
    Qa = logic(operator1, a, b)
    
    #logic gate Qb evaluate
    Qb = logic(operator2, a1, b1)
    
    #logic gate Q evaluate
    Q = logic(operator3, Qa, Qb)
    
    #open input gates
    if(a == 1):
        servoCTRL(servoA, 0, 500, 2400)
    if(b == 1):
        servoCTRL(servoB, 1, 500, 2400)
    if(a1 == 1):
        servoCTRL(servoA1, 3, 500, 2400)
    if(b1 == 1):
        servoCTRL(servoB1, 4, 500, 2400)
    
    time.sleep(2)
    #open output gates
    if(Qa == 1):
        servoCTRL(servoQa, 2, 500, 2400)
    if(Qb == 1):
        servoCTRL(servoQb, 5, 500, 2400)
    
    time.sleep(2)    
    #open final gate
    if(Q == 1):
        servoCTRL(servoQ, 6, 500, 2400)

if __name__ == '__main__':
    main()