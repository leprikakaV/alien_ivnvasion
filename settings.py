class Settings():
    """"Класс для хранения настрое игры Alien Invasion"""

    def __init__(self):
        """"Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_wigth = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # настройки корабля
        self.ship_limit = 3

        # параметры пули
        self.bullet_wight = 600
        self.bullet_height = 15
        self.bullet_color = (60, 0, 0)
        self.bullets_allowed = 4

        # Настройка пришельцев
        self.fleet_drop_speed = 10

        # Темп ускорение игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельца
        self.score_scale = 1.5
        # Подсчет очков

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.4
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.score_scale)
