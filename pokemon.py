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

	def set_hair(self, hair: HairLength):
		self.personaFinal.hairLength = hair

	def set_skin(self, sk: Skin):
		self.personaFinal.skin = sk

	def set_height(self, height: HeightType):
		self.personaFinal.Height = height

	def set_waist(self, waist: WaistType):
		self.personaFinal.Waist = waist


class Pokemon:
	lvl = 1
	hp = 20
	exp = 0
	atk = 5
	speed = 20
	name = ''
	up = 200
	psycho = 0

	def lvlup(self):
		self.lvl = self.lvl + 1
		self.hp = self.hp + 20
		self.speed = self.speed + 5
		self.atk = self.atk + 10
		self.up = self.up * 2
		self.exp = 0

	def evolution(self):
		pass

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
		self.atk = self.atk - 10


class Psychoduck(Pokemon):
	psycho = 30

	def lvlup(self):
		self.psycho = self.psycho + 2

	def attack1(self):
		print('Психодак наносит удар силой мысли и наносит', self.atk, 'урона, а также понижает сопротивление вашего покемона к гипнозу на 10%')
		self.psycho = self.psycho + 10


class Magikarp(Pokemon):
	hp = 30

	def attack1(self):
		print('Мэджикарп создаёт барьер который может принять на себя', self.hp // 5, 'урона')