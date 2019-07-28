import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
coil_A_1_pin = 27 # pink
coil_A_2_pin = 17 # orange
coil_B_1_pin = 23 # blue
coil_B_2_pin = 24 # yellow

# adjust if different
StepCount = 8
MotorVel = 0
Seq = range(0, StepCount)
Seq[0] = [1,0,0,0]
Seq[1] = [1,1,0,0]
Seq[2] = [0,1,0,0]
Seq[3] = [0,1,1,0]
Seq[4] = [0,0,1,0]
Seq[5] = [0,0,1,1]
Seq[6] = [0,0,0,1]
Seq[7] = [1,0,0,1]



GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)



def setStep(w1, w2, w3, w4):
    print("seq:"+ str(w1) + " " + str(w2) + " " + str(w3) + " " + str(w4) +" ")
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

def forward(delay, steps):
    for i in range(steps):
        for j in range(0,StepCount,MotorVel):
            print(str(j))
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(0,StepCount,MotorVel)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

if __name__ == '__main__':
    try:
        while True:
            MotorVel=2
            delay = raw_input("Time Delay (ms)?")
            steps = raw_input("How many steps forward? ")
            forward(int(delay) / 1000.0, int(steps))
            steps = raw_input("How many steps backwards? ")
            backwards(int(delay) / 1000.0, int(steps))
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
