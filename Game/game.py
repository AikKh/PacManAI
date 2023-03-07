import pygame, sys
from Game.map import Map
from Game.vector import V2D
from Game.ghost import Ghost
from Game.pacman import PacMan
from Game.ChaseStrategies.blinky import Blinky

pygame.init()
pygame.font.init()

BLACK = (0, 0, 0)
GREY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Game:

    FPS = 12
    Size = 20
    
    def __init__(self):
        # Init UI
        pygame.display.set_caption("PacManAI")
        self._screen = pygame.display.set_mode((Map.Width * Game.Size, Map.Height * Game.Size + 60))
        self._clock = pygame.time.Clock()
        self._all_sprites = pygame.sprite.Group()
        self._font = pygame.font.SysFont("arial", 15)

        # Init sprites
        self._map = Map()
        self._pacman = PacMan(V2D(14, 23), self._map)
        
        self._blinky = Ghost(V2D(1, 1), self._pacman, RED, Blinky)


    def blit_score(self):
        text = f"Score: {self._pacman._points}"
        rendered = self._font.render(text, True, WHITE)
        self._screen.blit(rendered, (40, Map.Height * Game.Size + 10))


    def run(self):
        s = Game.Size
        
        wall_fn = lambda x, y: pygame.draw.rect(self._screen, BLUE, (x * s, y * s, s, s), 5)
        void_fn = lambda x, y: pygame.draw.rect(self._screen, BLACK, (x * s, y * s, s, s))
        point_fn = lambda x, y: pygame.draw.circle(self._screen, WHITE, (x * s + s // 2, y * s + s // 2), s // 5)

        while not self._pacman._is_dead:

            # UI update
            pygame.display.flip()
            self._clock.tick(Game.FPS)
            self._screen.fill(BLACK)

            # State update
            self._pacman.move()
            self._blinky.move()
            self._pacman.check_dir()

            # Drawing
            self._map.draw(Map.Wall, wall_fn)
            self._map.draw(Map.Void, void_fn)
            self._map.draw(Map.Point, point_fn)
            self._pacman.draw(self._screen, s)
            self._blinky.draw(self._screen, s)
            self.blit_score()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    k = event.key
                    if k == pygame.K_LEFT or k == pygame.K_a:
                        self._pacman.turn(-1, 0)
                    if k == pygame.K_RIGHT or k == pygame.K_d:
                        self._pacman.turn(1, 0)
                    if k == pygame.K_UP or k == pygame.K_w:
                        self._pacman.turn(0, -1)
                    if k == pygame.K_DOWN or k == pygame.K_s:
                        self._pacman.turn(0, 1)