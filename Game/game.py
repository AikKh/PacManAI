import pygame, sys
from Game.pacman import PacMan
from Game.map import Map

BLACK = (0, 0, 0)
GREY = (127, 127, 127)
WHITE = (255, 255, 255)


class Game:

    FPS = 12
    Size = 20
    
    def __init__(self):
        self._screen = pygame.display.set_mode((Map.Width * Game.Size, Map.Height * Game.Size))
        self._clock = pygame.time.Clock()
        self._all_sprites = pygame.sprite.Group()

        self._map = Map()
        self._pacman = PacMan(14, 23, self._map)

        pygame.display.set_caption("PacManAI")


    def run(self):
        s = Game.Size
        self._map.draw(Map.Wall, lambda x, y: pygame.draw.rect(self._screen, GREY, (x * s, y * s, s, s)))

        void_fn = lambda x, y: pygame.draw.rect(self._screen, BLACK, (x * s, y * s, s, s))
        point_fn = lambda x, y: pygame.draw.circle(self._screen, WHITE, (x * s + s // 2, y * s + s // 2), s // 5)

        while True:
            # self.all_sprites.draw(self.screen)

            # UI update
            self._clock.tick(Game.FPS)
            pygame.display.flip()

            # State update
            self._pacman.move()
            self._pacman.check_dir()

            # Drawing
            self._map.draw(Map.Void, void_fn)
            self._map.draw(Map.Point, point_fn)
            self._pacman.draw(self._screen, s)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self._pacman.turn(-1, 0)
                    if event.key == pygame.K_RIGHT:
                        self._pacman.turn(1, 0)
                    if event.key == pygame.K_UP:
                        self._pacman.turn(0, -1)
                    if event.key == pygame.K_DOWN:
                        self._pacman.turn(0, 1)