class Settings():
    """"Класс для хранения настрое игры Alien Invasion"""

    def __init__(self):
        """"Инициализирует настройки игры"""
        #Параметры экрана
        self.screen_wigth = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # настройки корабля
        self.ship_speed_factor = 1.5

        # параметры пули
        self.bullet_speed_factor = 1
        self.bullet_wight = 3
        self.bullet_height = 15
        self.bullet_color = (60, 0, 0)
        self.bullets_allowed = 4
