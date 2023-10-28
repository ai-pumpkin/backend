
import cv2
from PIL import Image
from oac import MyOAC
from ram.models import ram_plus
from ram import inference_ram as inference
from ram import get_transform


class Logic:
    
    def __init__(self, model, oac) -> None:
        self.is_talking = False
        self.model = model
        self.oac = oac
    
    def __call__(self, img):
        return self.step(img)
    
    def step(self, frame):  
        
        tags = self._run_model(frame)
        is_person = self._is_person(tags)
        if not is_person:
            if self.is_talking:
                self._stop_talking()
            return 
        
        if self.is_talking:
            return 

        sentence = self._tags2sentence(tags)
        return sentence # TODO REMOVE THIS LINE
        self._talk(sentence)
        
    def _detect_person(self, img):
        pass
    
    def _stop_talking(self):
        # TODO: stop talking
        self.is_talking = False
        
    def _run_model(self, img):
        return self.model(img)
    
    def _tags2sentence(self, tags):
        return self.oac(tags)
    
    def _talk(self, sentence):
        # 
        pass
        
    def _is_person(self, taglist):
        taglist = taglist.split(" | ")
        for x in taglist:
            x = x.lower()
            if x in ["man", "woman", "person", "couple"]:
                return True
        return False


