class GameStats:
    """Track statics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initializa statics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start Alien Invasion in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statics that can change during the game."""
        self.ships_left = self.settings.ship_limit