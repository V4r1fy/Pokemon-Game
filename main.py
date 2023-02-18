# import telebot
#
# bot = telebot.TeleBot("5965990822:AAFuYx1D29gy2v7MHLSxMVgSYoei9WS5PSw", parse_mode=None)
# # 1. - Редактор персонажа

from enum import Enum

class WaistType(Enum):
	THIN = 0,
	MEDIUM = 1,
	FAT = 2

class HeightType(Enum):
	HIGH = 0,
	MEDIUM = 1,
	LEPRIKONE = 2

class HairLength(Enum):
	HIGH = 0,
	MEDIUM = 1,
	SKINHEAD = 2

class Skin(Enum):
	WHITE = 0,
	SUNBURNT = 1,
	BLACK = 2

class EyeSize(Enum):
	TIGHT = 0,
	MEDIUM = 1,
	WIDE = 2

class Persona:
	hairColor = 'black'
	hairLength = HairLength.MEDIUM
	skin = Skin.WHITE
	eyeColor = 'blue'
	eyeSize = EyeSize.MEDIUM
	Height = HeightType.MEDIUM
	Waist = WaistType.FAT

class PersonaBuilder():
	def __init__(self):
		self.personaFinal = Persona()

	def set_eyes(self, eye: EyeSize):
		self.personaFinal.eyeSuze = eye

class  Pokemon:
	lvl = 1
	hp = 20
	exp = 0
	atk = 5
	speed = 20
	name = ''
	up = 200

	def lvlup(self):
		self.lvl = self.lvl + 1
		self.hp = self.hp + 20
		self.speed = self.speed + 5
		self.atk = self.atk + 10
		self.up = self.up * 2
		self.exp = 0

	def attack1(self):
		pass

	def attack2(self):
		pass

	def attack3(self):
		pass

	def attack4(self):
		pass


class Pikachu(Pokemon):
	speed = 50

	def attack1(self):
		self.atk = self.atk + 10
		print('Пикачу ударяет разрядом молнии и наносит', self.atk, 'урона')

class Chermonder(Pokemon):
	atk = 10
	hp = 25

	def attack1(self):
		self.atk = self.atk + 10
		print('Чермондер запускает в противника шар огня который наносит', self.atk, 'урона')

























# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
#
# bot.infinity_polling()