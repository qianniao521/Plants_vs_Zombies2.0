from PIL import Image
import os
import pygame

pygame.init()

#组件尺寸
screen_size = (1080, 600)#窗口尺寸
map_size = (1400, 600)#地图尺寸
lawn_size = (738, 500)#整个草坪尺寸
lawn_cube_size = (82, 100)#草坪尺寸
card_size = (100, 60)#植物卡片
button_size = (112, 40)#按钮
button0_size = (40, 40)#按钮0
button_start_size = (200, 67)#开始按钮
card_select_size = (400, 300)#卡片片选择区
level_choose_size = (240, 160)#关卡选择区
shovel_size = (100, 40)#铲子背景图大小



#组件位置
pos_lawn = (250, 80)#草坪
pos_sun_warehouse = (160, 2)#太阳仓库
pos_im_speed_up = (880, 2)
pos_button_menu = (960, 2)#菜单按钮
pos_bg_card = (292, 80)#植物卡片选择背景图
pos_bg_timeout = (292, 80)#菜单界面背景图
pos_im_menu_button0 = (pos_bg_timeout[0] + 58, pos_bg_timeout[1] + 120)#菜单选择按钮0重新开始
pos_im_menu_button1 = (pos_bg_timeout[0] + 248, pos_bg_timeout[1] + 120)#菜单选择按钮1继续游戏
pos_im_menu_button2 = (pos_bg_timeout[0] + 58, pos_bg_timeout[1] + 220)#菜单选择按钮2退出游戏
pos_im_menu_button3 = (pos_bg_timeout[0] + 248, pos_bg_timeout[1] + 220)#菜单选择按钮3选择关卡
pos_button_start = (400, 433)#开始按钮
pos_card_member = (20, 10)#已选择的卡片所在区
pos_card_select = (pos_bg_card[0] + 8, pos_bg_card[1] + 20)#卡片片选择区
pos_bg_map = (0, 0)#地图
pos_im_start = (400, 200)#开始图片
pos_level_choose = (pos_bg_card[0] + 88, pos_bg_card[1] + 60)#关卡选择区
pos_button_return = (548, 320)#返回按钮
pos_bg_shovel = (300, 2)
pos_bg_level = (420, 2)
pos_im_attack_process_component0 = (560, 28)
pos_im_attack_process_component1 = (560, 5)
pos_im_over = (400, 100)
pos_im_over_button0 = (900, 200)
pos_im_over_button1 = (900, 400)
pos_im_attack_tips = (500, 300)


#字体及颜色
font1 = pygame.font.SysFont("Arial Rounded MT Bold", 36)
font2 = pygame.font.SysFont("Arial Rounded MT Bold", 24)
font3 = pygame.font.SysFont("隶书", 24)
font_color = [(200, 0, 0), (60, 60, 60), (0, 0, 0), (200, 200, 200)]


#植物参数
card_num = 8 #最大上阵植物数量
species = 8 #植物种数

plants = []#植物属性列表
for i in range(species):
    plants.append([])

max_cd = []#植物最大冷缩
now_cd = []#当前已冷缩
price = []#植物价格
statu_p = []#植物共有几种状态
statu_b = []#子弹共有几种状态
            #   max_cd  now_cd  price   statu_p statu_b get
plants[0]   =   [8,     0,      100,    2,      2,      1]  #豌豆射手
plants[1]   =   [8,     8,      50,     2,      1,      2]  #向日葵
plants[2]   =   [30,    0,      50,     3,      0,      3]  #坚果墙
plants[3]   =   [15,    0,      25,     3,      0,      4]  #土豆地雷
plants[4]   =   [12,    0,      150,    3,      0,      5]  #大食花
plants[5]   =   [60,    0,      150,    2,      0,      6]  #樱桃炸弹
plants[6]   =   [12,    0,      175,    2,      2,      7]  #寒冰射手
plants[7]   =   [30,    0,      125,    2,      0,      8]  #火辣椒


for i in plants:
    max_cd.append(i[0] * 24)
    now_cd.append(i[1] * 24)
    price.append(i[2])
    statu_p.append(i[3])
    statu_b.append(i[4])


    """#     0    1    2    3    4    5    6    7
max_cd  =[120, 120, 480, 360, 240, 720, 240, 600]#植物最大冷缩
now_cd  =[0  , 120, 0  , 0  , 0  , 0  , 0  , 0  ]#当前已冷缩
price   =[100, 50 , 50 , 25 , 150, 150, 175, 125]#植物价格
statu_p =[1  , 2  , 3  , 3  , 3  , 2  , 1  , 2  ]#植物共有几种状态
statu_b =[2  , 1  , 0  , 0  , 0  , 0  , 2  , 0  ]#子弹共有几种状态"""


