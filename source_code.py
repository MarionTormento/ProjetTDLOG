
# créer un fichier directement dès que les gens dépose leurs informations 
# choix de la langue d'interrogation
# distance de Levenshtein
# ATTENTION PROBLEME DANS READ FILE il ne voit pas la denière ligne

import random


# Fiche de vocabulaire sur un thème unique, choix du titre du fichier, collect data à partir de l'interface graphique
class fch_interro():
	def __init__(self):
		self.nb_words = 0
		self.name = ""
		self.langue1 = ""
		self.langue2 = ""
		#self.datafiche = ""
		self.nametxt = ""
		#self.namedata = ""
		self.score = 0
		self.tableau = []
		self.to_guess = [] #mot à deviner
		self.answer = [] #réponse correspondante (self.to_guess[i] traduit = self.answer[i])

	def create_file(self): #crée un fichier .txt qui restera en mémoire à terme
		self.nametxt = self.name + ".txt"
		#self.namedata = "data_" + self.name + ".txt"
		self.fiche = open(self.nametxt, "w")  # ou "a"? ou créer un conflit si le nom est déjà utilisé 
		self.fiche.close()
		#self.datafiche = open(self.namedata,"w")
		#self.datafiche.write(self.langue1 + ":" + self.langue2 + '\n')
		#self.datafiche.close()

	def open_file(self): #crée un fichier .txt qui restera en mémoire à terme
		self.nametxt = self.name + ".txt"
		self.fiche = open(self.nametxt, "r")  # ou "a"? ou créer un conflit si le nom est déjà utilisé 
		self.fiche.close()

	def collect_data(self, word_lg1, word_lg2): #remplit le fichier la première fois
		definition = word_lg1 + ":" + word_lg2 + '\n'
		self.fiche = open(self.nametxt, "a")
		self.fiche.write(definition)
		self.nb_words += 1
		self.fiche.close()

	def read_file(self): #collecte ligne par ligne une première fois
		data = open(self.nametxt, "r")
		self.tableau = data.readlines()
		self.nb_words = len(self.tableau)
		data.close()

	def file_to_tableau(self): #convertit le fichier texte en un tableau ou on trouve en indice par les mots langue 1 et en pair les mots langue 2
		self.read_file()
		for i in range(self.nb_words):
			word_lg1 = self.tableau[i].split(':', 1)[0] #mot dans la langue 1
			word_intermediaire = self.tableau[i].split(':', 1)[1] #mot correspondant dans la langue 2 + saut de ligne
			word_lg2 = word_intermediaire.split('\n', 1)[0] #mot correspondant dans la langue 2
			self.tableau[i] = word_lg1 
			self.tableau.append(word_lg2) #(prend la position nb_words+i)
		self.interrogate()

	#def choose_lg(self): #renvoi 0 si premier langage, 1 sinon

	def interrogate(self):
		'''On suppose qu'on peut être intérrogé dans n'importe quel sens'''
		couple_interro = [i for i in range(self.nb_words)]
		choix_langue = [0, 1]
		for i in range(self.nb_words):
			idx_rdm = random.choice(couple_interro) #on choisit le couple de mot
			idx_language = random.choice(choix_langue) #on choisit le sens de l'intero
			self.to_guess.append(self.tableau[idx_rdm + idx_language*self.nb_words])
			self.answer.append(self.tableau[idx_rdm + (1 - idx_language)*self.nb_words])
			couple_interro.remove(idx_rdm)

#f = fch_interro()
#f.name = "animaux"
#f.nb_words = 4
#f.open_file()
#f.file_to_tableau()
#for i in range(8):
#	print(f.tableau[i])
#for i in range(f.nb_words):
#	print(f.to_guess[i])
#for i in range(f.nb_words):
#	print(f.answer[i])






