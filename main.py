import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

def speech(text):
    print(text)
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save('./Sounds/output.mp3')
    playsound('./Sounds/output.mp3')


cap = cv2.VideoCapture(0)  # make a capture object
labels =[]

while True:
    ret, frame = cap.read()
    bbox, label, conf = cv.detect_common_objects(frame)  # detection
    output_image = draw_bbox(frame, bbox, label, conf)  # makes a bounding box

    cv2.imshow('Object Detection', output_image)

    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)

    if cv2.waitKey(1) == ord('q'):
        break
i=0
new_sentence = []
for label in labels:
    if i == 0:
        new_sentence.append(f"I found a {label},")
    elif i==len(labels)-1:
        new_sentence.append(f"and a {label}.")
    else:
        new_sentence.append(f" a {label},")


    i+=1

speech(' '.join(new_sentence))