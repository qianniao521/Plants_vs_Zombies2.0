
from parameter import *


#坚果墙
class Plant2:
    def __init__(self, ranks):
        self.id = 2           #植物编号 坚果墙
        self.exist = 1          #是否存在
        self.max_HP = 1600
        self.HP = self.max_HP           #植物血量
        self.HP0 = self.max_HP * 3 // 5
        self.HP1 = self.max_HP * 3 // 10
        self.frame = 0          #帧
        self.actions = 0        #动作状态0-11
        self.normal_fs = 3  # 正常每张图片播放几帧
        self.fs = self.normal_fs  # 每张图片播放几帧
        self.status = 0         #行为状态：0-等待，1-攻击
        self.ranks = ranks          #位置行列
        self.r = ranks[0]
        self.attack_interval = 144  #攻速,最大攻击间隔
        self.now_interval= self.attack_interval             #当前攻击间隔
        self.im0 = load_image("game_picture/plants/plant2/0")
        self.im1 = load_image("game_picture/plants/plant2/1")
        self.im2 = load_image("game_picture/plants/plant2/2")
        self.im = [self.im0, self.im1, self.im2]
        self.image = self.im[self.status][self.actions]
        self.size = []  # 不同状态下的大小
        for i in self.im:
            self.size.append(i[0].get_size())
        self.pos = [(self.ranks[1] + 0.5) * lawn_cube_size[0] + pos_lawn[0],
                    (self.ranks[0] + 1) * lawn_cube_size[1] + pos_lawn[1] - plant_offset_up]  # 实际位置
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])

    def action(self, model):
        if self.HP <= 0:
            self.exist = 0
            return
        if self.status == 0:
            if self.HP < self.HP0:
                self.status = 1
                self.actions = 0
        elif self.status == 1:
            if self.HP < self.HP1:
                self.status = 2
                self.actions = 0
        if self.frame == 0:
            self.actions = (self.actions + 1) % len(self.im[self.status])
        self.frame = (self.frame + 1) % self.fs
        self.image = self.im[self.status][self.actions]
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])  # 图片显示位置


Plant2((1, 1))