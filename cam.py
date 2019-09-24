import cv2

video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    rgb_small_frame = frame[:, :, ::-1]
    cv2.imshow('Video',rgb_small_frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()