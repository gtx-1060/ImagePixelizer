from os import listdir, path, mkdir, rmdir, remove
import base64
from PIL import Image
import json
import hashlib


class Util:
    converted_path = None

    @staticmethod
    def convert_all_to_png(folder : str, quality : int = 30) -> str:
        toPath = path.join(path.abspath(folder), path.basename(folder), "converted/")
        print(path.basename(folder))
        Util.converted_path = toPath
        if (not path.isdir(toPath)):
            mkdir(toPath)
        for fl in Util.file_list(folder):
            if path.isdir(path.join(folder,fl)):
                continue
            print(fl)
            Util.save_with_compression(folder+fl, f"{toPath+fl[0:fl.rfind('.')]}.png", quality)
        return toPath
    
    @staticmethod
    def delete_cached():
        if Util.converted_path == None:
            return
        try:
            files = Util.file_list(Util.converted_path)
            for f in files:
                remove(Util.converted_path+f)
            rmdir(Util.converted_path)
            Util.converted_path = None
        except Exception as e:
            print(e)
            print(Util.converted_path)

    @staticmethod
    def save_with_compression(fromPath : str, toPath : str, q : int = 50):
        try:
            img = Image.open(fromPath)
            img = Util.compress_image(img)
            img.save(toPath, "PNG", quality = q)
        except FileNotFoundError as e:
            print(e)
        except FileExistsError as e:
            print(e)

    @staticmethod
    def compress_image(img : Image.Image):
        w, h = img.size
        print(w, h)
        if w > h:
            h = int(400 * (h / w))
            w = 400
        else:
            w = int(400 * (w / h))
            h = 400
        return img.resize((w, h))

    @staticmethod
    def get_hash(pic : bytes):
        h = hashlib.new("md5")
        h.update(pic)
        return h.hexdigest()

    @staticmethod
    def save_image(pic : str, path : str = "", fileName : str = None):
        pic = base64.b64decode(pic)
        if fileName == None: fileName = Util.get_hash(pic)
        with open(f"{path+fileName[0:fileName.rfind('.')]}.png",'wb') as file:
            file.write(pic)
            file.close()

    @staticmethod
    def file_list(path : str):
        return listdir(path)

    @staticmethod
    def load_image(fullPath : str):
        with open(fullPath, 'rb') as f:
            return base64.b64encode(f.read())

    @staticmethod
    def parse_json(string : str):
        return json.loads(string)

    @staticmethod
    def load_settings():
        try:
            f = open('config.json', 'r')
            settings = Util.parse_json(f.read())
            f.close()
        except Exception as e:
            print(e)
        return settings
