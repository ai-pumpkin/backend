
from openaiclient import OpenAIClient
from gradio_client import Client
import cv2
import argparse
import numpy as np
import random

import torch

from PIL import Image
from ram.models import ram_plus
from ram import inference_ram as inference
from ram import get_transform

from IPython.display import clear_output



img_client = Client("https://xinyu1205-recognize-anything.hf.space/")
oac = OpenAIClient(api_key="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", model="gpt-3.5-turbo", )


image_size = 384
transform = get_transform(image_size=image_size)

model = ram_plus(pretrained='pretrained/ram_plus_swin_large_14m.pth',
                 image_size=image_size,
                 vit='swin_l')

model.eval()
device = "mps"
model = model.to(device)

def pilify(x):
    x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
    return Image.fromarray(x, "RGB")

def is_person(taglist):
    taglist = taglist.split(" | ")
    for x in taglist:
        x = x.lower()
        if x in ["man", "woman", "person", "couple"]:
            return True
    return False

def main():
    # Capture video from the first webcam connected to the system
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        img = pilify(frame)
        image = transform(img).unsqueeze(0).to(device)
        res = inference(image, model)
        tags = res[0]
        clear_output(wait=True)
        print(tags)
        print(is_person(tags))

        # call say_something function

        # Check if frame is read correctly
        if not ret:
            break

        # Display the frame
        cv2.imshow('Webcam', frame)

        # Break out of the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()


exit()
result = img_client.predict(
				image_path,	
				fn_index=2
)

print(result[0])
tags = result[0]

prompt = f"You are a scary pumpkin during Halloween. There is a person in front of you that you are trying to scare. I took a picture of this person and I am going to describe it to you using tags. Delimited by  {tags}. Write a creepy sentence about this person using details about the person and their surroundings."

response = oac.chat_completion(prompt)

print(response)



