from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, MoveDifferential, SpeedPercent
from ev3dev2.wheel import EV3Tire
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.sound import Sound
from .button import Button
from time import sleep

# Config setting for Griffy
LEFT_MEDIUM_MOTOR_PORT = OUTPUT_A
LEFT_LARGE_MOTOR_PORT = OUTPUT_B
RIGHT_LARGE_MOTOR_PORT = OUTPUT_C
RIGHT_MEDIUM_MOTOR_PORT = OUTPUT_D
STUD_MM = 7
WHEEL_CLASS = EV3Tire
WHEEL_DISTANCE = STUD_MM * 11 # Center of wheels are 11 studs apart
LEFT_GYRO_SENSOR_INPUT = INPUT_1
LEFT_COLOR_SENSOR_INPUT = INPUT_2
RIGHT_COLOR_SENSOR_INPUT = INPUT_3
RIGHT_GYRO_SENSOR_INPUT = INPUT_4


class Griffy(MoveDifferential):
    """
    Created a Griffy Class based on MoveDifferential
    Adds:
    Move with Gyro
    Recreated PID Line Follower
    Drive until color
    Maybe Missions
    """

    def __init__(self):
        """
        Initalize a griffy class which is based
        on move differential. Also set up the medium motors
        and all sensors.
        """
        super().__init__(LEFT_LARGE_MOTOR_PORT, RIGHT_LARGE_MOTOR_PORT, WHEEL_CLASS, WHEEL_DISTANCE)
        self.left_color_sensor = ColorSensor(LEFT_COLOR_SENSOR_INPUT)
        self.cs = self.left_color_sensor
        self.left_gyro_sensor = GyroSensor(LEFT_GYRO_SENSOR_INPUT)
        self.right_gyro_sensor = GyroSensor(RIGHT_GYRO_SENSOR_INPUT)
        self.right_color_sensor = ColorSensor(RIGHT_COLOR_SENSOR_INPUT)
        self.left_medium_motor = MediumMotor(LEFT_MEDIUM_MOTOR_PORT)
        self.right_medium_motor = MediumMotor(RIGHT_MEDIUM_MOTOR_PORT)
        # Put a sound at the end to show when it is done.
        self.start_tone()

    def start_tone(self):
        player = Sound()
        player.play_tone(500, 0.5, delay=0.0, volume=100, play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

    def line_square(self, black_light_intensity, white_light_intensity):
        """Needs a method description and usage."""
        pass

    def pid_line_follow(self, black_light_intensity, white_light_intensity, speed):
        """Needs a method description and usage."""
        pass

    def dive_until_color(self, speed):
        """Needs a method description and usage."""
        pass

    def gyro_turn(self, degrees, speed):
        """Needs a method description and usage."""
        pass

    def first_run(self):
        """Needs a method description and usage."""
        self.on_for_distance(30, 520)
        self.on_for_distance(-100, 520)
