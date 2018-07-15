# -*- coding: utf-8 -*-

# import the necessary packages
import logging
import os
import time

import cv2
import numpy as np
from imutils import paths
from threading import Thread
from queue import Queue

from ustoolbox.utils.io_validations import (is_dir_empty, is_directory)

# Reference frame
# 0/0---X--->
#  |
#  |
#  Y
#  |
#  |
#  v

def video_capture_settings():
    camera_port = 0

    #capture from camera at location 0
    cap = cv2.VideoCapture(camera_port)
    cap.set(cv2.CAP_PROP_POS_MSEC, 1000)
    # Change the camera setting using the set() function
    # cap.set(cv2.CAP_PROP_EXPOSURE, -6.0)
    # cap.set(cv2.CV_CAP_PROP_GAIN, 4.0)
    # cap.set(cv2.CAP_PROP_BRIGHTNESS, 144.0)
    # cap.set(cv2.CAP_PROP_CONTRAST, 27.0)
    # cap.set(cv2.CV_CAP_PROP_HUE, 13.0) # 13.0
    # cap.set(cv2.CAP_PROP_SATURATION, 28.0)
    cap.set(cv2.CAP_PROP_FRAME_COUNT, 24.0)
    # Read the current setting from the camera
    test = cap.get(cv2.CAP_PROP_POS_MSEC)
    ratio = cap.get(cv2.CAP_PROP_POS_AVI_RATIO)
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    brightness = cap.get(cv2.CAP_PROP_BRIGHTNESS)
    contrast = cap.get(cv2.CAP_PROP_CONTRAST)
    saturation = cap.get(cv2.CAP_PROP_SATURATION)
    hue = cap.get(cv2.CAP_PROP_HUE)
    gain = cap.get(cv2.CAP_PROP_GAIN)
    exposure = cap.get(cv2.CAP_PROP_EXPOSURE)
    count = cap.get(cv2.CAP_PROP_FRAME_COUNT )
    print("Test: ", test)
    print("Ratio: ", ratio)
    print("Frame Rate: ", frame_rate)
    print("Height: ", height)
    print("Width: ", width)
    print("Brightness: ", brightness)
    print("Contrast: ", contrast)
    print("Saturation: ", saturation)
    print("Hue: ", hue)
    print("Gain: ", gain)
    print("Exposure: ", exposure)
    print("Count: ", count)

    while True:
        ret, img = cap.read()
        cv2.imshow("Test camera", img)
        key = cv2.waitKey(10)

        if key == 27:
            break

    cv2.destroyAllWindows()
    cv2.VideoCapture(0).release()


#   0  CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
#   1  CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
#   2  CAP_PROP_POS_AVI_RATIO Relative position of the video file
#   3  CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
#   4  CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
#   5  CAP_PROP_FPS Frame rate.
#   6  CAP_PROP_FOURCC 4-character code of codec.
#   7  CAP_PROP_FRAME_COUNT Number of frames in the video file.
#   8  CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
#   9  CAP_PROP_MODE Backend-specific value indicating the current capture mode.
#   10 CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
#   11 CAP_PROP_CONTRAST Contrast of the image (only for cameras).
#   12 CAP_PROP_SATURATION Saturation of the image (only for cameras).
#   13 CAP_PROP_HUE Hue of the image (only for cameras).
#   14 CAP_PROP_GAIN Gain of the image (only for cameras).
#   15 CAP_PROP_EXPOSURE Exposure (only for cameras).
#   16 CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
#   17 CAP_PROP_WHITE_BALANCE Currently unsupported
#   18 CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)



def capture_secuence():
    # Camera 0 is the integrated web cam on my netbook
    camera_port = 0

    # Number of frames to throw away while the camera adjusts to light levels
    ramp_frames = 30

    # Now we can initialize the camera capture object with the cv2.VideoCapture class.
    # All it needs is the index to a camera port.
    camera = cv2.VideoCapture(camera_port)

    # Check if camera opened successfully
    if (camera.isOpened() == False):
        print("Unable to read camera feed")

    # Captures a single image from the camera and returns it in PIL format
    def get_image():
        # read is the easiest way to get a full image out of a VideoCapture object.
        retval, im = camera.read()
        return im

    # These frames will be discarded and are only used
    # to adjust light levels, if necessary
    for i in range(ramp_frames):
        _, _ = camera.read()

    # Take the actual image we want to keep

    # for i in [1, 2, 3, 4 , 5]:
    #     print("Taking image...")
    #     camera_capture = get_image()
    #     file = 'test_image_{}.png'.format(i)
    #     cv2.imwrite(file, camera_capture)
    #     time.sleep(5)


    while True:
        ret, img = camera.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        if ret:
            # Display video
            cv2.imshow("Video capture", gray)
            key = cv2.waitKey(10)



            if key == 27:
                break
        # Break the loop
        else:
            break

    # A nice feature of the imwrite method is that it will automatically choose the
    # correct format based on the file extension you provide. Convenient!


    # Release the video capture, otherwise you won't be able to create a new
    # capture object until your script exits
    del (camera)

    # Close all the frames
    cv2.destroyAllWindows()

def crop_roi(input_path: str, output_path: str) -> None:
    '''
        Crop US images with a fix window

    Parameters
    ----------
    input_path :str
        Path to the directory that contains the original files
    output_path :str
        Path to the directory to store the cropped images

    Returns
    -------

    '''

    # Validation of parameters
    if not is_directory(input_path):
        raise ValueError('The input directory does not exist')

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

    logging.info('Processing directory: {}'.format(output_path))

    for image_path in sorted(list(paths.list_images(input_path))):
        logging.debug('Original image: {}'.format(image_path))
        _, filename = os.path.split(image_path)

        # read images
        image = cv2.imread(image_path, 0)

        # image(0:cY, 0:cX)
        cropped = image[40:435, 166:366]

        # write the cropped image to disk
        cropped_path = os.path.join(output_path, filename)
        cv2.imwrite(cropped_path, cropped)
        logging.debug('Cropped image: {}'.format(cropped_path))

    logging.info('Done!')




if __name__ == '__main__':
    from src.utils.logs import set_logger

    set_logger(1)
    # input_dir = '../../data/raw/test_crop_input'
    # output_dir = '../../data/raw/test_crop_output'
    # crop_roi(input_dir, output_dir)

    #capture_secuence()
    #video_capture_settings()





