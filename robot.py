from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

hub = PrimeHub()

AXLE_TRACK = 112

left_drive = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_drive = Motor(Port.D, Direction.CLOCKWISE)
drive = DriveBase(left_drive, right_drive, 64, AXLE_TRACK)
drive.use_gyro(True)

# attachment motors spin inward
right_attach = Motor(Port.F, Direction.COUNTERCLOCKWISE)
left_attach = Motor(Port.B, Direction.CLOCKWISE)