import pygame

class Game:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.turel = self.turel
        self.image = pygame.image.load('img/torel.png')









WIDTH, HEIGHT = 1000, 1000
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("brick breaker")
FPS = 60
BACKGROUND_COLOR = pygame.Color('white')


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    win.fill(BACKGROUND_COLOR)

if __name__ == "__main__":
    main()





