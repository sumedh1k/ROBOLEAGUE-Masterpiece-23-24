from hub import light_matrix, motion_sensor, port
import runloop, motor_pair, motor,math,time,runloop, color, color_sensor

async def drive(distance, speed):
    CM = round(distance * 17.5)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, CM, 0, velocity = speed, stop=motor.SMART_COAST)

async def turnLeft(angle):
    while motion_sensor.tilt_angles()[0]<(angle*10): #while the angle sensor is less than desired angle
        motor_pair.move(motor_pair.PAIR_1,-100, acceleration=600, velocity=350) #both motors will run -100 degrees
    motor_pair.stop(motor_pair.PAIR_1) #stop the motors after that while loop
    motion_sensor.reset_yaw(0) #reset yaw value

async def turnRight(angle):
    while motion_sensor.tilt_angles()[0]>(angle*-10): #getting yaw value from tuple
        motor_pair.move(motor_pair.PAIR_1,100,acceleration=600, velocity=350) #move to right
    motor_pair.stop(motor_pair.PAIR_1) #stop the motors after that while loop
    motion_sensor.reset_yaw(0) #reset yaw value


async def whiteout(speed, port):
    while(color_sensor.color(port) == 10):
            motor_pair.move(motor_pair.PAIR_1, 0, velocity = speed) #drive robot until white is not sensed
    motor_pair.stop(motor_pair.PAIR_1)

async def moveMotor(degrees,speed, side):
    if (side == "left"):
        motor.run_for_degrees(port.B, degrees, speed, stop = motor.HOLD)
    if (side == "right"):
        motor.run_for_degrees(port.A, degrees, speed, stop = motor.HOLD)        
    

async def main():
    # write your code here
    motion_sensor.reset_yaw(0)
    motor_pair.pair(motor_pair.PAIR_1,port.D,port.C)
    await drive(25,1050)
    # motor.run_for_time(port.A, 1000, 100)
    await moveMotor(-10,100,"left")
    await turnRight(45)
    await drive(16, 1050)
    await turnLeft(45)
    await drive(8, 1050)
    await moveMotor(100,800, "left")
    time.sleep_ms(250)
    await drive (15, 1050)
    await moveMotor(-100, 800, "left")
    await turnRight(45)
    await drive(18,1050)
    await turnLeft(70)#75 was original value
    await moveMotor(50, 350, "right")
    time.sleep_ms(500)
    await drive(11, 1050)
    time.sleep_ms(500)
    await moveMotor(48, 300, "right")
    await drive(-20, 1050)
    await moveMotor(-100,600,"right")
    await turnRight(60)
    await drive(-100, 1050)

    

runloop.run(main())