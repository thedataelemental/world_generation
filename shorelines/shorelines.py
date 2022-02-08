# shorelines.py
# Randomly generates a crude world map with appropriate shorelines.
# Author: Jackie P, aka TheDataElemental


import random
import pygame


# Convert water-adjacent land tiles to appropriate type of shore tiles
def convert_to_shore(y, x):
	global world
	global shore_lines
	global tiles
	
	# Find values of cardinal neighbor tiles
	N = world[y - 1][x] 
	E = world[y][x + 1] 
	S = world[y + 1][x] 
	W = world[y][x - 1] 
	
	nbr_tiles = [N, E, S, W]
	
	# Assign shoreline tile type based on cardinal neighboring tiles
	
	if nbr_tiles == [tiles["water"], tiles["land"], tiles["land"], tiles["water"]]:
		shore_lines[y][x] = tiles["NW_shore"]
	
	elif nbr_tiles == [tiles["water"], tiles["water"], tiles["land"], tiles["land"]]:
		shore_lines[y][x] = tiles["NE_shore"]
		
	elif nbr_tiles == [tiles["land"], tiles["water"], tiles["water"], tiles["land"]]:
		shore_lines[y][x] = tiles["SE_shore"]
		
	elif nbr_tiles == [tiles["land"], tiles["land"], tiles["water"], tiles["water"]]:
		shore_lines[y][x] = tiles["SW_shore"]
	
	elif nbr_tiles == [tiles["land"], tiles["land"], tiles["water"], tiles["land"]]:
		shore_lines[y][x] = tiles["S_shore"]
	
	elif nbr_tiles == [tiles["water"], tiles["land"], tiles["land"], tiles["land"]]:
		shore_lines[y][x] = tiles["N_shore"]
	
	elif nbr_tiles == [tiles["land"], tiles["land"], tiles["land"], tiles["water"]]:
		shore_lines[y][x] = tiles["W_shore"]
	
	elif nbr_tiles == [tiles["land"], tiles["water"], tiles["land"], tiles["land"]]:
		shore_lines[y][x] = tiles["E_shore"]
	
	elif nbr_tiles == [tiles["water"], tiles["land"], tiles["water"], tiles["land"]]:
		shore_lines[y][x] = tiles["horizontal_straight"]
		
	elif nbr_tiles == [tiles["land"], tiles["water"], tiles["land"], tiles["water"]]:
		shore_lines[y][x] = tiles["vertical_straight"]
		
	elif nbr_tiles == [tiles["water"], tiles["water"], tiles["land"], tiles["water"]]:
		shore_lines[y][x] = tiles["N_tip"]
		
	elif nbr_tiles == [tiles["water"], tiles["water"], tiles["water"], tiles["land"]]:
		shore_lines[y][x] = tiles["E_tip"]
		
	elif nbr_tiles == [tiles["land"], tiles["water"], tiles["water"], tiles["water"]]:
		shore_lines[y][x] = tiles["S_tip"]
		
	elif nbr_tiles == [tiles["water"], tiles["land"], tiles["water"], tiles["water"]]:
		shore_lines[y][x] = tiles["W_tip"]
		
	elif nbr_tiles == [tiles["water"], tiles["water"], tiles["water"], tiles["water"]]:
		shore_lines[y][x] = tiles["island"]


# Draw world map, one tile at a time	
def render_world():
	global shore_lines
	global world_width
	global world_height

	for y in range(0, world_height - 1):
		for x in range(0, world_width - 1):
			screen.blit(tile_images[shore_lines[y][x]], (int(x) * 32, int(y) * 32))
			
	pygame.display.flip()


# Possible tile types for world rep 2 (shorelines)
tiles = {
	'water': '0',
	'land': '1',
	'N_shore': '2',
	'E_shore': '3',
	'S_shore': '4',
	'W_shore': '5',
	'NW_shore': '6',
	'NE_shore': '7',
	'SE_shore': '8',
	'SW_shore': '9',
	'vertical_straight': 'A',
	'horizontal_straight': 'B',
	'N_tip': 'C',
	'E_tip': 'D',
	'S_tip': 'E',
	'W_tip': 'F',
	'island': 'G',
	}

