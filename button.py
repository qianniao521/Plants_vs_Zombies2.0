import sys
from pygame.locals import *
from plants.plants import *

import pygame

#选择界面按钮
class Button0:
    def __init__(self, game):
        self.game = game
        #self.member = []
        self.member = game.member
        self.pos0 = [pos_card_member[0], pos_card_member[1],
                     pos_card_member[0] + card_size[0], pos_card_member[1] + card_size[1] * card_num]#区域0已选择植物清单区域
        self.pos1 = [pos_card_select[0], pos_card_select[1],
                     pos_card_select[0] + card_select_size[0], pos_card_select[1] +card_select_size[1]]#区域1选择植物区
        self.pos2 = [pos_button_start[0], pos_button_start[1],
                     pos_button_start[0] + button_start_size[0], pos_button_start[1] + button_start_size[1]]#区域2确认按钮区
        self.pos3 = [pos_button_menu[0], pos_button_menu[1],
                     pos_button_menu[0] + button_size[0], pos_button_menu[1] + button_size[1]]#区域3菜单区
        self.square = [[1, 1, 1, 1],
                       [1, 1, 1, 1],
                       [1, 1, 1, 1],
                       [1, 1, 1, 1],
                       [1, 1, 1, 1]]
        for i in range(species):
            m = i // 4
            n = i % 4
            if i + 1 >self.game.checkpoint:
                self.square[m][n] = 0

    def action(self, events):
        point_x, point_y = pygame.mouse.get_pos()
        if self.pos0[0] < point_x < self.pos0[2] and self.pos0[1] < point_y < self.pos0[3]:#区域0
            x = point_x - self.pos0[0]
            y = point_y - self.pos0[1]
            i = y // 60
            if i < len(self.member):
                surface0 = font2.render(str(price[self.member[i]]), False, font_color[1])
                screen.blit(card[self.member[i]][1], (20, 9 + 60 * i))
                screen.blit(surface0, (80, 49 + 60 * i))

            for event in events:
                if event.type == MOUSEBUTTONUP:
                    if i < len(self.member):
                        m = self.member[i] // 4
                        n = self.member[i] % 4
                        self.member.remove(self.member[i])
                        self.square[m][n] = 1

        elif self.pos1[0] < point_x < self.pos1[2] and self.pos1[1] < point_y < self.pos1[3]:#区域1
            x = point_x - self.pos1[0]
            y = point_y - self.pos1[1]
            m = y // 60
            n = x // 100
            i = m * 4 + n
            if i < species:
                if i + 1 > self.game.checkpoint:
                    pass
                elif i in self.member:
                    screen.blit(card[i][0],
                                (pos_card_select[0] + card_size[0] * n, pos_card_select[1] - 1 + card_size[1] * m))
                    surface0 = font2.render(str(price[i]), False, font_color[1])
                    screen.blit(surface0, (pos_card_select[0] + 60 + n * 100, pos_card_select[1] + 39 + 60 * m))
                else:
                    screen.blit(card[i][1], (pos_card_select[0] + card_size[0] * n, pos_card_select[1] - 1 + card_size[1] * m))
                    surface0 = font2.render(str(price[i]), False, font_color[1])
                    screen.blit(surface0, (pos_card_select[0] + 60 + n * 100, pos_card_select[1] + 39 + 60 * m))

            for event in events:
                if event.type == MOUSEBUTTONUP:
                    if i < species and self.square[m][n] == 1:
                        self.member.append(i)
                        self.square[m][n] = 0

        elif self.pos2[0] < point_x < self.pos2[2] and self.pos2[1] < point_y < self.pos2[3]:  # 区域2
            screen.blit(button_start, (pos_button_start[0], pos_button_start[1] - 1))
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    return 1
        elif self.pos3[0] < point_x < self.pos3[2] and self.pos3[1] < point_y < self.pos3[3]:  # 区域3
            screen.blit(im_button, (pos_button_menu[0], pos_button_menu[1] - 1))
            surface = font3.render("菜单", False, font_color[2])
            screen.blit(surface, (pos_button_menu[0] + 30, pos_button_menu[1] + 7))
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    self.game.run[0] = 0
            pass
        return 0

