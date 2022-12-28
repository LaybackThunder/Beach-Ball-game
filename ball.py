import pygame

class Ball():
    """A class to manage a ship."""

    def __init__(self, client):
        """Initialize ball and set its starting position"""
        self.screen = client.screen # Access game window
        self.screen_rect = self.screen.get_rect() # Get it's rect

        # Load the ball and get it's rect.
        self.image = pygame.image.load('catch_the_ball\_beach_ball.bmp')
        self.rect = self.image.get_rect()

        # Starting each new ball in the middle of the screen.
        self.center_the_ball()

    def center_the_ball(self):
        """Centers the ball in the middle."""
        MIDDLE_OF_THE_SCREEN = self.screen_rect.center # Screen Coordinates
        self.rect.center = MIDDLE_OF_THE_SCREEN # Ball gets coordinates
    
    def blitme(self):
        """Draw ball at its current location."""
        self.screen.blit(self.image, self.rect)