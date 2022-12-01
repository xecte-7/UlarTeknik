''' Import library '''
import pygame	# Library untuk konsol game
import time		# Library untuk waktu
import random	# Library untuk pengacakan
import sys		# Library untuk sistem

''' Ukuran jendela '''
window_x = 720
window_y = 480

''' Pewarnaan '''
colorList = [
	pygame.Color(0, 0, 0), pygame.Color(255, 255, 255),
	pygame.Color(255,0,0), pygame.Color(0,255,0), pygame.Color(0,0,255),
	pygame.Color(255,255,0), pygame.Color(255,165,0), pygame.Color(255,192,203)
	]
colorBlack = colorList[0]
colorWhite = colorList[1]
colorRed = colorList[2]
colorGreen = colorList[3]
colorBlue = colorList[4]
colorYellow = colorList[5]
colorOrange = colorList[6]
colorPink = colorList[7]

''' Inisialiasi game '''
pygame.init()
''' Inisialisasi jendela program '''
game_title = "Ular Teknik"
game_icon = pygame.image.load(".//image//icon-1.png")
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption(game_title)
pygame.display.set_icon(game_icon)
''' Inisialiasasi Audio '''
daftarSuara = [pygame.mixer.Sound(".//sound//Eat-1.wav"), pygame.mixer.Sound(".//sound//Eat-2.wav"), pygame.mixer.Sound(".//sound//Eat-3.wav")]
soundDeath = pygame.mixer.Sound(".//sound//Death.wav")

# Kontrol FPS (frames per second)
fps = pygame.time.Clock()

''' Size Font '''
smallestFont_consolas = pygame.font.SysFont("Consolas", 15)
smallestFont_tms = pygame.font.SysFont("Times New Roman", 17)
smallestFont_tms = pygame.font.SysFont("Times New Roman", 15)
smallFont_tms = pygame.font.SysFont("Times New Roman", 20)
smallFont_consolas = pygame.font.SysFont("Consolas", 20)
mediumFont_tms = pygame.font.SysFont("Times New Roman", 30)
mediumFont_consolas = pygame.font.SysFont("Consolas", 30)
bigFont_tms = pygame.font.SysFont("Times New Roman", 50)
bigFont_consolas = pygame.font.SysFont("Consolas", 50)

# Kecepatan ular
snake_speed = 20

