import random, pygame, os, sys

colours = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "purple": (255, 0, 255)
}





w, h = 800, 600
fps = 30

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'frog.png')).convert()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (w / 2, h / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > w:
            self.rect.right = 0

sprites = pygame.sprite.Group()
player = Player()
sprites.add(player)

run = True
while run:
    clock.tick(fps)
    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update
    sprites.update()

    # Draw
    screen.fill(colours["blue"])
    sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
