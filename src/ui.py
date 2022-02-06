import pygame


class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.SysFont('Arial', 15)

        self.health_bar_rect = pygame.Rect(10, 10, 200, 20)
        self.mana_bar_rect = pygame.Rect(10, 34, 120, 20)

    def show_bar(self, current, max_amount, bg_rect, color):
        pygame.draw.rect(self.display_surface, '#222222', bg_rect)

        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, '#292929', bg_rect, 3)

    def display(self, player):
        self.show_bar(player.health, player.stats["health"], self.health_bar_rect, "red")
        self.show_bar(player.mana, player.stats["mana"], self.mana_bar_rect, "blue")
