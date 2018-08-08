__author__ = "Narwhale"
#导入方法
from PIL import Image,ImageDraw,ImageFont
#打开图片
im = Image.open('qq.jpg')
#获取长w，高h
w,h = im.size
#设置图片可绘制
image_draw = ImageDraw.Draw(im)
#设置字体样式
text_font = ImageFont.truetype("C:\Windows\Fonts\SCRIPTBL.TTF",20)
#设置写什么字
text1 = '1'
#绘制一个在右上角的半径为40的圆，颜色为红色
image_draw.ellipse((w-40,0,w,40),fill='red',outline='red')
#将字写上绘制的圆上
image_draw.text([w-25,10],text1,font=text_font,fill='white')
#图片保存
im.save("C:\\PycharmProjects\\编程\\7月\\7.5\\qq2.jpg")