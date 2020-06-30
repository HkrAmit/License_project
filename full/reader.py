import zbar

from PIL import Image
import cv2


def reader():

    # Begin capturing video. You can modify what video source to use with VideoCapture's argument. It's currently set
    # to be your webcam.
    capture = cv2.VideoCapture(0)

    while True:

        # Breaks down the video into frames
        ret, frame = capture.read()

        # Displays the current frame
        #cv2.imshow('Current', frame)

        # Converts image to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Uses PIL to convert the grayscale image into a ndary array that ZBar can understand.
        image = Image.fromarray(gray)
        width, height = image.size
        zbar_image = zbar.Image(width, height, 'Y800', image.tobytes())

        # Scans the zbar image.
        scanner = zbar.ImageScanner()
        scanner.scan(zbar_image)

        # Prints data from image.
        out=0
        for decoded in zbar_image:
            #print(decoded.data)
            out=decoded.data
        if out!=0:
            #print(out)
            return out
            break

if __name__ == "__main__":
    reader()
