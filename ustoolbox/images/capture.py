# -*- coding: utf-8 -*-

# import the necessary packages

import cv2
import logging
import os
import numpy as np
from os.path import splitext
from imutils.video import FPS
from imutils.video import VideoStream

from ustoolbox.utils.io_validations import (is_dir_empty, is_directory, is_accessible)

# Reference frame
# 0/0---X--->
#  |
#  Y
#  |
#  v

def __warm_up(source: int = 0, numFrames: int = 60):
    # Capture from device
    cap = VideoStream(src=source).start()

    # Check if camera opened successfully
    if (cap.stream.isOpened() == False):
        print("Unable to read camera feed")

    # Warm-up the device during 30 frames
    fps = FPS().start()
    while fps._numFrames < numFrames:
        _ = cap.read()
        # update the FPS counter
        fps.update()
    fps.stop()

    return cap


def device_settings():
    """
        Displays some settings of the current device.

        Source: https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html
    Returns
    -------
        None
    """

    cap = __warm_up(source=0, numFrames=60)

    # Read the current device setting
    frame_rate = cap.stream.get(cv2.CAP_PROP_FPS)
    width = cap.stream.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.stream.get(cv2.CAP_PROP_FRAME_HEIGHT)
    brightness = cap.stream.get(cv2.CAP_PROP_BRIGHTNESS)
    contrast = cap.stream.get(cv2.CAP_PROP_CONTRAST)
    saturation = cap.stream.get(cv2.CAP_PROP_SATURATION)
    hue = cap.stream.get(cv2.CAP_PROP_HUE)
    gain = cap.stream.get(cv2.CAP_PROP_GAIN)
    exposure = cap.stream.get(cv2.CAP_PROP_EXPOSURE)

    print("[INFO] Press ESC to stop the device")
    print()

    fps = FPS().start()
    while True:
        img = cap.read()
        cv2.imshow("Device setting, press ESC to quit.", img)
        key = cv2.waitKey(10)

        if key == 27:
            break

        # Update the FPS counter
        fps.update()

    fps.stop()

    print("Height:      {} (Height of the frames in the video stream)".format(height))
    print("Width:       {} (Width of the frames in the video stream)".format(width))
    print("Brightness:  {} (Brightness of the image (only for cameras))".format(brightness))
    print("Contrast:    {} (Contrast of the image (only for cameras))".format(contrast))
    print("Saturation:  {} (Saturation of the image (only for cameras))".format(saturation))
    print("Hue:         {} (Hue of the image (only for cameras))".format(hue))
    print("Gain:        {} (Gain of the image (only for cameras))".format(gain))
    print("Exposure:    {} (Exposure (only for cameras))".format(exposure))
    print("FPS:         {:.2f} (Frame rate)".format(fps.fps()))

    # Release the video capture, and destroy all the windows
    cv2.destroyAllWindows()
    cap.stop()


def capture_sequence(output_path: str, everyFrame: int = 1):
    """
        Capture a set of frames until ESC is pressed

    Parameters
    ----------
    output_path : str
        Path to save the frames
    everyFrame : int
        Indicate that every n frames, one of them will be stored

    Returns
    -------
        None

    """
    cap = __warm_up(source=0, numFrames=60)

    if everyFrame <1:
        raise ValueError('The parameter `everyFrame` must be positive')

    if is_directory(output_path):
        logging.info("Ouput directory {} already exists".format(output_path))
        if not is_dir_empty(output_path):
            raise ValueError('The output directory is not empty')

    else:
        logging.info("Output directory {} does not exist, creating directory".format(output_path))
        try:
            os.makedirs(output_path)
        except OSError:
            print('Error: Creating directory {} '.format(output_path))


    fps = FPS().start()
    print("[INFO] Press ESC to stop the device")
    print()

    while True:
        img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Device capture, press ESC to quit.", gray)
        key = cv2.waitKey(10)

        if key == 27:
            break

        i = fps._numFrames
        if i % everyFrame == 0:
            new_frame = 'IMG_{}.png'.format(i)

            # write the frame to disk
            new_frame_path = os.path.join(output_path, new_frame)
            cv2.imwrite(new_frame_path, gray)

        # update the FPS counter
        fps.update()


    # stop the timer and display FPS information
    fps.stop()
    logging.info("Elapsed time:     {:.2f}".format(fps.elapsed()))
    logging.info("Approximated FPS: {:.2f}".format(fps.fps()))


    # Release the video capture, and destroy all the windows
    cv2.destroyAllWindows()
    cap.stop()


