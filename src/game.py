import pygame
import sys
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 400))
        pygame.key.set_repeat(20)
        pygame.display.set_caption("WYZARDS")
        self.clock = pygame.time.Clock()
        self.running = True
        self.FPS = 60
        self.level = Level('assets/level/level1.txt')

    def update(self, event):
        self.level.update(event)

    def update_render(self):
        self.window.fill('red')
        self.level.update_render(self.window)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.update(event)

            self.update_render()
            self.clock.tick(self.FPS)
            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
