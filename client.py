import pygame, sys

from settings import Settings

class Client():
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Pygame screen
        self.screen = pygame.display.set_mode(
            (self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        pygame.display.set_caption('Beach Ball')

        self.LIGHT_GRAY = (230, 230, 230)
        self.BACKGROUND_COLOR = (self.LIGHT_GRAY)

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Light gray background
            self.screen.fill(self.settings.BACKGROUND_COLOR)
            
            # Make most recently drawn screen visible
            pygame.display.update()



if __name__ == '__main__':
    # Make game instance and run the game.
    client = Client()
    client.run_game()