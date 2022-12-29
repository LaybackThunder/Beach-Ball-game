import pygame, sys

from settings import Settings
from ball import Ball

class Client():
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() # Instantiate pygame modules
        self.settings = Settings() # Instance Settings

        # Pygame screen
        self.screen = pygame.display.set_mode(
            (self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        pygame.display.set_caption('Beach Ball') # Add string to top of game's window

        # Instanciate objects
        self.ball = Ball(self)

        # Colors and background color
        self.LIGHT_GRAY = (230, 230, 230)
        self.BACKGROUND_COLOR = (self.LIGHT_GRAY)

        # Clock
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ball.update()
            self._update_screen()  
            self.clock.tick(self.FPS)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on teh screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop 
        self.screen.fill(self.settings.BACKGROUND_COLOR)
        self.ball.blitme()

        # Make most recently drawn screen visible; like animation
        pygame.display.flip()

if __name__ == '__main__':
    # Make game instance and run the game.
    client = Client()
    client.run_game()