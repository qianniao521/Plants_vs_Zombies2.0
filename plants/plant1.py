from bullets.bullet1 import *
from parameter import *


#向日葵
class Plant1:
    def __init__(self, ranks):
        self.id = 1           #植物编号 向日葵
        self.exist = 1          #是否存在
        self.HP = 100           #植物血量
        self.frame = 0          #帧
        self.actions = 0        #动作状态
        self.normal_fs = 3  # 正常每张图片播放几帧
        self.fs = self.normal_fs  # 每张图片播放几帧
        self.status = 0         #行为状态：0-等待，2-攻击
        self.ranks = ranks          #位置行列
        self.r = ranks[0]
        self.attack_interval = 240  #攻速,最大攻击间隔
        self.now_interval= self.attack_interval             #当前攻击间隔
        self.im0 = load_image("game_picture/plants/plant1/0")
        self.im1 = load_image("game_picture/plants/plant1/1")
        self.im = [self.im0, self.im1]
        self.image = self.im[self.status][self.actions]
        self.size = []  # 不同状态下的大小
        for i in self.im:
            self.size.append(i[0].get_size())
        self.pos = [(self.ranks[1] + 0.5) * lawn_cube_size[0] + pos_lawn[0],
                    (self.ranks[0] + 1) * lawn_cube_size[1] + pos_lawn[1] - plant_offset_up]  # 实际位置
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])# 图片显示位置

    def action(self, model):
        if self.HP <= 0:
            self.exist = 0
            return
        self.attack(model.bullets)
        if self.frame == 0:
            self.actions = (self.actions + 1) % len(self.im[self.status])
        self.frame = (self.frame + 1) % self.fs
        self.image = self.im[self.status][self.actions]
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])# 图片显示位置
    def attack(self, bullets):
        if self.now_interval <= 0:
            self.add_bullet(bullets)
            self.now_interval = self.attack_interval
        else:
            self.now_interval -= 1
        if self.now_interval <= 6:
            self.status = 1
        else:
            self.status = 0

    def add_bullet(self, bullets):
        bullets.append(Bullet1(self.ranks))


Plant1((1, 1))