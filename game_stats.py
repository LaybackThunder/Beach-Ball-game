class GameStats():
    """Track statistics  for Catch The Ball."""

    def __init__(self, client):
        """Initialize statistics."""
        self.settings = client.settings
        self.reset_stats()
        self.active_game = False
        self.high_score = self.score
        self.counter = 0

    def reset_stats(self):
        """Initialize statistics that chnage during the game."""
        self.lives_left = self.settings.lives
        self.score = self.settings.score
    
    def is_high_score(self):
        """Check If high score is greater than old highscore: set if True"""
        if self.score > self.high_score:
            self.high_score = self.score

    def wall_counter(self):
        """Detects how many times ball hits the walls of the game."""
        self.counter += 1
        print(self.counter)
    
    def reset_counter(self):
        """Reset wall counter"""
        self.counter = 0
        print('reset counter')