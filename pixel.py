import requests
import enum
from utils import Util

__all__ = ("Art")

class WrongConvertringException(Exception):
    def __init__(self, status_code: int, answer: str):
        super().__init__(f"Server answer: {answer}\nStatus code: {status_code}")
        self.errors = "WrongConvertringException"

class WrongDetectingException(Exception):
    def __init__(self, status_code: int, answer: str):
        super().__init__(f"Server answer: {answer}\nStatus code: {status_code}")
        self.errors = "WrongDetectingException"
        
class ImageWasntDetectedException(Exception):
    """If you try to call Art.getImage() after uncorrect detection (or without it), you get it"""

class Art:

    DEBUG = False
    DETECT_URL = "https://api.pixel-me.tokyo/api/v1/detect/"
    CONVERT_URL = "https://convert-to-pixelart-cat-ws3zldwfta-an.a.run.app/api/v1/convert/"
    __headers = { 
            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "content-type" : "application/json;charset=UTF-8",
            "accept" : "application/json, text/plain, */*",
        }

    class Resolution(enum.Enum):
        LOWEST = 3
        LOW = 2
        MEDIUM = 1
        HIGHT = 0

    def __init__(self, image : bytes, auto_detect = True):
        self.__image = {"image" : image.decode('utf8')}
        self.__success = False
        self.__pixelArt = None
        if auto_detect:
            self.detect_image()

    def detect_image(self):
        resp = requests.post(self.DETECT_URL, headers = self.__headers, json = self.__image)
        content = Util.parse_json(resp.content)
        if (resp.status_code == 200 and content['meta']['status'] == "ok"):
            self.__success = True
        else:
            raise WrongDetectingException(resp.status_code, resp.content)

    def get_image(self, resolution : int):
        if (self.__pixelArt != None):
            return self.__pixelArt[int(resolution)]["image"]
        if (not self.__success):
            raise ImageWasntDetectedException()
        
        resp = requests.post(self.CONVERT_URL, headers = self.__headers, json = self.__image)
        content = Util.parse_json(resp.content)
        if self.DEBUG:
            with open("temp.txt", "wb") as f:
                f.write(resp.content)
        if (resp.status_code == 200 and content['meta']['status'] == "ok"):
            self.__pixelArt = content['data']['images']
            return self.__pixelArt[resolution.value]["image"]
        else:
            raise WrongConvertringException(resp.status_code, resp.content)