#战斗界面按钮
class Button1:
    def __init__(self, game):
        self.game = game
        self.menu = game.menu
        self.speed = game.speed #加速
        self.no = -1  # 编号
        self.run = game.run  #游戏运行状态0-暂停，1-进行
        self.pos0 = [pos_card_member[0], pos_card_member[1],
                     pos_card_member[0] + card_size[0], pos_card_member[1] + card_size[1] * len(game.member)]  # 区域0已选择植物清单区域
        if game.checkpoint <= 2:
            n = 3 - game.checkpoint
            self.pos1 = [pos_lawn[0], pos_lawn[1] + lawn_cube_size[1] * n,
                         pos_lawn[0] + lawn_size[0], pos_lawn[1] + lawn_cube_size[1] * (5 - n)]  # 区域1草坪
        else:
            self.pos1 = [pos_lawn[0], pos_lawn[1],
                         pos_lawn[0] + lawn_size[0], pos_lawn[1] + lawn_size[1]]  # 区域1草坪
        self.pos2 = [pos_bg_shovel[0], pos_bg_shovel[1],
                     pos_bg_shovel[0] + shovel_size[0], pos_bg_shovel[1] + shovel_size[1]]  # 区域2铲子
        self.pos3 = [pos_button_menu[0], pos_button_menu[1],
                     pos_button_menu[0] + button_size[0], pos_button_menu[1] + button_size[1]] #区域3菜单
        self.pos4 = [pos_im_speed_up[0], pos_im_speed_up[1],
                     pos_im_speed_up[0] + im_speed_up0.get_size()[0], pos_im_speed_up[1] + im_speed_up0.get_size()[1]]#区域4加速按钮
        self.square = game.square

    def action(self, events):
        if self.run == 0:
            return
        point_x, point_y = pygame.mouse.get_pos()
        if self.pos0[0] < point_x < self.pos0[2] and self.pos0[1] < point_y < self.pos0[3]:  # 区域0
            y = point_y - self.pos0[1]
            n = y // card_size[1]
            # 显示鼠标所在植物菜单卡片
            if self.menu.sunlight >= price[self.game.member[n]]:
                surface0 = font2.render(str(price[self.game.member[n]]), False, font_color[1])
                if self.menu.now_cd[self.game.member[n]] >= max_cd[self.game.member[n]]:
                    screen.blit(card[self.game.member[n]][1],
                                (pos_card_member[0], pos_card_member[1] - 1 + card_size[1] * n))
                else:
                    screen.blit(card[self.game.member[n]][0],
                                (pos_card_member[0], pos_card_member[1] - 1 + card_size[1] * n))
            else:
                surface0 = font2.render(str(price[self.game.member[n]]), False, font_color[0])
                screen.blit(card[self.game.member[n]][0],
                            (pos_card_member[0], pos_card_member[1] - 1 + card_size[1] * n))
            screen.blit(surface0, (pos_card_member[0] + 60, pos_card_member[1] + 39 + card_size[1] * n))
            # 响应点击事件
            for event in events:
                if event.type == MOUSEBUTTONUP:# 鼠标是否在植物菜单点击
                    if self.menu.now_cd[self.game.member[n]] >= max_cd[self.game.member[n]] \
                            and self.menu.sunlight >= price[self.menu.member[n]]:
                        self.no = n if self.no != n else -1
                    else:
                        self.no = -1

        elif self.pos1[0] < point_x < self.pos1[2] and self.pos1[1] < point_y < self.pos1[3]:  # 区域1
            for event in events:
                if event.type == MOUSEBUTTONUP and self.no != -1:
                    x = point_x - pos_lawn[0]
                    y = point_y - pos_lawn[1]
                    m = y // lawn_cube_size[1]
                    n = x // lawn_cube_size[0]
                    if self.square[m][n] == 0:
                        if 0 <= self.no < self.menu.num and self.menu.sunlight >= price[self.menu.member[self.no]]:
                            i = self.menu.member[self.no]
                            s = "self.game.model.plants.append(Plant" + str(i) + "((m, n)))"
                            # print(s)
                            eval(s)
                            self.menu.sunlight -= price[self.menu.member[self.no]]
                            self.menu.now_cd[self.menu.member[self.no]] = 0
                            self.square[m][n] = 1
                        self.no = -1
                    elif self.no == -2:
                        for i in self.game.model.plants:
                            if i.ranks[0] == m and i.ranks[1] == n:
                                i.HP = 0
                                self.square[m][n] = 0
                                break
                        self.no = -1
                    else:
                        self.no = -1

        elif self.pos2[0] < point_x < self.pos2[2] and self.pos2[1] < point_y < self.pos2[3]:  # 区域2
            screen.blit(bg_shovel, (pos_bg_shovel[0], pos_bg_shovel[1] - 1))
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    self.no = -1 if self.no == -2 else -2

        elif self.pos3[0] < point_x < self.pos3[2] and self.pos3[1] < point_y < self.pos3[3]:  # 区域3
            screen.blit(im_button, (pos_button_menu[0], pos_button_menu[1] - 1))  # 显示菜单按钮
            surface = font3.render("菜单", False, font_color[2])
            screen.blit(surface, (pos_button_menu[0] + 30, pos_button_menu[1] + 7))
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    self.run[0] = 0
            pass

        elif self.pos4[0] < point_x < self.pos4[2] and self.pos4[1] < point_y < self.pos4[3]:  # 区域4
            if self.speed[0] == 1:
                screen.blit(im_speed_up0, (pos_im_speed_up[0], pos_im_speed_up[1] - 1))  #显示加速按钮
            else:
                screen.blit(im_speed_up1, (pos_im_speed_up[0], pos_im_speed_up[1] - 1))  #显示加速按钮
            surface = font3.render("X" + str(self.speed[0]), False, font_color[2])
            screen.blit(surface, (self.pos4[2] + 2, self.pos4[1] + 4))
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    self.game.speed[0] = self.speed[0] % self.game.max_speed + 1
            pass

        else:
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    self.no = -1

        if 0 <= self.no < self.menu.num and self.menu.sunlight >= price[self.game.member[self.no]]:  # 显示鼠标跟随卡片
            size = card[self.game.member[self.no]][2].get_size()
            screen.blit(card[self.game.member[self.no]][2], (point_x - size[0] // 2, point_y - size[1] // 2))
        elif self.no == -2:
            size = im_shovel.get_size()
            screen.blit(im_shovel, (point_x - size[0] // 2, point_y - size[1] // 2))


#结束界面按钮
class Button2:
    def __init__(self, game):
        self.game = game
        self.menu = game.model.menu
        self.pos0 = [900, 200, 1012, 240]#区域0重新开始
        self.pos1 = [900, 400, 1012, 440]#区域1

    def action(self, events):
        point_x, point_y = pygame.mouse.get_pos()
        if self.pos0[0] < point_x < self.pos0[2] and self.pos0[1] < point_y < self.pos0[3]:  # 区域0
            screen.blit(im_button, (pos_im_over_button0[0], pos_im_over_button0[1] - 1))  # 选择按钮1
            surface = font3.render("重新开始", False, font_color[2])
            screen.blit(surface, (pos_im_over_button0[0] + 10, pos_im_over_button0[1] + 7))
            # 响应点击事件
            for event in events:
                if event.type == MOUSEBUTTONUP:# 鼠标是否在植物菜单点击
                    return 0

        elif self.pos1[0] < point_x < self.pos1[2] and self.pos1[1] < point_y < self.pos1[3]:  # 区域1
            screen.blit(im_button, (pos_im_over_button1[0], pos_im_over_button1[1] - 1))  # 选择按钮1
            if self.game.model.win[0] == 1:
                surface = font3.render("下一关卡", False, font_color[2])
            else:
                surface = font3.render("退出游戏", False, font_color[2])
            screen.blit(surface, (pos_im_over_button1[0] + 10, pos_im_over_button1[1] + 7))
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    return 1
        else:
            return -1


#暂停界面按钮
class Button3:
    def __init__(self, game):
        self.game = game
        self.pos0 = [pos_im_menu_button0[0], pos_im_menu_button0[1],
                     pos_im_menu_button0[0] + button_size[0], pos_im_menu_button0[1] + button_size[1]]#区域0
        self.pos1 = [pos_im_menu_button1[0], pos_im_menu_button1[1],
                     pos_im_menu_button1[0] + button_size[0], pos_im_menu_button1[1] + button_size[1]]#区域1
        self.pos2 = [pos_im_menu_button2[0], pos_im_menu_button2[1],
                     pos_im_menu_button2[0] + button_size[0], pos_im_menu_button2[1] + button_size[1]]#区域2
        self.pos3 = [pos_im_menu_button3[0], pos_im_menu_button3[1],
                     pos_im_menu_button3[0] + button_size[0], pos_im_menu_button3[1] + button_size[1]]#区域2

    def action(self, events):
        point_x, point_y = pygame.mouse.get_pos()
        if self.pos0[0] < point_x < self.pos0[2] and self.pos0[1] < point_y < self.pos0[3]:  # 区域0
            screen.blit(im_button, (pos_im_menu_button0[0], pos_im_menu_button0[1] - 1))  # 选择按钮0
            surface = font3.render("重新开始", False, font_color[2])
            screen.blit(surface, (pos_im_menu_button0[0] + 10, pos_im_menu_button0[1] + 7))
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    self.game.run[0] = 1
                    self.game.member = []
                    self.game.game_slect()

        elif self.pos1[0] < point_x < self.pos1[2] and self.pos1[1] < point_y < self.pos1[3]:  # 区域1
            screen.blit(im_button, (pos_im_menu_button1[0], pos_im_menu_button1[1] - 1))  # 选择按钮1
            surface = font3.render("继续游戏", False, font_color[2])
            screen.blit(surface, (pos_im_menu_button1[0] + 10, pos_im_menu_button1[1] + 7))
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    self.game.run[0] = 1
                    return 1

        elif self.pos2[0] < point_x < self.pos2[2] and self.pos2[1] < point_y < self.pos2[3]:  # 区域2
            screen.blit(im_button, (pos_im_menu_button2[0], pos_im_menu_button2[1] - 1))  # 选择按钮2
            surface = font3.render("退出游戏", False, font_color[2])
            screen.blit(surface, (pos_im_menu_button2[0] + 10, pos_im_menu_button2[1] + 7))
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    pygame.quit()
                    sys.exit()

        elif self.pos3[0] < point_x < self.pos3[2] and self.pos3[1] < point_y < self.pos3[3]:  # 区域3
            screen.blit(im_button, (pos_im_menu_button3[0], pos_im_menu_button3[1] - 1))  # 选择按钮3
            surface = font3.render("选择关卡", False, font_color[2])
            screen.blit(surface, (pos_im_menu_button3[0] + 10, pos_im_menu_button3[1] + 7))
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    self.game.member = []
                    self.game.choose_level()

        return 0


#选关界面按钮
class Button4:
    def __init__(self, game):
        self.game = game
        self.pos0 = [pos_level_choose[0], pos_level_choose[1],
                     pos_level_choose[0] + level_choose_size[0], pos_level_choose[1] + level_choose_size[1]]  # 关卡选择区域
        self.pos1 = [pos_button_return[0], pos_button_return[1],
                     pos_button_return[0] + button_size[0], pos_button_return[1] + button_size[1]]#返回按钮

    def action(self, events):
        point_x, point_y = pygame.mouse.get_pos()
        if self.pos0[0] < point_x < self.pos0[2] and self.pos0[1] < point_y < self.pos0[3]:  # 区域0
            x = point_x - self.pos0[0]
            y = point_y - self.pos0[1]
            m = y // button0_size[1]
            n = x // button0_size[0]
            i = m * 6 + n
            screen.blit(im_button0, (pos_level_choose[0] + n * button0_size[0], pos_level_choose[1] - 1 + m * button0_size[1]))
            surface = font3.render(str(i + 1), False, font_color[2])
            screen.blit(surface, (pos_level_choose[0] + 10 + n * button0_size[0], pos_level_choose[1] -1 + 5 + m * button0_size[1]))
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    self.game.run[0] = 1
                    self.game.member = []
                    self.game.checkpoint = i + 1
                    self.game.game_slect()

        elif self.pos1[0] < point_x < self.pos1[2] and self.pos1[1] < point_y < self.pos1[3]:  # 区域1
            screen.blit(im_button, (pos_button_return[0], pos_button_return[1] - 1))
            surface = font3.render("返回游戏", False, font_color[2])
            screen.blit(surface, (pos_button_return[0] + 10, pos_button_return[1] + 7))
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    self.game.run[0] = 1
                    return 1

        return 0
