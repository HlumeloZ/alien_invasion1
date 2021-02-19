class Settings:
	"""A class to store all settings for Alien Invasion."""
	def __init__(self):
		"""Initialize the game's settings."""
		# Screen Settings
		self.screen_width = 600
		self.screen_height = 300
		self.bg_color = (42, 198, 209)
		# Ship settings
		self.ship_speed = 1.5
		# Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3
