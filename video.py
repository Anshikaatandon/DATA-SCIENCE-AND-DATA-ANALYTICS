import cv2

def read_video(path):
    video = cv2.VideoCapture(path)
    while True:
        state,frame = video.read()
        if not state:
            break
        frame = process_something(frame)