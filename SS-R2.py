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
    motion_sensor.reset_yaw(0)
    motor_pair.pair(motor_pair.PAIR_1,port.D,port.C)
    default = 800
    await drive(30,default)
    await turnRight(90)
    await drive(55,default)
    await turnRight(42)
    await drive(38,default)
    time.sleep_ms(500)
    await moveMotor(2500,1050,"left")
    time.sleep_ms(3000)
    await drive(-45, 1050)
    await turnLeft(135)
    await drive(-20,1050)
    await drive(7,1050)
    await drive(-9,1050)
    await drive(57,1050)
    await moveMotor(45,1050,"right")
    time.sleep_ms(300)
    await drive(-30,1050)
    await moveMotor(-45,1050,"right")
    await turnLeft(50)
    await drive(50,1050)
    await turnRight(50)
    await drive(40,1050)
    await turnRight(90)
    await drive(30,default)
    await moveMotor(4400,2000,"left")
    time.sleep_ms(4400)
    await drive(-30,1050)
    await turnRight(90)
    await drive(115,1050)
runloop.run(main())