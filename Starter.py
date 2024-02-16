from hub import light_matrix, motion_sensor, port
import runloop, motor_pair, motor,math,time,runloop, color, color_sensor

async def drive(distance, speed):
    CM = round(distance * 17.5)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, CM, 0, velocity = speed, stop=motor.COAST)

async def turnLeft(angle): 
    motion_sensor.reset_yaw(0) #resets the wheel angle (if it was anything other than 0)
    while motion_sensor.tilt_angles()[0]<(angle*10): #while the angle sensor is less than desired angle
         motor_pair.move(motor_pair.PAIR_1,-100) #both motors will run -100 degrees
    motor_pair.stop(motor_pair.PAIR_1) #stop the motors after that while loop

async def turnRight(angle):
    motion_sensor.reset_yaw(0) #resets the wheel angle (if it was anything other than 0)
    while motion_sensor.tilt_angles()[0]>(angle*-10): #getting yaw value from tuple
        motor_pair.move(motor_pair.PAIR_1,100) #move to right
    motor_pair.stop(motor_pair.PAIR_1)

def whiteFound():
    return color_sensor.color(port.A) != color.WHITE

async def main():
    # write your code here
    motor_pair.pair(motor_pair.PAIR_1,port.D,port.C)

    

runloop.run(main())
