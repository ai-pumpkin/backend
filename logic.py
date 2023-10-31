import cv2
from PIL import Image
from oac import OpenAIClient
from ram.models import ram_plus
from ram import inference_ram as inference
from ram import get_transform
from text2speech import SaySomething

import time
class Logic:
    def __init__(self, model) -> None:
        self.model = model
        self.speak_model = SaySomething()
        self.was_person_visible = False
        self.was_person_visible_start = 0

    def __call__(self, frame):
        return self.step(frame)

    def step(self, frame):
        tags = self._run_model(frame)
        is_person = self._is_person(tags)
        
        if not is_person:
            self.was_person_visible = False
            return False

        now = time.time()
        if not self.was_person_visible:
            self.was_person_visible = True
            self.was_person_visible_start = now
            
        if now - self.was_person_visible_start > 3:
            self._talk(tags)
            return True
        
        return False
        

    def _detect_person(self, img):
        pass

    def _run_model(self, img):
        return self.model(img)

    def _talk(self, tags):
        self.speak_model.talk(image_tags=tags)

    def _is_person(self, taglist):
        taglist = taglist.split(" | ")
        allowlist = [
                "man",
                "woman",
                "person",
                "couple",
                "boy",
                "girl",
                "child",
                "kid",
                "baby",
                "people",
            ]
        print(taglist)
        for x in taglist:
            x = x.lower()
            if x in allowlist:
                return True
        return False
