"""Settings for Alien Invasion."""

import random


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (
            random.randint(0, 230),
            random.randint(0, 230),
            random.randint(0, 230),
        )
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 4000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.speedup_scale = 3.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.points_alien_red = 50
        self.points_alien_yellow = 25
        self.points_alien_green = 10
        self.score_scale = 1.5
        self.fleet_drop_speed = 10

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        self.points_alien_red = int(self.points_alien_red * self.score_scale)
        self.points_alien_yellow = int(self.points_alien_yellow * self.score_scale)
        self.points_alien_green = int(self.points_alien_green * self.score_scale)