''' Fungsi Utama Aplikasi '''
def UlarTeknik():
	''' Pengaturan awal untuk ular '''
	# Posisi awal ular
	snake_position = [360, 120]
	# 3 blok pertama dari badan ular
	snake_body = [[360, 120], [350, 120], [340, 120]]
	# Posisi buah
	fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
	fruit_spawn = True
	# Arah jalan awal
	direction = 'RIGHT'
	change_to = direction
	# Skor awal
	score = 0
	
	''' Fungsi Menampilkan skor '''
	def show_score(skor):
		textScore = smallFont_tms.render(f'Skor : {skor}', True, colorWhite)
		textScore_rect = textScore.get_rect()
		textScore_rect.midtop = (50, 10)
		game_window.blit(textScore, textScore_rect)
	
	''' Fungsi Game Over '''
	def game_over():
		# Audio
		pygame.mixer.Sound.play(soundDeath)
		pygame.mixer.music.stop()
		# Mengosongkan layar
		game_window.fill(colorBlack)
		# Gambar background
		pygame.display.set_caption("[GAME OVER] Ular Teknik")
		backgroundImg2 = pygame.image.load(".//image//bg_death.jpg").convert()
		game_window.blit(backgroundImg2, (0,0))
		# Title Game Over
		textTitle = bigFont_tms.render("YOU DIED B#TCH!", True, colorWhite)
		textTitle_rect = textTitle.get_rect()
		textTitle_rect.midtop = (window_x/2, window_y/13)
		game_window.blit(textTitle, textTitle_rect)
		# Skor Game Over
		textSkor = mediumFont_consolas.render(f"Skor Anda : {str(score)}", True, colorRed)
		textSkor_rect = textSkor.get_rect()
		textSkor_rect.midtop = (window_x/2, window_y/4)
		game_window.blit(textSkor, textSkor_rect)
		# Instruksi
		textInstruksi1 = smallestFont_consolas.render(f"<< Tekan [ENTER] atau [SPACE] untuk melanjutkan >>", True, colorRed)
		textInstruksi1_rect = textInstruksi1.get_rect()
		textInstruksi1_rect.midtop = (window_x/2, window_y/2.5)
		game_window.blit(textInstruksi1, textInstruksi1_rect)
		textInstruksi2 = smallestFont_consolas.render(f"<< Tekan [ESC] atau [Q] untuk keluar >>", True, colorRed)
		textInstruksi2_rect = textInstruksi2.get_rect()
		textInstruksi2_rect.midtop = (window_x/2, window_y/2.5+25)
		game_window.blit(textInstruksi2, textInstruksi2_rect)
		# Credit Teknik
		textTeknik = smallestFont_tms.render("Teknik Komputer - Fakultas Teknik - Universitas Borneo Tarakan", True, colorWhite)
		textTeknik_rect = textTeknik.get_rect()
		textTeknik_rect.midtop = (window_x/2, window_y/1-60)
		game_window.blit(textTeknik, textTeknik_rect)
		# Credit Coder
		textMe = smallestFont_tms.render("~ Coded by Muhammad Rizky // Reference from GeeksForGeeks ~", True, colorWhite)
		textMe_rect = textMe.get_rect()
		textMe_rect.midtop = (window_x/2, window_y/1-35)
		game_window.blit(textMe, textMe_rect)
		# Menampilkan elemen-elemen text
		pygame.display.flip()
		# Menunggu respon dari pemain
		tunggu = True
		while tunggu:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
						tunggu = False
						UlarTeknik()
					elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()

	''' Looping utama '''
	while True:
		# Mendeteksi pencetan tombol
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					change_to = 'UP'
				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					change_to = 'DOWN'
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					change_to = 'LEFT'
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					change_to = 'RIGHT'
		# Perubahan arah ular
		if change_to == 'UP' and direction != 'DOWN':
			direction = 'UP'
		if change_to == 'DOWN' and direction != 'UP':
			direction = 'DOWN'
		if change_to == 'LEFT' and direction != 'RIGHT':
			direction = 'LEFT'
		if change_to == 'RIGHT' and direction != 'LEFT':
			direction = 'RIGHT'
		# Menggerakkan ular
		if direction == 'UP':
			snake_position[1] -= 10
		if direction == 'DOWN':
			snake_position[1] += 10
		if direction == 'LEFT':
			snake_position[0] -= 10
		if direction == 'RIGHT':
			snake_position[0] += 10
		# Menggambar blok badan baru sesuai posisi ular
		snake_body.insert(0, list(snake_position))
		
		# Jika ular memakan buah
		if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
			pygame.mixer.Sound.play(daftarSuara[random.randint(0,2)])
			pygame.mixer.music.stop()
			score += 5
			fruit_spawn = False
		else:
			# Menghapus blok paling belakang dari badan ular
			snake_body.pop()
		
		# Posisi buah
		if not fruit_spawn:
			fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
		fruit_spawn = True
		
		# Gambar background
		game_window.fill(colorBlack)
		backgroundImg1 = pygame.image.load(".//image//bg_main-2.jpg").convert()
		game_window.blit(backgroundImg1, (-40,20))
		
		# Menggambar badan ular ke layar
		for pos in snake_body:
			pygame.draw.rect(game_window, colorRed,
							pygame.Rect(pos[0], pos[1], 10, 10))
		# Menggambar buah ke layar
		pygame.draw.rect(game_window, colorOrange, pygame.Rect(
			fruit_position[0], fruit_position[1], 10, 10))
		
		# Game Over - Ular menyentuh pembatas
		if snake_position[0] < 0 or snake_position[0] > window_x-10:
			game_over()
		if snake_position[1] < 0 or snake_position[1] > window_y-10:
			game_over()
		# Game Over - Ular memakan badan sendiri
		for block in snake_body[1:]:
			if snake_position[0] == block[0] and snake_position[1] == block[1]:
				game_over()
		
		# Menampilkan score terus menerus
		show_score(str(score))
		# Refresh layar game
		pygame.display.update()
		# Frame Per Second /Refresh Rate
		fps.tick(snake_speed)

UlarTeknik()