from ram import get_transform
from PIL import Image
import cv2 
from ram.models import ram_plus
from ram import inference_ram as inference


image_size = 384
transform = get_transform(image_size=image_size)
device = "mps"


def pilify(x):
    x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
    return Image.fromarray(x, "RGB")
      
        
class Model:
    
    def __init__(self) -> None:
        self._model = ram_plus(
            pretrained="pretrained/ram_plus_swin_large_14m.pth",
            image_size=image_size,
            vit="swin_l",
        )
        self._model.eval()
        self._model = self._model.to(device)
    
    def __call__(self, img):
        return self.run(img)
    
    def run(self, frame):
        img = transform(pilify(frame)).unsqueeze(0).to(device)
        tags = inference(img, self._model)[0]  
        return tags
    