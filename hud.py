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
        self.text_bg_color = (255, 234, 0)
        self.font = pygame.font.Font("catch_the_ball\BeachOcean-MVGOw.otf", 48)

        # Display HUD on screen
        self.display_hud = False

        # Prepare the initial score image.
        self.prep_score()
        self.prep_lives()
        self.prep_wall_counter()
    
    def prep_score(self):
        """Turn the score into a rendered image."""
        self.score_text = self.font.render(f"Score: {self.game_stats.score}", 
        True, self.text_color, self.text_bg_color)
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_text.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        """Draw score to the screen."""
        self.score_text = self.font.render(f"Score: {self.game_stats.score}", 
        True, self.text_color, (255, 234, 0))
        self.screen.blit(self.score_text, self.score_rect)
    
    def prep_lives(self):
        """Turn the lives into a rendered image."""
        self.lives_left_text = self.font.render(f"Lives: {self.game_stats.lives_left}", 
        True, self.text_color, self.text_bg_color)
        
        # Display the score at the top right of the screen.
        self.lives_left_rect = self.lives_left_text.get_rect()
        self.lives_left_rect.left = self.screen_rect.left + 20
        self.lives_left_rect.top = 20
    
    def show_lives_left(self):
        """Draw score to the screen."""
        self.lives_left_text = self.font.render(f"Lives: {self.game_stats.lives_left}", 
        True, self.text_color, self.text_bg_color)
        self.screen.blit(self.lives_left_text, self.lives_left_rect)

    def prep_wall_counter(self):
        """Turn the lives into a rendered image."""
        self.wall_counter_text = self.font.render(f"Counter: {self.game_stats.counter}", 
        True, self.text_color, self.text_bg_color)
            
        # Display the counter at the top right of the screen.
        self.wall_counter_rect = self.wall_counter_text.get_rect()
        self.wall_counter_rect.midtop = self.screen_rect.midtop
        self.wall_counter_rect.top = 20
    
    def show_wall_counter(self):
        """Draw score to the screen."""
        self.wall_counter_text = self.font.render(f"Counter: {self.game_stats.counter}", 
        True, self.text_color, self.text_bg_color)
        self.screen.blit(self.wall_counter_text, self.wall_counter_rect)

    def _show_hud(self):
        """Display hud elements on screen."""
        self.show_score()
        self.show_lives_left()
        self.show_wall_counter()