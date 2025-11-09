import sys, pygame

pygame.init()

class Screen:
    def __init__(self, size, black):
        self._size = size # 320, 240
        self._black = black # (0, 0, 0)
        self._screen = pygame.display.set_mode(size)

    # Public Functions
    def get_size(self):
        return self._size
    def get_background(self):
        return self._black
    def get_screen(self):
        return self._screen


class Ball:
    def __init__(self, screen_size):
        self._ball = pygame.image.load("OOPPractice/intro_ball.gif")
        self._rect = self._ball.get_rect()
        self._speed = [2, 2]
        self._screen_size = screen_size

    # Public Functions
    def move(self):
        self._rect = self._rect.move(self._speed) # why?
        if self._rect.left < 0 or self._rect.right > self._screen_size[0]:
            self._speed[0] = -self._speed[0]
        if self._rect.top < 0 or self._rect.bottom > self._screen_size[1]:
            self._speed[1] = -self._speed[1]

    def draw(self, screen_for_ball):
        screen_for_ball.blit(self._ball, self._rect)


class Game:
    def __init__(self, screen, ball):
        self._screen = screen
        self._ball = ball

    def game_loop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()


            self._ball.move()

            self._screen.get_screen().fill(self._screen.get_background())
        
            self._ball.draw(self._screen.get_screen())
        

            pygame.display.flip()
            pygame.time.wait(1)



if __name__ == "__main__":  
    screen = Screen((320, 240), (0, 0, 0))
    ball = Ball(screen.get_size())
    game= Game(screen, ball)
    game.game_loop()