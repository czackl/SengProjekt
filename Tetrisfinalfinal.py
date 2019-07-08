

from random import randrange as rand
import pygame, sys
import gamemanager


config = {						#Rahmenbedingungen für Tetris
	'cell_size':	20,
	'cols':		13,
	'rows':		20,
	'delay':	800,
	'maxfps':	120
}

farben = [						#Farben für Steine und Hintergrund
(0,   0,   0),
(247, 255,   0),
(42, 255, 56),
(255, 155, 0),
(85, 76, 255),
(255, 0, 129),
(180, 0,   255),
(0,   220, 220)
]


steine = [			#Formen der Steine
	[[0, 0, 5],
	 [5, 5, 5]],

	[[0, 2, 2],
	 [2, 2, 0]],

	[[3, 3, 0],
	 [0, 3, 3]],

	[[4, 0, 0],
	 [4, 4, 4]],

	[[1, 1, 1],
	 [0, 1, 0]],

	[[6, 6, 6, 6]],

	[[7, 7],
	 [7, 7]]
]

def drehen(shape):
	return [ [ shape[y][x]
			for y in range(len(shape)) ]
		for x in range(len(shape[0]) - 1, -1, -1) ]

def collision(board, shape, offset):			#steine stapeln
	off_x, off_y = offset
	for cy, row in enumerate(shape):
		for cx, cell in enumerate(row):
			try:
				if cell and board[ cy + off_y ][ cx + off_x ]:
					return True
			except IndexError:
				return True
	return False

def remove_zeile(board, row):				#wenn eine Reihe vollständig ist, wird sie entfernt
	del board[row]
	return [[0 for i in range(config['cols'])]] + board

def join_matrixes(mat1, mat2, mat2_off):
	off_x, off_y = mat2_off
	for cy, row in enumerate(mat2):
		for cx, val in enumerate(row):
			mat1[cy+off_y-1	][cx+off_x] += val
	return mat1

def neues_Spielfeld():
	board = [ [ 0 for x in range(config['cols']) ]
			for y in range(config['rows']) ]
	board += [[ 1 for x in range(config['cols'])]]
	return board

class TetrisApp(object):
	def __init__(self):
		pygame.init()
		pygame.key.set_repeat(250,25)
		self.width = config['cell_size']*config['cols']
		self.height = config['cell_size']*config['rows']

		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.event.set_blocked(pygame.MOUSEMOTION)



		self.init_game()

	def neuer_Stein(self):					#neue steine generieren
		self.stone = tetris_shapes[rand(len(tetris_shapes))]
		self.stone_x = int(config['cols'] / 2 - len(self.stone[0])/2)
		self.stone_y = 0

		if check_collision(self.board,
		                   self.stone,
		                   (self.stone_x, self.stone_y)):
			self.gameover = True

	def init_game(self):
		self.board = new_board()
		self.new_stone()

	def zentrierung(self, msg):
		for i, line in enumerate(msg.splitlines()):
			msg_image =  pygame.font.Font(
				pygame.font.get_default_font(), 12).render(
					line, False, (255,255,255), (0,0,0))

			msgim_center_x, msgim_center_y = msg_image.get_size()
			msgim_center_x //= 2
			msgim_center_y //= 2

			self.screen.blit(msg_image, (
			  self.width // 2-msgim_center_x,
			  self.height // 2-msgim_center_y+i*22))

	def draw_matrix(self, matrix, offset):
		off_x, off_y  = offset
		for y, row in enumerate(matrix):
			for x, val in enumerate(row):
				if val:
					pygame.draw.rect(
						self.screen,
						colors[val],
						pygame.Rect(
							(off_x+x) *
							  config['cell_size'],
							(off_y+y) *
							  config['cell_size'],
							config['cell_size'],
							config['cell_size']),0)

	def bewegen(self, delta_x):
		if not self.gameover and not self.paused:
			new_x = self.stone_x + delta_x
			if new_x < 0:
				new_x = 0
			if new_x > config['cols'] - len(self.stone[0]):
				new_x = config['cols'] - len(self.stone[0])
			if not check_collision(self.board,
			                       self.stone,
			                       (new_x, self.stone_y)):
				self.stone_x = new_x
	def beenden(self):			#escape fuehrt zum gamemanager
		self.center_msg("...Spiel wird beendet...")
		pygame.display.update()
		gamemanager.main()

	def fastdrop(self):			#Stein schneller als normal fallen lassen
		if not self.gameover and not self.paused:
			self.stone_y += 1
			if check_collision(self.board,
			                   self.stone,
			                   (self.stone_x, self.stone_y)):
				self.board = join_matrixes(
				  self.board,
				  self.stone,
				  (self.stone_x, self.stone_y))
				self.new_stone()
				while True:
					for i, row in enumerate(self.board[:-1]):
						if 0 not in row:
							self.board = remove_row(
							  self.board, i)
							break
					else:
						break

	def rotate_stein(self):			#stein kann gedreht werden
		if not self.gameover and not self.paused:
			new_stone = rotate_clockwise(self.stone)
			if not check_collision(self.board,
			                       new_stone,
			                       (self.stone_x, self.stone_y)):
				self.stone = new_stone

	def toggle_pause(self):
		self.paused = not self.paused

	def start_game(self):
		if self.gameover:
			self.init_game()
			self.gameover = False

	def run(self):
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.update()

		Steuerung = {				#die steuerung
			'ESCAPE':	self.quit,
			'LEFT':		lambda:self.move(-1),
			'RIGHT':	lambda:self.move(+1),
			'DOWN':		self.drop,
			'UP':		self.rotate_stone,
			'p':		self.toggle_pause,
			'SPACE':	self.start_game
		}

		self.gameover = False
		self.paused = False

		pygame.time.set_timer(pygame.USEREVENT+1, config['delay'])
		clock = pygame.time.Clock()
		while 1:
			self.screen.fill((0,0,0))
			if self.gameover:
				self.center_msg("Gameover :( Zum fortsetzen bitte die 'Space'-Taste druecken")
			else:
				if self.paused:
					self.center_msg("*Pause*")
				else:
					self.draw_matrix(self.board, (0,0))
					self.draw_matrix(self.stone,
					                 (self.stone_x,
					                  self.stone_y))
			pygame.display.update()

			for event in pygame.event.get():		#die interaktionsmoeglichkeiten die der spieler hat
				if event.type == pygame.USEREVENT+1:
					self.drop()
				elif event.type == pygame.QUIT:
					self.quit()

				elif event.type == pygame.KEYDOWN:
					for key in key_actions:
						if event.key == eval("pygame.K_"
						+key):
							key_actions[key]()

			clock.tick(config['maxfps'])

if __name__ == '__main__':
	App = Tetris()
	App.run()
