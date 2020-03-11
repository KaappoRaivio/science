import picamera


def getRaspiImage():
    stream = io.BytesIO()
    # camera.start_preview()
    time.sleep(1)

    camera.capture(stream, format='jpeg')
    # "Rewind" the stream to the beginning so we can read its content
    stream.seek(0)
    image = Image.open(stream)
    image.thumbnail((640,480))
    a = image.convert("RGBA").getdata()
    print("done")
    return a
