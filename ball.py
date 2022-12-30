import pygame, random

from settings import Settings

class Ball():
    """A class to manage a ship."""

    def __init__(self, client):
        """Initialize ball and set its starting position"""
        self.screen = client.screen # Access game window
        self.settings = client.settings # Access game's settings through the client
        self.screen_rect = self.screen.get_rect() # Get it's rect

        # Load the ball and get it's rect.
        self.image = pygame.image.load('catch_the_ball\_beach_ball.bmp')
        self.rect = self.image.get_rect()

        # Starting each new ball in the middle of the screen.
        self.center_the_ball()

        # Ball direction
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])

        # Ball coordinates for smooth incremental movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Ball's movement
        self.velocity = [self.x, self.y]
        
    def update(self):
        """Updates object's behavior"""
        # Speed & Direction = Velocity
        self.x = self.settings.ball_speed * self.dx
        self.y = self.settings.ball_speed * self.dy
        # Give velocity its values
        self.velocity[0] = self.x 
        self.velocity[1] = self.y 
        # Ball's velocity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def change_ball_x_direction(self):
        """Changes ball's x direction."""
        self.dx *= -1

    def change_ball_y_direction(self):
        """Change the ball's y direction."""
        self.dy *= -1

    def center_the_ball(self):
        """Centers the ball in the middle."""
        MIDDLE_OF_THE_SCREEN = self.screen_rect.center # Screen Coordinates
        self.rect.center = MIDDLE_OF_THE_SCREEN # Ball gets coordinates
    
    def blitme(self):
        """Draw ball at its current location."""
        self.screen.blit(self.image, self.rect)