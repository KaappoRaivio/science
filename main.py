from PIL import Image
import sys
import io
import time

try:
    import picamera
except ImportError:
    print("couldn't import PiCamera!")

def getRaspiImage():
    stream = io.BytesIO()
    camera = picamera.PiCamera()
    # camera.start_preview()
    # sleep(2)
    camera.capture(stream, format='jpeg')
    # "Rewind" the stream to the beginning so we can read its content
    stream.seek(0)
    image = Image.open(stream)
    image.thumbnail((640,480))
    a = image.convert("RGBA").getdata()
    print("done")
    return a


def openImage(path):
    print("getting photo")
    image = Image.open(path).convert("RGBA")
    image.thumbnail((640,480))
    a = image.convert("RGBA").getdata()
    print("done")
    return a

def getPhoto():
    return openImage("IMG_20200309_134525.jpg")


def getMask():
    return openImage("IMG_20200309_134525_maski.png")


def analyze():
    newData = []
    for pixel, mask in zip(getPhoto(), getMask()):
        newData.append((*pixel[:3], mask[0]))

    filtered = filter(lambda x: x[3] != 0, newData) # filter all masked
    average = tuple(map(lambda x: sum(x[:3]) / 3, filtered))
    value = sum(average) / len(average)

    return value / 255


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "overwrite":
        mode = "w"
    else:
        mode = "a"

    with open("data.csv", mode) as file:
        file.write(f"{analyze():.2f};")
