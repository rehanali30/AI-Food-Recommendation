import base64
import numpy as np

from fer import FER
import cv2

from flask import Flask, request, make_response, render_template, url_for

app = Flask(__name__)

@app.route("/", methods=['GET'])
def login():
    return render_template('login.html')

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        pass
    else:
        return render_template('signup.html')

def get_emotion(img_base64):
    img_binary = base64.b64decode(img_base64)
    img_jpg = np.frombuffer(img_binary, dtype=np.uint8)
    img = cv2.imdecode(img_jpg, cv2.IMREAD_COLOR)
    
    detector = FER()
    emotion, score = detector.top_emotion(img)
    print(score)
    return emotion

@app.route('/emotion', methods=['POST', 'GET'])
def capture_img():
    if request.method == "POST":
        msg = get_emotion(request.form["img"])
        return make_response(msg)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)





