import time
import cv2

# import SDK library
from supports.tello_sdk.Command import Command
from supports.tello_sdk.Stream import Stream

# create SDK object
command = Command(log=False)

# enter SDK mode and takeoff
command.command()

# enable and start camera stream
stream = Stream(adress='udp://0.0.0.0:11111').start()

# set flight timeout
timeout_msec = 5000
initial_time = time.time()

# flag to check if tello has taken off
has_takeoff = False

# image name
image_name = 'Ambrosia_trifida.jpg'

while True:
    try:
        # takeoff once
        if not has_takeoff:
            has_takeoff = True
            command.takeoff()

        # check if flight time not reach timeout
        flight_time = time.time() - initial_time
        if flight_time < timeout_msec:

            # save frame to image file that later can be used 
            # for object recognition and pose estimation
            key = cv2.waitKey(1) & 0xFF
            if key == ord('p'):
                print("picture")
                cv2.imwrite(image_name, stream.frame)
                continue

            # display the image
            cv2.imshow("example", stream.frame)
            cv2.waitKey(1)

        else:
            # land tello when reach flight timeout
            command.land()
            command.disable_stream()
            break

    except KeyboardInterrupt:
        # land tello when hit ctrl+c in emergency
        command.land()
        command.disable_stream()
        break