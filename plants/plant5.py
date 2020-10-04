from parameter import *


#樱桃炸弹
class Plant5:
    def __init__(self, ranks):
        self.id = 5           #植物编号
        self.exist = 1  # 是否存在
        self.max_HP = 0
        self.HP = self.max_HP           #植物血量
        self.hurt = 800
        self.frame = 0          #帧
        self.time = 0
        self.actions = 0        #动作状态0-11
        self.normal_fs = 3  # 正常每张图片播放几帧
        self.fs = self.normal_fs  # 每张图片播放几帧
        self.status = 0         #行为状态：0-生长，1-成熟，3-攻击
        self.ranks = ranks          #位置行列
        self.r = -1
        self.r1 = ranks[0]
        self.im0 = load_image("game_picture/plants/plant5/0")
        self.im1 = load_image("game_picture/plants/plant5/1")
        self.im = [self.im0, self.im1]
        self.image = self.im[self.status][self.actions]
        self.size = []  # 不同状态下的大小
        for i in self.im:
            self.size.append(i[0].get_size())
        self.pos = [(self.ranks[1] + 0.5) * lawn_cube_size[0] + pos_lawn[0],
                    (self.ranks[0] + 1) * lawn_cube_size[1] + pos_lawn[1] - plant_offset_up]  # 实际位置
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])  # 图片显示位置
        self.attack_distance = 200  # 攻击距离
        self.attack_range = [(self.ranks[1] - 1.1) * lawn_cube_size[0] + pos_lawn[0],
                             (self.ranks[1] + 2.1) * lawn_cube_size[0] + pos_lawn[0]]  # 攻击范围

    def action(self, model):
        if self.status == 0:
            self.time += 1
            if self.time == len(self.im[self.status]) * self.fs - 1:
                self.status = 1
                self.actions = 0
                self.time = 0
                for i in model.zombies:
                    if self.r1 - 1 <= i.r <= self.r1 + 1 and i.HP > 0:
                        if self.attack_range[0] < i.pos[0] < self.attack_range[1]:
                            i.HP -= self.hurt
                            if i.HP <= 0:
                                i.status = 0
                                i.actions = 0
        else:
            self.time += 1
            if self.time == len(self.im[self.status]) * self.fs - 1:
                self.exist = 0
        if self.frame == 0:
            self.actions = (self.actions + 1) % len(self.im[self.status])
        self.frame = (self.frame + 1) % self.fs
        self.image = self.im[self.status][self.actions]
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])  # 图片显示位置


Plant5((1, 1))