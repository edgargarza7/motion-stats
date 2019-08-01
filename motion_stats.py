import time #library used to obtain time stamps
from gpiozero import MotionSensor #library used to access MotionSensors
from sense_hat import SenseHat #library used to access SenseHat

sensor_start = MotionSensor(17) #initilze first motion sensor to GPIO 17
sensor_end = MotionSensor(27) #initilize second motion sensor to GPIO 27
sense = SenseHat() #initilize SenseHat
distance = 0.381 #constant variable created for distance

sensor_start.wait_for_motion() #first motion sensor is waiting for motion
t_stamp1 = time.time() #once motion is detected obtain time stamp
print("motion detected")
print(t_stamp1)

sensor_end.wait_for_motion() #second motion sensor is waiting for motion
t_stamp2 = time.time() #once motion is detected obtain time stamp
print("motion detected")
print(t_stamp2)

run_time = round((t_stamp2 - t_stamp1), 2) #calculate total run time
speed = round((distance / (t_stamp2-t_stamp1)), 2) #calculate speed

print(run_time)
print(speed)
print("This is the run time: " + str(run_time))
print("This is the speed: " + str(speed))

#print out data to SenseHat LED matrix
red = (255,0,0)
sense.show_message("Runtime: " + str(run_time), text_colour=[255,0,0])
sense.show_message("Speed: " + str(speed), text_colour=[255,0,0])    