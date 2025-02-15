from PIL import Image
x = 600 #x坐标  通过对txt里的行数进行整数分解
y = 800 #y坐标  x*y = 行数

im = Image.new("RGB",(x,y))#创建图片
file = open('data.txt') #打开rbg值文件


#通过一个个rgb点生成图片
for j in range(0, y):
    for i in range(0,x):
        line = file.readline()#获取一行
        rgb = line.split(" ")#分离rgb
        im.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])))#rgb转化为像素
im.show()