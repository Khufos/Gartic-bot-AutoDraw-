from PIL import Image as img  
from datetime import datetime
from convertHSV import RGB_HSV
from time import sleep, time
import random
import pyautogui
import threading
import keyboard
import sys
pyautogui.PAUSE = 1 / 100
class Gartic(threading.Thread):
	def __init__(self,paleta_cor_x,paleta_cor_y,p_x,p_y,screen,canto_x='',canto_y='',baixo_x='',baixo_y=''):
		#screen:str,p_x,p_y,paleta_cor_x, paleta_cor_y
	    threading.Thread.__init__(self)
	    self.esc_hue = 360/180
	    self.esc_sat = 100/100
	    self.esc_val = 100/100
	    self.paleta_cor_x = paleta_cor_x
	    self.paleta_cor_y = paleta_cor_y
	    self.screen = screen
	    self.p_x = p_x
	    self.p_y = p_y
			
	def paleta_cor(self):
		pyautogui.click(self.paleta_cor_x ,self.paleta_cor_y)
		
	def paleta_cruz(self):
		cruz_canto = pyautogui.locateOnScreen('imagens/cruz2.png')
		cruz_centro = pyautogui.center(cruz_canto)
		self.canto_x = cruz_centro[0]
		self.canto_y = cruz_centro[1]
		pyautogui.click(self.paleta_cor_x,self.paleta_cor_y)
		
	def paleta_seta(self):
		setinha_barra_canto = pyautogui.locateOnScreen('imagens/seta.png')
		setinha_barra_centro = pyautogui.center(setinha_barra_canto)
		self.baixo_x = setinha_barra_centro[0]
		self.baixo_y = setinha_barra_centro[1]
		
				   
		
	def paleta_autodraw(self):
		px_atual= 1
		px_anterior= 0
		imagem = img.open(self.screen)
		largura, altura = imagem.size
		for y in range(altura):
			for x in range(largura):
				pixel = imagem.getpixel((x, y))
				R, G, B = pixel[0], pixel[1], pixel[2]
				HSV = RGB_HSV(R, G, B)
				Hue, Saturation, Value = HSV[0], HSV[1], HSV[2]
				px_atual = (Hue, Saturation, Value)
				if px_atual != px_anterior:
				   pyautogui.click(self.paleta_cor_x,self.paleta_cor_y)
				   x_cor = self.canto_x + (Hue/self.esc_hue)
				   y_cor = self.canto_y - (Saturation/self.esc_sat)
				   pyautogui.click(x_cor, y_cor)
				   x_luminosidade = self.baixo_x
				   y_luminosidade = self.baixo_y - (Value/self.esc_val)
				   pyautogui.click(x_luminosidade, y_luminosidade)
				pyautogui.click(self.p_x + x, self.p_y+ y)
				px_anterior = (Hue, Saturation, Value)


'''a = Gartic(224,376,324,146,"desenhos/foca.jpg")
a.paleta_cor()
a.paleta_cruz()
a.paleta_seta()
a.paleta_autodraw()'''


		


