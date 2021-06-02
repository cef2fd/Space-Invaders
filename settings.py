class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):

		# Ship settings
		self.ship_speed = 2.0
		self.ship_limit = 3 

		# Screen settings
		self.screen_width = 1100
		self.screen_height = 650
		self.bg_color = (50, 50, 50)

		#Bullet settings
		self.bullet_speed = 1.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 5

		# Alien Settings
		self.alien_speed = .75
		self.fleet_drop_speed = 9
		# fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1