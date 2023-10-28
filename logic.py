import cv2
from PIL import Image
from oac import OpenAIClient
from ram.models import ram_plus
from ram import inference_ram as inference
from ram import get_transform
from text2speech import SaySomething


class Logic:
    def __init__(self, model) -> None:
        self.model = model
        self.speak_model = SaySomething()

    def __call__(self, frame):
        return self.step(frame)

    def step(self, frame):
        tags = self._run_model(frame)
        print(tags)
        is_person = self._is_person(tags)
        if not is_person:
            return

        self._talk(tags)

    def _detect_person(self, img):
        pass

    def _run_model(self, img):
        return self.model(img)

    def _talk(self, tags):
        self.speak_model.talk(image_tags=tags)

    def _is_person(self, taglist):
        taglist = taglist.split(" | ")
        for x in taglist:
            x = x.lower()
            if x in [
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
            ]:
                return True
        return False
