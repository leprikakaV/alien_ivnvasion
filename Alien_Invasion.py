import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    # Инициация игры и создания объекта экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_wigth,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(ai_settings)  # Создание экземпляра для хранения игровой статистики.
    ship = Ship(ai_settings, screen)  # Создаем корабль
    bullets = Group()  # Создание группы для хранения пуль.
    aliens = Group()  # Создание группы для пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)




run_game()
