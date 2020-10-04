from parameter import *


#火辣椒
class Plant7:
    def __init__(self, ranks):
        self.id = 7           #植物编号 土豆地雷
        self.exist = 1  # 是否存在
        self.max_HP = 0
        self.HP = self.max_HP           #植物血量
        self.hurt = 400
        self.frame = 0          #帧
        self.actions = 0        #动作状态0-11
        self.normal_fs = 3  # 正常每张图片播放几帧
        self.fs = self.normal_fs  # 每张图片播放几帧
        self.status = 0         #行为状态：0-生长，1-成熟，3-攻击
        self.ranks = ranks          #位置行列
        self.r = -1
        self.r1 = ranks[0]
        self.im0 = load_image("game_picture/plants/plant7/0")
        self.im1 = load_image("game_picture/plants/plant7/1")
        for i in range(len(self.im1)):
            self.im1[i] = pygame.transform.scale(self.im1[i], (972, 66))
        self.im = [self.im0, self.im1]
        self.image = self.im[self.status][self.actions]
        self.size = []  # 不同状态下的大小
        for i in self.im:
            self.size.append(i[0].get_size())
        self.pos = [(self.ranks[1] + 0.5) * lawn_cube_size[0] + pos_lawn[0],
                    (self.ranks[0] + 1) * lawn_cube_size[1] + pos_lawn[1] - plant_offset_up]  # 实际位置
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])  # 图片显示位置

    def action(self, model):
        if self.status == 0:
            self.actions = self.frame // 3
            self.frame += 1
            if self.frame == len(self.im0) * 3:
                self.status = 1
                self.actions = 0
                self.frame = 0
                self.pos[0] = pos_lawn[0]
                self.pos[1] += 10
                for i in model.zombies:
                    if self.r1 == i.r and i.HP > 0:
                        i.HP -= self.hurt
                        if i.HP <= 0:
                            i.status = 0
                            i.actions = 0
        else:
            self.actions = self.frame // 4
            self.frame += 1
            if self.frame == len(self.im1) * 4:
                self.exist = 0
        self.image = self.im[self.status][self.actions]
        if self.status == 0:
            self.pos0 = pos_conversion_p(self.pos, self.size[self.status])  # 图片显示位置
        else:
            self.pos0 = pos_conversion_p(self.pos, self.size[self.status])  # 图片显示位置
            self.pos0[0] = pos_lawn[0] - 20

Plant7((1, 1))