plant_offset_up = 30#植物位置偏移（向上）
zombies_offset_up = 20#僵尸位置偏移（向上）

win_distance_zombies = 160#僵尸胜利距离

#图片批量加载函数
def load_image(path):
    image_list = []
    for list in os.walk(path):
        for i in list[2]:
            image_list.append(pygame.image.load(path + "/" + i))
    return image_list

def load_image0(path, size):
    image_list = []
    for list in os.walk(path):
        for i in list[2]:
            image = pygame.image.load(path + "/" + i)
            image_list.append(pygame.transform.scale(image, size))
    return image_list


def load_card(card, i):
    path0 = "game_picture/plants/card/card" + str(i) + "/0.png"
    path1 = "game_picture/plants/card/card" + str(i) + "/1.png"
    path2 = "game_picture/plants/card/card" + str(i) + "/2.png"
    s0 = "pygame.image.load(path0)"
    s1 = "pygame.image.load(path1)"
    s2 = "pygame.image.load(path2)"
    im0 = eval(s0)
    im1 = eval(s1)
    im2 = eval(s2)
    im = [im0, im1, im2]
    card.append(im)


def pos_conversion_p(pos, size):    #将植物坐标转为图片显示坐标pos植物坐标, size图片尺寸
    return [pos[0] - size[0] // 2, pos[1] - size[1]]


def pos_conversion_z(pos, size, w): #将僵尸坐标转为图片显示坐标pos植物坐标, size图片尺寸
    return [pos[0] - size[0] // 2 - w, pos[1] - size[1]]

#图片
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("植物大战僵尸")
im_load = pygame.image.load("game_picture/background/game_load.png").convert_alpha()
bg_map1_0 = pygame.image.load("game_picture/background/background1.0.png").convert_alpha()  # 加载图片
bg_map1_1 = pygame.image.load("game_picture/background/background1.1.png").convert_alpha()
bg_map1_2 = pygame.image.load("game_picture/background/background1.2.png").convert_alpha()
bg_map1_3 = pygame.image.load("game_picture/background/background1.3.png").convert_alpha()
bg_map2 = pygame.image.load("game_picture/background/background2.png").convert_alpha()
bg_card = pygame.image.load("game_picture/background/bg_card.png").convert_alpha()
button_start = pygame.image.load("game_picture/background/button_start.png").convert_alpha()  # 开始按钮图片
bg_timeout = pygame.image.load("game_picture/background/bg_timeout.png").convert_alpha()
im_button = pygame.image.load("game_picture/background/button.png").convert_alpha()
im_button0 = pygame.image.load("game_picture/background/button0.png").convert_alpha()
im_start = load_image("game_picture/background/start")
im_warehouse = pygame.image.load("game_picture/background/sun_warehouse.png").convert_alpha()
bg_shovel = pygame.image.load("game_picture/background/shovel0.png").convert_alpha()
im_shovel = pygame.image.load("game_picture/background/shovel1.png").convert_alpha()
bg_level = pygame.image.load("game_picture/background/bg_level.png").convert_alpha()
im_ice = pygame.image.load("game_picture/background/ice0.png").convert_alpha()
im_ice = pygame.transform.scale(im_ice, (20, 20))  # 改变尺寸
im_lose = pygame.image.load("game_picture/background/lose.png").convert_alpha()
im_win = pygame.image.load("game_picture/background/win.png").convert_alpha()
im_group_attack = pygame.image.load("game_picture/background/group_attack.png").convert_alpha()
im_last_attack = pygame.image.load("game_picture/background/last_attack.png").convert_alpha()
im_attack_process_component0 = pygame.image.load("game_picture/background/attack_process/0.png").convert_alpha()
im_attack_process_component1 = pygame.image.load("game_picture/background/attack_process/1.png").convert_alpha()
im_attack_process_component2 = pygame.image.load("game_picture/background/attack_process/2.png").convert_alpha()
im_attack_process_component3 = pygame.image.load("game_picture/background/attack_process/3.png").convert_alpha()
im_attack_process_component4 = pygame.image.load("game_picture/background/attack_process/4.png").convert_alpha()
im_speed_up0 = pygame.image.load("game_picture/background/speed_up0.png").convert_alpha()
im_speed_up1 = pygame.image.load("game_picture/background/speed_up1.png").convert_alpha()
card = []  # 植物卡片图片
for i in range(species):  # 遍历成员加载图片
    load_card(card, i)

