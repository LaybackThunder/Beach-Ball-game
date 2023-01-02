import pygame

class HUD():
    """A class to report information to the player."""

    def __init__(self, client):
        """Initialize head up diplay attributes."""
        self.screen = client.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = client.settings
        self.game_stats = client.game_stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()
    
    def prep_score(self):
        """Turn the score into a rendered image."""
        self.score_text = self.font.render(f"Score: {self.game_stats.score}", 
        True, self.text_color, (0, 0, 0))
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_text.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_text, self.score_rect)