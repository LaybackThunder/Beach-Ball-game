import pygame, sys, time

from settings import Settings
from ball import Ball
from game_stats import GameStats
from button import Button
from hud import HUD

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
        self.screen_rect = self.screen.get_rect()

        # Instanciate objects
        self.game_stats = GameStats(self) # Acess stats
        self.hud = HUD(self)
        self.play_button = Button(self, "Play") # Make play button
        self.ball = Ball(self) # Craete a beach ball

        # Clock
        self.clock = pygame.time.Clock()
        self.FPS = 60

    # Run game method
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events() # Keyboard & mouse events

            if self.game_stats.active_game: # Game logic
                self._check_ball_update()

            self._update_screen() # Graphical game projections
            self.clock.tick(self.FPS) # Controls how was the game processes

    # Helper methods 
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            self._check_buttondown_events(event)

    def _check_buttondown_events(self, event):
        """Checks all button down events."""
        # Quit game when pressing the "q" key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

        # Check if click was on ball
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if self.play_button.play_button_hide:
                self._check_click_ball(mouse_pos)
            
            if not self.play_button.play_button_hide:
                self._check_play_button(mouse_pos)
            
    def _check_play_button(self, mouse_pos):
        """Start new game when the player clicks Play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self._reset_game() # Reset stats: lives, score
            self.game_stats.active_game = True # Turn the game logic on  
            self.play_button.play_button_hide = True
            
    def _check_ball_update(self):
        """Check for ball update and its collitions."""
        self.ball.update()
        self._check_collition()

    def _check_collition(self):
        """Ball bounces if it hits the walls or floor or ceiling."""
        # Walls
        if self.ball.rect.left <= 0 or self.ball.rect.right >= self.settings.SCREEN_WIDTH:
            self.ball.change_ball_x_direction()
        # Floor and ceiling
        if self.ball.rect.top <= 0 or self.ball.rect.bottom >= self.settings.SCREEN_HEIGHT:
            self.ball.change_ball_y_direction()

    def _check_click_ball(self, mouse_pos):
        """Change ball direction when ball gets clicked, 
        click out side the ball and player gets damaged."""
        if self.ball.rect.collidepoint(mouse_pos): 
            self._ball_got_clicked() # Get points
        else:
            self.player_damage() # Damage player
            self._is_game_over() # Check for game over

    def _ball_got_clicked(self):
            # change ball x and y directions
            self.ball.change_ball_x_direction()
            self.ball.change_ball_y_direction()
            # Accelerate the ball
            self.ball_acceleration()
            # Playe gained one point
            self.score()

    def _is_game_over(self):
        """Checks if its game over."""
        if self.game_stats.lives_left <= 0:
            self.game_stats.active_game = False # turn game logic off
            self.game_over() # Display game over graphics

    def _reset_game(self):
        """Reset stats and ball vlocity."""
        self.game_stats.reset_stats()
        self.reset_ball_velocity()
        self.ball.center_the_ball()
        
    def _update_screen(self):
        """Update images on teh screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop 
        self.screen.fill(self.settings.BACKGROUND_COLOR)
        # Display score
        self.hud.show_score() 
        # Draw beach ball
        self.ball.blitme()
        if not self.game_stats.active_game:
            self.play_button.play_button_hide = False # Button not hidden
            self.play_button.draw_button() # Draw play button
             
        # Make most recently drawn screen visible; like animation
        pygame.display.flip()
    
    # Methods
    def game_over(self):
        """Game over graphics."""
        print("Game Over!")

    def player_damage(self): 
        """Inflict one damage to player's life count."""
        self.game_stats.lives_left -= 1
        print('hit')
        time.sleep(1.5)

    def score(self):
        """Give player one point."""
        self.game_stats.score += 1
        print(self.game_stats.score)

    def reset_ball_velocity(self):
        """Reset ball velocity."""
        self.settings.ball_speed = self.settings.STARTING_BALL_SPEED

    def ball_acceleration(self):
        """Add acceleration to ball."""
        self.settings.ball_speed += self.settings.ball_acceleration



if __name__ == '__main__':
    # Make game instance and run the game.
    client = Client()
    client.run_game()