"""a=[0, 1, 2]
b = 1
def A(a, b):
    a.remove(2)
    a[0] = 10
    b = 0

print(a, b)
A(a, b)
print(a, b)"""

"""import pygame
pygame.init()
screen = pygame.display.set_mode((200,300))
font = pygame.font.SysFont("Arial Rounded MT Bold", 60)
surface = font.render("hello pygame", False, (255, 200 ,10))
print(type(surface))
screen.blit(surface, (100, 100))
pygame.display.update()"""


"""a="123"
b="123"
print(a == b)"""

"""a=[[0]*3]*2
b =a.copy()
b[0][0] = 1
print(b)"""

"""if 1 >= 1 | 2 <= 2:
    print(1)"""

"""import numpy as np
y = np.zeros(10)
print(y)
print(y[0])

m = []
n = []
for j in range(9):
    n.append((0))
for i in range(5):
    m.append(n.copy())
m[0][0] = 1
print(m)"""



"""from PIL import Image
import os
import pygame
def gif_to_png(gifpath):#将gif转为png列表
    im = Image.open(gifpath)  # 打开一个序列文件时，PIL库自动加载第一帧
    photos = []

    try:
        while (1):
            filename = "植物大战僵尸角色素材/植物/豌豆射手/豌豆射手等待/豌豆射手" + str(im.tell()) + ".png"
            im.save(filename)
            im.seek(im.tell() + 1)  # 向下一帧移动
            if im.tell() == 7:
                im.seek(im.tell() + 1)
    except EOFError:
        pass
    return photos

gif1 = gif_to_png("植物大战僵尸角色素材/植物/豌豆射手.gif")"""


"""import os
import pygame
dirs = os.walk("植物大战僵尸角色素材/僵尸/普通僵尸")
for i in dirs:
    print(i[2])"""


"""a = (1, 2, 3)
print(a[2])"""

"""import os
import pygame
def pygame_Load_image(path):
    image_name_list = []
    for list in os.walk(path):
        for i in list[2]:
            image_name_list.append(pygame.image.load(path + "/" + i))
    return image_name_list
pygame_Load_image("植物大战僵尸角色素材/僵尸/普通僵尸")"""


"""#import eval
print(eval("1 + 1"))"""


"""from PIL import Image
import os
def load_image(path):
    for root, dirs, files in os.walk(path):

        for file in files:
            print(root)
            print(os.path.join(root, file))
            im = Image.open(os.path.join(root, file))
            im.save(os.path.join(root, file))
    print("success!")

load_image("植物大战僵尸角色素材")
"""

"""m = {1:1, 2:2, 4:3}
m[3] = 4
print(m[3])
print(len(m))
for i in range(0):
  print(i)
print(0)"""

"""import  pygame
import sys
from pygame.locals import *
from parameter import *

screen = pygame.display.set_mode((1000, 600))
im = pygame.image.load("game_picture/background/lose.png").convert_alpha()
i = 0
while True:
  events = pygame.event.get()
  for event in events:
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  screen.fill((0, 200, 0))
  screen.blit(im, (0, 0))
  pygame.display.update()
"""
"""class A:
  def __init__(self):
    self.a = 0
    self.b = 1
a = A()
b = A()
c = [a, b]
for i in c:
  d = i
d.a = 9
print(c[1].a)"""

"""import  pygame
font = pygame.font.get_fonts()
for i in font:
  print(i)"""

"""import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((100, 100))
ice = pygame.image.load("game_picture/background/ice0.png").convert_alpha()
print(ice.get_size())"""


import numpy as np
a = np.zeros((5, 6))
a[1][1] = 1
print(a)