class Settings:
  """A class to store all settings for Alien Invasion."""

  def __init__(self):
    """Initialize the game's settings"""

    #Screen settings
    self.screen_width = 800
    self.screen_height = 500
    self.bg_color = (255, 255, 255)

    #Ship Settings
    self.ship_speed = 1.5