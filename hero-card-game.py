## Christopher Stanley
## December 2, 2018
## CSC 119.201
## Final Project - Hero Card Game

import pygame
from pygame. locals import *
import random

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    face_names = [None, '2', '3', '4', '5', '6',
                '7', '8', '9', '10', 'jack', 'queen',
                'king', 'ace']
    suit_names = ['clubs', 'spades', 'hearts', 'diamonds']

    def __str__(self):
        return "%s_of_%s" % (Card.face_names[self.face],
                            Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.face, self.suit
        t2 = other.face, other.suit
        return t1 < t2

class Deck:
    def __init__(self):
        self.cards = []
        for face in range(1,14):
        	for suit in range(4):
	            card = Card(face, suit)
	            self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def __getitem__(self,index):
    	return self.cards[index]

    def __len__(self):
    	return len(self.cards)

    def pop_card(self):
        return self.cards.pop()

    def remove_card(self,n):
    	self.cards.remove(self[n])

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def draw_card(self, n, deck, num):
        for i in range(num):
            self.cards.insert(n, deck.pop_card())

    def move_card(self, hand, n):
    	hand.add_card(self[n])
    	self.remove_card(n)

class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label

d1 = Deck()
d2 = Hand('Play Pile')
comp = Hand('Computer')
p1 = Hand('Player 1')

d1.move_card(d2,1)
d1.shuffle()
d1.deal_cards(comp,5)
d1.deal_cards(p1,5)

class Gameplay:
	black = (0,0,0)
	white = (255,255,255)
	green = (0,128,0)

	def __init__(self, width=800, height=600):
		pygame.init()
		pygame.display.set_caption('Hero Card Game')
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.clock = pygame.time.Clock()
		self.card_back = pygame.image.load('./cards/cardback1.png').convert()
		self.p1_card1 = pygame.image.load('./cards/%s.png' % (p1[0])).convert()
		self.p1_card2 = pygame.image.load('./cards/%s.png' % (p1[1])).convert()
		self.p1_card3 = pygame.image.load('./cards/%s.png' % (p1[2])).convert()
		self.p1_card4 = pygame.image.load('./cards/%s.png' % (p1[3])).convert()
		self.p1_card5 = pygame.image.load('./cards/%s.png' % (p1[4])).convert()

	def run_game(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						running = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if self.p1_card1.get_rect(topleft=((self.width * 0.23), (self.height * 0.7))).collidepoint(event.pos):
						if not self.invalid_play(p1[0],d2[len(d2)-1]):
							self.play_card(p1,0)
							self.p1_card1 = pygame.image.load('./cards/%s.png' % (p1[0])).convert()
						else:
							None
					elif self.p1_card2.get_rect(topleft=((self.width * 0.33), (self.height * 0.7))).collidepoint(event.pos):
						if not self.invalid_play(p1[1],d2[len(d2)-1]):
							self.play_card(p1,1)
							self.p1_card2 = pygame.image.load('./cards/%s.png' % (p1[1])).convert()
						else:
							None
					elif self.p1_card3.get_rect(topleft=((self.width * 0.43), (self.height * 0.7))).collidepoint(event.pos):
						if not self.invalid_play(p1[2],d2[len(d2)-1]):
							self.play_card(p1,2)
							self.p1_card3 = pygame.image.load('./cards/%s.png' % (p1[2])).convert()
						else:
							None
					elif self.p1_card4.get_rect(topleft=((self.width * 0.53), (self.height * 0.7))).collidepoint(event.pos):
						if not self.invalid_play(p1[3],d2[len(d2)-1]):
							self.play_card(p1,3)
							self.p1_card4 = pygame.image.load('./cards/%s.png' % (p1[3])).convert()
						else:
							None
					elif self.p1_card5.get_rect(topleft=((self.width * 0.63), (self.height * 0.7))).collidepoint(event.pos):
						if not self.invalid_play(p1[4],d2[len(d2)-1]):
							self.play_card(p1,4)
							self.p1_card5 = pygame.image.load('./cards/%s.png' % (p1[4])).convert()
						else:
							None
					self.set_board()
				elif event.type == pygame.QUIT:
					running = False
			
			self.screen.fill(self.green)
			self.set_board()
			pygame.display.update()
			self.clock.tick(60)
		pygame.quit()
		quit()

	def set_board(self):
		self.display_drawPile()
		self.display_playPile()
		self.display_compHand()
		self.display_playerHand()

	def display_drawPile(self):
		x = (self.width * 0.38)
		y = (self.height * 0.40)
		self.screen.blit(self.card_back, (x,y))

	def display_playPile(self):
		x = (self.width * 0.48)
		y = (self.height * 0.40)
		n = d2.__getitem__(len(d2)-1)
		card_image = pygame.image.load('./cards/%s.png' % (n))
		self.screen.blit(card_image, (x,y))

	def display_compHand(self):
		y = (self.height * 0.1)
		card1 = pygame.image.load('./cards/cardback1.png')
		self.screen.blit(card1, ((self.width * 0.33),y))
		card2 = pygame.image.load('./cards/cardback1.png')
		self.screen.blit(card2, ((self.width * 0.38),y))
		card3 = pygame.image.load('./cards/cardback1.png')
		self.screen.blit(card3, ((self.width * 0.43),y))
		card4 = pygame.image.load('./cards/cardback1.png')
		self.screen.blit(card4, ((self.width * 0.48),y))
		card5 = pygame.image.load('./cards/cardback1.png')
		self.screen.blit(card5, ((self.width * 0.53),y))

	def display_playerHand(self):
		y = (self.height * 0.7)
		self.screen.blit(self.p1_card1, ((self.width * 0.23),y))
		self.screen.blit(self.p1_card2, ((self.width * 0.33),y))
		self.screen.blit(self.p1_card3, ((self.width * 0.43),y))
		self.screen.blit(self.p1_card4, ((self.width * 0.53),y))
		self.screen.blit(self.p1_card5, ((self.width * 0.63),y))

	def play_card(self,hand,n):
		hand.move_card(d2,n)
		self.draw_card(hand,d1,n)

	def invalid_play(self,card,other):
		card.__lt__(other)

	def draw_card(self,hand,deck,n):
		hand.draw_card(n,deck,1)

	def draw_heroCard(self):
		pass

if __name__ == '__main__':
	play = Gameplay()
	play.run_game()