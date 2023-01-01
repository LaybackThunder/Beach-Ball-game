class GameStats():
    """Track statistics  for Catch The Ball."""

    def __init__(self, client):
        """Initialize statistics."""
        self.settings = client.settings
        self.reset_stats()
        self.active_game = True

    def reset_stats(self):
        """Initialize statistics that chnage during the game."""
        self.lives_left = self.settings.lives
        self.score = self.settings.score

