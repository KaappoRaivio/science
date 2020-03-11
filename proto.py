from PIL import Image

x = Image.open("/home/kaappo/git/science/IMG_20200309_134525_maski.png") \
    .convert("RGBA")
# x.thumbnail((640,480))

b = x.getdata()

y = Image.open("/home/kaappo/git/science/IMG_20200309_134525.jpg") \
    .convert("RGBA")
# y.thumbnail((640,480))
a = y.getdata()

newData = []
for pixel, mask in zip(a, b):
    newData.append((*pixel[:3], mask[0]))

y.putdata(newData)

filtered = filter(lambda x: x[3] != 0, newData) # alpha-0 pois
# print(tuple(filtered))
# a = tuple(filtered)
# print(len(a))

average = tuple(map(lambda x: sum(x[:3]) / 3, filtered))
# print(average)
value = sum(average) / len(average)

print(value / 255)
