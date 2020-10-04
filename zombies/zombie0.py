from parameter import *

class Zombie0:
    def __init__(self, r):
        self.id = 0            #类别
        self.max_HP = 200
        self.HP = self.max_HP           #血量
        self.exist = 1          #是否存在
        self.frame = 0          #帧
        self.actions = 0        #动作状态0-11
        self.status = 2         #行为状态：0-灰，1-死，2-走， 3-攻击, 4-
        self.r = r
        self.normal_speed = 0.6           #正常移速
        self.speed = self.normal_speed        #移速
        self.normal_fs = 3      #正常每张图片播放几帧
        self.fs = self.normal_fs             #每张图片播放几帧
        self.ice_time = -1    #冰冻减速时间
        self.im0 = load_image("game_picture/zombies/zombie1/0")
        self.im1 = load_image("game_picture/zombies/zombie1/1")
        self.im2 = load_image("game_picture/zombies/zombie0/2")
        self.im3 = load_image("game_picture/zombies/zombie0/3")
        self.im = [self.im0, self.im1, self.im2, self.im3]
        self.image = self.im[self.status][self.actions]
        self.size = []  # 不同状态下的大小
        for i in self.im:
            self.size.append(i[0].get_size())
        self.w = self.size[2][0] // 2 # 图片宽度，血条长度
        self.pos = [screen_size[0], (r + 1) * lawn_cube_size[1] + pos_lawn[1] - zombies_offset_up]  # 实际位置
        self.offset = self.size[2][0] // 6
        self.pos0 = pos_conversion_z(self.pos, self.size[self.status], self.offset) # 图片显示位置
        self.attack_power = 10  # 攻击力
        self.attack_distance = lawn_cube_size[0] // 2  # 攻击距离
        self.attack_range = [self.pos[0] - self.attack_distance, self.pos[0] + self.attack_distance]  # 攻击范围
        self.attack_interval = 12  # 攻速,最大攻击间隔
        self.now_interval = 0  # 当前攻击间隔


    def action(self, model):
        if self.HP <= 0 and self.status > 1:
            self.status = 1
            self.actions = 0
        elif self.status == 2:
            self.move()
            self.attack_range = [self.pos[0] - self.attack_distance, self.pos[0] + self.attack_distance]  # 攻击范围
            for i in range(len(model.plants)):
                if self.r == model.plants[i].r:
                    if self.attack_range[0] < model.plants[i].pos[0] < self.attack_range[1]:  # 攻击状态
                        self.status = 3
                        self.actions = 0
                        self.frame = 0
                        self.target = model.plants[i]
                        break
        elif self.status == 3:
            if self.target.exist == 1:
                self.attack()
            else:
                self.status = 2
                self.actions = 0
        elif self.status == 0:
            if self.actions == len(self.im[0]) - 1:
                self.exist = 0
        else:
            if self.actions == len(self.im[1]) - 1:
                self.exist = 0
        if self.frame == 0:
            self.actions = (self.actions + 1) % len(self.im[self.status])
        self.frame = (self.frame + 1) % self.fs
        self.image = self.im[self.status][self.actions]
        if self.status == 0:
            self.pos0 = pos_conversion_z(self.pos, self.size[self.status], 20)  # 图片显示位置
        if self.status == 1:
            self.pos0 = pos_conversion_z(self.pos, self.size[self.status], 20)  # 图片显示位置
        else:
            self.pos0 = pos_conversion_z(self.pos, self.size[self.status], self.offset) # 图片显示位置
        if self.ice_time >= 0:
            if self.ice_time <= 0:
                self.speed = self.normal_speed
                self.fs = self.normal_fs
            else:
                self.ice_time -= 1

    def move(self):
        self.pos[0] = self.pos[0] - self.speed

    def attack(self):
        if self.now_interval <= 0:
            self.target.HP -= self.attack_power
            self.now_interval = self.attack_interval
        else:
            self.now_interval -= 1


Zombie0(0)