# Possible tile types for world rep 3 (terrain)
terrain = {
	'water': '0',
	'land': '1',
	'forest': '2',
	'mountain': '3',
	'town': '4',
	}

world_width = 10
world_height = 10

# World rep 1 (water and land) - starting values
world = [
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	]

# World rep 2 (detailed - adds corner and cardinal shorelines)
# Filled out later automatically
shore_lines = [
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
	
	]

# Todo: add a third world rep here to accound for terrain type -
# Grass, forest, mountain, etc

# Randomly generate 2D world rep array (0 = water, 1 = land)
for y in range(1, (world_height - 1)):
	for x in range(1, (world_width - 1)):
		world[y][x] = str(random.randint(0, 1))

# Add shoreline properties to world rep tiles

# Iterate through rows of matrix
for y in range(1, (world_height - 1)): 
	# Iterate through columns of matrix
	for x in range(1, (world_width - 1)): 
		# If this tile is land (is not water)...
		if world[y][x] == tiles["land"]:
			# Default 'center land' assignment
			shore_lines[y][x] = tiles["land"]
			
			# Do actual conversion to shorelines tiles
			convert_to_shore(y, x)
			
# Show detailed world map w/ shorelines
for i in shore_lines:
	print(i)

# Start pygame window
pygame.init()
screen = pygame.display.set_mode((288, 288), \
	pygame.HWSURFACE | pygame.DOUBLEBUF, vsync = 1)
pygame.display.set_caption("TERRAIN GENERATOR")
# game_icon = pygame.image.load("Assets/Exports/Art/Backgrounds/terrain_icon.png")
# pygame.display.set_icon(game_icon)

# Load image assets
NE_coast = pygame.image.load\
	("shore_tiles/NE_coast.png").convert_alpha()

SE_coast = pygame.image.load\
	("shore_tiles/SE_coast.png").convert_alpha()
	
SW_coast = pygame.image.load\
	("shore_tiles/SW_coast.png").convert_alpha()
	
NW_coast = pygame.image.load\
	("shore_tiles/NW_coast.png").convert_alpha()
	
N_coast = pygame.image.load\
	("shore_tiles/N_coast.png").convert_alpha()
	
E_coast = pygame.image.load\
	("shore_tiles/E_coast.png").convert_alpha()
	
S_coast = pygame.image.load\
	("shore_tiles/S_coast.png").convert_alpha()
	
W_coast = pygame.image.load\
	("shore_tiles/W_coast.png").convert_alpha()
	
horizontal_straight = pygame.image.load\
	("shore_tiles/horizontal_straight.png").convert_alpha()
	
vertical_straight = pygame.image.load\
	("shore_tiles/vertical_straight.png").convert_alpha()
	
land = pygame.image.load\
	("shore_tiles/land.png").convert_alpha()

island = pygame.image.load\
	("shore_tiles/island.png").convert_alpha()
	
water = pygame.image.load\
	("shore_tiles/water.png").convert_alpha()
	
N_tip = pygame.image.load\
	("shore_tiles/N_tip.png").convert_alpha()
	
E_tip = pygame.image.load\
	("shore_tiles/E_tip.png").convert_alpha()
	
S_tip = pygame.image.load\
	("shore_tiles/S_tip.png").convert_alpha()

W_tip = pygame.image.load\
	("shore_tiles/W_tip.png").convert_alpha()

tile_images = {
	'0': water,
	'1': land,
	'2': N_coast,
	'3': E_coast,
	'4': S_coast,
	'5': W_coast,
	'6': NW_coast,
	'7': NE_coast,
	'8': SE_coast,
	'9': SW_coast,
	'A': vertical_straight,
	'B': horizontal_straight,
	'C': N_tip,
	'D': E_tip,
	'E': S_tip,
	'F': W_tip,
	'G': island,
	}

# Draw the world to the screen
render_world()

# Wait ten seconds
pygame.time.delay(10000)

pygame.quit()
