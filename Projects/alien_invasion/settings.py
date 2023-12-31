class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 5.5

        # Bullet settings
        self.bullet_speed = 4.0
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = (60, 0, 0)
        self.bullets_allowed = 10
