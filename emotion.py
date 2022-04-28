import base64
import numpy as np

from fer import FER
import cv2

def get_emotion(img_base64):
    img_binary = base64.b64decode(img_base64)
    img_jpg = np.frombuffer(img_binary, dtype=np.uint8)
    img = cv2.imdecode(img_jpg, cv2.IMREAD_COLOR)
    
    detector = FER()
    try:
        emotion, score = detector.top_emotion(img)
        result = "You seem to be " + emotion
    except:
        result = "The image was unclear\nPlease try again.."
    
    print(score)
    return emotion, result, img_base64

