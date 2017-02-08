from PIL import Image
im=Image.open('./image/litten.png')
print(im.format,im.size,im.mode);

im.thumbnail((100,100));
im.save('./image/thumb.jpg',"JPEG");