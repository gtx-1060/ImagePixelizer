from pixel import Art
from threading import Thread
from utils import Util 
import time

def convert(path : str, outputPath: str):
    img = Util.load_image(path)
    art = Art(img)
    try:
        pixel_img = art.get_image(Art.Resolution.HIGHT)
        Util.save_image(pixel_img, outputPath)
    except Exception as e:
        print(e)

def start_async(files : list, new_path : str, out_path : str):
    startTime = time.time()
    threads = []
    for item in files:
        fullpath = new_path+item
        threads.append(Thread(target=convert, args = (fullpath, out_path)))
        threads[len(threads)-1].start()
    for thread in threads:
        thread.join()

    print(f"All operations completed in {round(time.time() - startTime,3)} seconds")
    Util.delete_cached()

def launch():
    settings = Util.load_settings()
    new_path = Util.convert_all_to_png(settings["sources_path"], 30)   
    out_path = settings["output_path"]
    files = Util.file_list(new_path)
    start_async(files, new_path, out_path)

if __name__ == "__main__":
    launch()


