class Settings():
    """A class to store all settings for Catch The Beach Ball."""

    def __init__(self):
        """Initialize the games settings."""
        # Screen settings
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 800
        self.LIGHT_GRAY = (230, 230, 230)
        self.BACKGROUND_COLOR = self.LIGHT_GRAY

        # Ball settings
        self.STARTING_BALL_SPEED = 5
        self.ball_speed = self.STARTING_BALL_SPEED
        self.ball_acceleration = 0.5