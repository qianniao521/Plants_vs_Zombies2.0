from parameter import *


class Menu:
    def __init__(self, member):
        self.sunlight = 75
        self.frame = 0
        self.sun_time = 240
        self.time = self.sun_time // 2
        self.now_cd = now_cd.copy()
        self.member = member  # 上阵成员
        self.num = len(self.member)  # 成员数量
        self.b_m = {}  # 子弹到menu中的映射
        self.p_m = {}  # 植物到menu中的映射

        for i in range(self.num):  # 实现
            self.p_m[self.member[i]] = i
            if statu_b[self.member[i]] > 0:
                self.b_m[self.member[i]] = len(self.b_m)
        self.font1 = pygame.font.SysFont("Arial Rounded MT Bold", 48)
        self.font2 = pygame.font.SysFont("Arial Rounded MT Bold", 24)
        self.font3 = pygame.font.SysFont("隶书", 24)
        self.font_color = [(200, 0, 0), (60, 60, 60), (0, 0, 0)]
        self.card = []  # 植物卡片图片
        self.image = []  # 植物状态图片
        self.bu_im = []  # 子弹状态图片
        for i in self.member:  # 遍历成员加载图片
            load_card(self.card, i)
            im = []
            for j in range(statu_p[i]):  # 遍历植物状态加载图片
                path = "game_picture/plants/plant" + str(i) + "/" + str(j)
                im.append(load_image(path))
            self.image.append(im)
            im = []
            for j in range(statu_b[i]):  # 遍历子弹状态加载图片
                path = "game_picture/plants/bullet" + str(i) + "/" + str(j)
                im.append(load_image(path))
            self.bu_im.append(im)

    def action(self):
        self.time += 1
        if self.time == self.sun_time:
            self.time = 0
            self.sunlight += 25
        for i in self.member:
            if self.now_cd[i] < max_cd[i]:
                self.now_cd[i] += 1
